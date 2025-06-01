from viewBase import viewBase
import pygame
from enum import Enum

class Direction(Enum):
    Next = 1
    Back = 2
    Modes = 3
    Partidas = 4
    Again = 5

class NavigationGraph:
    views = []
    #TODO: Add a dictionary to hold transitions between views

    def __init__(self):
        pass

    def addView(self, view):
        self.views.append(view)
    
    def addTransition(srcView: viewBase, destView: viewBase, direction: Direction):
        if srcView not in NavigationGraph.views:
            NavigationGraph.views.append(srcView)

        if destView not in NavigationGraph.views:
            NavigationGraph.views.append(destView)

    def go(view: viewBase, direction: Direction):
        if direction == Direction.Next:
            # Logic to go to the next view
            pass
        elif direction == Direction.Back:
            # Logic to go back to the previous view
            pass
        elif direction == Direction.Modes:
            # Logic to switch to modes view
            pass
        elif direction == Direction.Partidas:
            # Logic to switch to partidas view
            pass
        elif direction == Direction.Again:
            # Logic to restart the current view
            pass
        else:
            raise ValueError("Invalid navigation direction")
        
        tempView = views[]
