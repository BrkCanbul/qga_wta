
from abc import ABC


class BaseOptimizer(ABC):
    def __init__(self, model, **kwargs):
        self.model = model
    
    def optimize(self, *args, **kwargs):
        
        raise NotImplementedError("The optimize method must be implemented in the subclass.")

    