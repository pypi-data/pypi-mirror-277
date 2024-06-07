#!/usr/bin/env python3
#
# Base Generatic Evolutionary Algorithm Class
from __future__ import annotations

import uuid
import random
import logging
import json
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from tqdm import tqdm
from abc import abstractmethod
from typing import Callable, Concatenate, List
from collections.abc import Iterable

from .fitness import FitnessEvaluation
from .population import PopulationGenerator, Population, Individual
from .selection.base import SelectionStrategy
from .variation.crossover.base import CrossoverStrategy
from .variation.mutation.base import MutationStrategy
from .variation.probability import VariationProbability, ConstantVariationProbability

from .metrics import EvolutionMetric, FitnessMetric

class Evolution:
    def __init__(self, population_generator: PopulationGenerator, *,
                 fitness: Callable[[object], float],
                 selection_strategy: SelectionStrategy, # parents selection strategy
                 crossover_strategy: CrossoverStrategy,
                 mutation_strategy: MutationStrategy,
                 crossover_prob: Union[float, Iterable] , mutation_prob: Union[float, Iterable],
                 metrics: dict[str, EvolutionMetric] = None, # metrics about the evolution
                 history: List[Type[EvolutionHistory]] = None,
                 next_generation_selection_strategy: SelectionStrategy = None):
        self.fitness_func = fitness
        self.population_generator = population_generator
        self.population: Population = None
        self.generation: int = 1

        self.best: Individual = None # invidividual with the largest fitness value on the last generation
        self.worse: Individual = None # invidividual with the smallest fitness value on the last generation

        self.parent_selection_strategy = selection_strategy
        self.next_generation_selection_strategy = selection_strategy
        if next_generation_selection_strategy is not None:
            self.next_generation_selection_strategy = next_generation_selection_strategy

        # variation(crossover and mutation)
        self.crossover_strategy = crossover_strategy
        self.crossover_prob = crossover_prob
        if not isinstance(crossover_prob, Iterable):
            self.crossover_prob = ConstantVariationProbability(value=crossover_prob)

        self.mutation_strategy = mutation_strategy
        self.mutation_prob = mutation_prob
        if not isinstance(mutation_prob, Iterable):
            self.mutation_prob = ConstantVariationProbability(value=mutation_prob)

        self.logger: logging.Logger = logging.getLogger(type(self).__name__)

        ## metrics
        self.fitness_metric = FitnessMetric(fitness=fitness)

        metrics = {} if metrics is None else metrics
        self.metrics = dict({"fitness": self.fitness_metric}, **metrics)

        # subcribers of evolution process (notification to subcribers is done every generation)
        self.subcribers: List[EvolutionSubscriber] = []

        ## history
        if history:
            self.figure = plt.figure()
            self.subcribers += [history_cls(axes=Axes(self.figure)) for history_cls in history]

    def select_next_generation(self, k: int, individuals: List[Individual]) -> List[Individual]:
        """ Select k individual from the current population using a selection strategy"""
        return self.next_generation_selection_strategy.select(k, individuals)

    def select_parents(self, k: int, individuals: List[Individual], *args, **kwargs) -> List[Individual]:
        """ Select individuals using a selection strategy"""
        return self.parent_selection_strategy.select(k, individuals)

    def variation(self, k: int, parents: List[Individual]) -> List[Individual]:
        """Perform variation operators (crossover or mutation) on a group of selected individual (parents)
        to generate k individuals"""

        count = 0
        generated_individuals = []
        while count < k:
            r = random.random()
            if next(self.crossover_prob) > r:
                parent1 = random.choice(parents)
                parent2 = random.choice(parents) # check that the two parent are different individuals

                children = self.crossover_strategy.crossover(parent1, parent2)
                generated_individuals += children
                count += len(children)

            if next(self.mutation_prob) > r:
                parent = random.choice(parents)
                children = self.mutation_strategy.mutate(parent)
                generated_individuals += children
                count += len(children)

        # since the crossover and mutation can generate more than one individual, therefore can generate more than
        # the required elements, we are only seleting the first k generated (But perhaps a more appropiated way of doing this
        # is selecting the best k)
        if count > k:
            self.logger.info(f"Variation operation have been generated {count} individuals. Taking only {k} individuals")
        return generated_individuals[:k]


    def converged(self) -> bool:
        """
        Function that determine if the current population of the evolution satisfied the convergency criteria

        True means that the evolution process has converged and the evolution must be stoped,
            otherwise the evolution process will continue
        """
        return False # if the problen hasn't a well defined stop condition, just return False

    def evaluate(self, individuals: List[Individual]) -> dict:
        """Evaluate metrics on evolved individuals (next-generation)"""
        self.fitness_metric.evaluate(individuals)

        self.best = self.fitness_metric.best.individual
        self.worse = self.fitness_metric.worse.individual

        #evaluate extra metrics
        # for name, metric in self.metrics.items():
        #     metric.evaluate(individuals)

        return {'generation': self.generation,
                'fitness': {
                    'average': self.fitness_metric.avg_fitness,
                    'best': self.fitness_metric.best.fitness,
                    'worse': self.fitness_metric.worse.fitness
                    },
                'individual': {
                    'best': [gen.value for gen in self.best.chromosome.genes],
                    'worse': [gen.value for gen in self.worse.chromosome.genes]
                    }
                }

    #[DEPRECATED] This function is maintain only to suport legacy examples
    def population_fitness(self) -> List[float]:
        """Compute the fitness of the current population"""
        return [self.fitness_func(individual) for individual in self.population]

    def evolution(self, population_size: int, max_generations: int,
                  selection: int, descendents: int,
                  initial_individuals: List[Individual] = None) -> Population:
        """
        perform the evolution of initial population using multiple variation operations
        this method quits when max number of iteratons were done or the convergence condition was met

        Inputs
        =======
        max_generations: maximun number of iterations (or generations - evolutions)
        selection: number of parents selected fom current population (for generate next generation)
        descendents: number of descendents to generate using variation operation over selected individuals

        Output
        ======
        evolved population
        """

        k = selection # number of individual to selecte in each generation for reproduction
        self.population = self.population_generator.random(population_size,
                                                           initial_individuals=initial_individuals)

        with tqdm(total=max_generations) as pbar: # progress bar
            while self.generation < max_generations and not self.converged():
                #import pdb; pdb.set_trace()
                population = self.population.individuals # current generation

                selected = self.select_parents(k, population) # select individuals from current generation for reproduction
                generated = self.variation(descendents, selected + population) # reproduction (crossover + mutation)

                # select individuals for next generation
                population = self.select_next_generation(population_size, generated + population)

                self.population.individuals = population # replace old generation with a new one
                self.generation += 1

                pbar.update(1)

                # compute metric of current generation (next-generation)
                evaluation = self.evaluate(self.population.individuals)

                pbar.set_postfix({'generation': self.generation, **evaluation['fitness']})

                # notify subscribers about new generation
                # this subscribers generally register some information about evaluated metrics of new generation
                for subscriber in self.subcribers:
                    subcriber.register(self)

        if self.converged():
            self.logger.info("The evolution process converged (generation: {self.generation})")

        # best is element with the largest fitness and worse is the element with the smallest fitness
        # Therefore in a maximization problem our objective is find the individual that has the best fitness (the best),
        # however in a minimization problem our objective is find the individual with the lowerst fitness (the worse)
        print("\n" + "="*20)
        print(f"Best: {self.best.phenotype}")
        print(f"Worse: {self.worse.phenotype}")
        print("="*20)

        """
        file = f"evolution-{uuid.uuid4().hex}.json"
        print(f"Writing results to: {file}")
        with open(file, 'w') as f:
            json.dump(evaluation, f, indent=4)
        """
        return self.population

    # perform evolution process mutiple times
    def evolve(self, population_size: int, max_generations: int,
               selection: int, descendents: int,
               evolutions: int = 10,
               initial_individuals: List[Individual] = None):

        for evol in range(evolutions):
            print(f"Evolution: {evol+1}")
            population = self.evolution(population_size=population_size,
                                        max_generations=max_generations,
                                        selection=selection,
                                        descendents=descendents,
                                        initial_individuals=initial_individuals)

            self.generation = 0 # reset generation counter for next evolution

            # TODO
            # - evaluate performance of population
            # - consider select best individuals of previous evolution for next evolution
