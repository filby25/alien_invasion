import pygame
import time

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((0, 0, 210))
pygame.display.flip()
#loop otherwise python will stop running
time.sleep(2)