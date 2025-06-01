import pygame
from viewBase import viewBase
from startView import startView

pygame.init()

h, w = 1280, 720

screen = pygame.display.set_mode((h, w))
clock = pygame.time.Clock()
running = True

currentView: viewBase = startView()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Renderiza la ventana de inicio acá
    screen.fill("black")
    
    currentView.render(screen)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()