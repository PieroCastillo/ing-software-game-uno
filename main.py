import pygame

pygame.init()

h, w = 1280, 720

screen = pygame.display.set_mode((h, w))
clock = pygame.time.Clock()
running = True

logoImg = pygame.transform.scale_by(pygame.image.load("assets/UNO_Logo.svg.png").convert(), 0.5)
# rectlogoImg = logoImg.get_rect()
# rectlogoImg.center = (h // 2, w // 2)
# rectlogoImg.size = (h // 4, w // 4)
# logoImg.set_rect(rectlogoImg)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    imgCenter = logoImg.get_rect()
    imgCenter.center = screen.get_rect().center

    screen.blit(logoImg, imgCenter)

    # RENDER YOUR GAME HERE


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()