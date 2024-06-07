#!/usr/bin/env python3
#
# base class for crossover operations

from abc import ABC, abstractmethod
from typing import List

from ...population import Individual

class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1: Individual, parent2: Individual) -> List[Individual]:
        pass
