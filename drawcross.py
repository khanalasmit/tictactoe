import pygame as game
from pygame.sprite import Sprite

class Cross(Sprite):
    def __init__(self,ai_settings,screen,x,y):
        super().__init__()
        self.screen=screen
        self.x=x
        self.y=y
        self.ai_settings=ai_settings
        self.cross_size=ai_settings.cross_size
        self.color=ai_settings.cross_color
        self.width=ai_settings.cross_width
        self.image=game.Surface((self.cross_size,self.cross_size),game.SRCALPHA)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.draw_cross()
        
    def draw_cross(self):
        game.draw.line(self.image,self.color,(0,0),(self.cross_size,self.cross_size),self.width)
        game.draw.line(self.image,self.color,(self.cross_size,0),(0,self.cross_size),self.width)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)