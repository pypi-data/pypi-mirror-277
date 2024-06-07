#!/usr/bin/env python3
#
# History evolution for fitness metric

import pandas as pd
from .base import EvolutionHistory

class AvgFitnessEvolutionHistory(EvolutionHistory):
    def __init__(self, axes: Axes):
        super(AvgFitnessEvolutionHistory, self).__init__(axes)
        self.history = pd.DataFrame(columns=["generation", "avg_fitness"])

    def register(self, context: Evolution):
        record = {"generation": context.generation, "avg_fitness": context.fitness_metric.avg_fitness}
        self.history._append(record)

    def plot(self):
        pass
