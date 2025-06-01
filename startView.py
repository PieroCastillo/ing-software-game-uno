import pygame
from viewBase import viewBase

class startView(viewBase):
    logoImg: pygame.Surface
    
    def __init__(self):
        super().__init__()
        self.logoImg = pygame.transform.scale_by(pygame.image.load("assets/UNO_Logo.svg.png").convert(), 0.5)

    def render(self, surface):
        surface.fill("black")

        self.imgCenter = self.logoImg.get_rect()
        self.imgCenter.center = surface.get_rect().center

        surface.blit(self.logoImg, self.imgCenter)