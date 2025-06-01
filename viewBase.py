import pygame

class viewBase:
    def __init__(self):
        pass

    def render(self, surface):
        NotImplementedError("This method should be overridden by subclasses")