import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 0, 0), (160, 150), 17)
circle(screen, (255, 0, 0), (240, 150), 15)
circle(screen, (0, 0, 0), (160, 150), 6)
circle(screen, (0, 0, 0), (240, 150), 5)
rect(screen, (0, 70, 0), (130, 200, 130, 15))
polygon(screen, (0, 0, 0), [(150,100), (190,150)], 10)
polygon(screen, (0, 0, 0), [(250,100), (210,150)], 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()