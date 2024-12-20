import pygame as game
from pygame.sprite import Sprite
class Boxes(Sprite):
    def __init__(self,screen,ai_settings):
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.screen_rect=self.screen.get_rect()
        self.line_color=ai_settings.line_color
        self.rect=game.Rect(0,0,2,200)
        self.rect2=game.Rect(0,0,2,200)
        self.rect.centerx=self.screen_rect.centerx-35
        self.rect.bottom=self.screen_rect.bottom-50
        self.rect2.centerx=self.screen_rect.centerx+35
        self.rect2.bottom=self.screen_rect.bottom-50
        
        self.horizontal_rect1=game.Rect(0,0,200,2)
        self.horizontal_rect2=game.Rect(0,0,200,2)
        self.horizontal_rect1.right=self.screen_rect.right-50
        self.horizontal_rect1.centery=self.screen_rect.centery-35
        self.horizontal_rect2.right=self.screen_rect.right-50
        self.horizontal_rect2.centery=self.screen_rect.centery+35
        
        
        self.boxcolor=(0,255,0)
        self.boxwidth=58
        self.boxheight=58
        self.boxrect1=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect1.centerx=self.rect.centerx-35
        self.boxrect1.centery=80
        self.boxrect2=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect2.centerx=self.rect.centerx+35
        self.boxrect2.centery=self.boxrect1.centery
        self.boxrect3=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect3.centerx=self.boxrect2.centerx+70
        self.boxrect3.centery=self.boxrect2.centery
        
        self.boxrect4=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect4.centerx=self.boxrect1.centerx
        self.boxrect4.centery=148
        self.boxrect5=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect5.centerx=self.boxrect2.centerx
        self.boxrect5.centery=self.boxrect4.centery
        self.boxrect6=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect6.centerx=self.boxrect3.centerx
        self.boxrect6.centery=self.boxrect4.centery
        
        self.boxrect7=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect7.centerx=self.boxrect1.centerx
        self.boxrect7.centery=218
        self.boxrect8=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect8.centerx=self.boxrect2.centerx
        self.boxrect8.centery=self.boxrect7.centery
        self.boxrect9=game.Rect(0,0,self.boxwidth,self.boxheight)
        self.boxrect9.centerx=self.boxrect3.centerx
        self.boxrect9.centery=self.boxrect7.centery
        
        
        
          
    def draw_lines(self):
        game.draw.rect(self.screen,self.ai_settings.line_color,self.rect)
        game.draw.rect(self.screen,self.ai_settings.line_color,self.rect2)
        game.draw.rect(self.screen,self.ai_settings.line_color,self.horizontal_rect1)
        game.draw.rect(self.screen,self.ai_settings.line_color,self.horizontal_rect2)
        
    def draw_boxes(self):
        game.draw.rect(self.screen,self.boxcolor,self.boxrect1)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect2)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect3)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect4)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect5)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect6)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect7)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect8)
        game.draw.rect(self.screen,self.boxcolor,self.boxrect9)

        
        
        
        
        
        
