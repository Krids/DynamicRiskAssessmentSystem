"""
Abstract pipeline class, this abstract class is responsible for the signature on the pipeline classes that will inherit.

Author: Felipe Lana Machado
Date: 30/08/20222
"""
from abc import ABC, abstractmethod


class Pipeline(ABC):

    @abstractmethod
    def run(self):
        pass
