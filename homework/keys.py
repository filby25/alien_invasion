import pygame
import sys

class Rocket:
    """Overall class to manage the hw"""

    def __init__(self):

        pygame.init()
        screen = pygame.display.set_mode((300, 300))
        screen.fill((230, 0, 0))

    def run_hw(self):
        """Start the main loop for the hw"""
        while True:
            self._check_events()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key==pygame.K_RIGHT:
            print('right')
        elif event.key==pygame.K_LEFT:
            print('left')
        elif event.key==pygame.K_DOWN:
            print('down')
        elif event.key==pygame.K_UP:
            print('up')
        elif event.key==pygame.K_q:
            print('q')

        pygame.display.flip()
if __name__=='__main__':
    #make a game instance and run the game
    ai=Rocket()
    ai.run_hw()




