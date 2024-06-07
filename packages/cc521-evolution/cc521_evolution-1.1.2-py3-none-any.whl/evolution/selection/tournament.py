#!/usr/bin/env python3
#
# Implementation of tournament selection strategy

import random
import functools
import collections
from typing import Callable

from .misc import FitnessEvaluation
from .base import SelectionStrategy
from ..fitness import Fitness

class TournamentSelection(SelectionStrategy):
    """Tournament selection strategy (Linear Classification)"""
    def __init__(self, fitness: Fitness, 
                 selection_probability: Callable[[int, float], float] = lambda i, s, u: (2.0-s)/u + 2.0*i*(s-1)/(u*(u-1)),
                 sample_size: int):
        super(SelectionStrategy, self).__init__(fitness)
        self.selection_probability: Callable = selection_probability
        self.sample_size = sample_size

    def select(self, k: int, individuals: List[Individual], s: float = 2.0) -> List[Individual]:
        """
        Inputs
            k: number of individuals to select
            individuals: collection of individuals to select from
            s: parameter of selection probability function (best individual advantage)
        
        Ouputs
            k selected individuals
        """
        n = len(individuals)
        probability_func = functools.partial(self.selection_probability, u=n)
        
        selected_individuals = []
        for tournament in range(k):
            # selecting "sample_size" individuals randomly for tournament
            participants = random.choice(individuals, k=self.sample_size) 

            fitness = [FitnessEvaluation(x, self.fitness(x)) for x in individuals])
            sorted_fitness = sorted(fitness, key=lambda t: t.fitness)

            sorted_individuals = [x.individual for x in sorted_fitness]

            # probability of selection for each individual (based on rank [linear clssification])
            probability = [probability_func(i, s) for i in range(n)] 

            # instead of selecting the more competent individual (based on fitness) 
            # we are going to randomly select individuals using the rank based [lineal classification] selection strategy
            #   with parameter s=2.0 (best individual advantage) 
            #   [to favor the best individual, but mantain the stochasticity of the selection process]
            selected = random.choice(sorted_individuals, weights=probability, k=1)
            selected_individuals.append(selected)

        return selected_individuals
