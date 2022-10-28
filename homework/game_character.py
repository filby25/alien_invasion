import pygame
import time
pygame.init()

screen= pygame.display.set_mode((200,200))
screen.fill((190,190,190))
character = pygame.image.load('../images/riot.bmp')
screen_rectangle= screen.get_rect()
character_rectangle= character.get_rect()
character_rectangle.center= screen_rectangle.center
screen.blit(character,character_rectangle)
pygame.display.flip()
time.sleep(10)