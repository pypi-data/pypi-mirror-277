#!/usr/bin/env python3
#
# History base classes - A history class records points of interest of an evolution process

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from abc import ABC, abstractmethod
from ..evolution import Evolution


class EvolutionSubscriber(ABC):
    """Base class to subcriber to specific information about any metric or information about an evolution"""

    @abstractmethod
    def register(self, context: Evolution):
        """Register an specific information about the evolution process (called every generation)"""
        pass


class EvolutionHistory(EvolutionSubscriber):
    def __init__(self, axes: Axes):
        self.name = type(self).__name__
        self.axes = axes

    @abstractmethod
    def plot(self):
        pass
