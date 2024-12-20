import pygame as game
from pygame.sprite import Sprite

class Circles(Sprite):
    def __init__(self,ai_settings,screen,x,y):
        super().__init__()
        self.screen=screen
        self.x=x
        self.y=y
        self.ai_settings=ai_settings
        self.radius=ai_settings.circle_size
        self.color=ai_settings.circle_color
        self.border=ai_settings.circle_width
        self.image=game.Surface((self.radius*2,self.radius*2),game.SRCALPHA)
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.center=(self.x,self.y)
        self.draw_circle()
        
    def draw_circle(self):
        game.draw.circle(self.image,self.color,(self.radius,self.radius),self.radius,self.border)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)