import pygame
import sys

from shooter_settings import Shooter_settings
from shooter_ship import Shooter_ship
from shooter_bullet import Shooter_bullet

class Sideways_shooter:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.shooter_settings=Shooter_settings()



        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.shooter_settings.screen_width=self.screen.get_rect().width
        self.shooter_settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.shooter_ship = Shooter_ship(self)
        self.bullets=pygame.sprite.Group()

        #Set the background color
        self.bg_color=(230,230,230)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()

        #Get rid of bullets that have disappeared
        for shooter_bullet in self.bullets.copy():
            if shooter_bullet.rect.top <= 0:
                self.bullets.remove(shooter_bullet)
    def run_game (self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.shooter_ship.update()
            self._update_bullets()
            self._update_screen()
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """Respond to Keypresses"""
        if event.key==pygame.K_UP:
            self.shooter_ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.shooter_ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """Respond to Key releases"""
        if event.key==pygame.K_UP:
            self.shooter_ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.shooter_ship.moving_down=False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.shooter_settings.bullets_allowed:
            new_bullet=Shooter_bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.shooter_settings.bg_color)
        self.shooter_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    hw=Sideways_shooter()
    hw.run_game()