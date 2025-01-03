import pygame.font
import time
class Button:
    def __init__(self,screen,msg):
        self.screen=screen
        self.width,self.height=200,50
        
        self.screen_rect=self.screen.get_rect()
        self.button_color=(0,0,255)
        self.text_color=(0,0,0)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.prep_msg(msg)
        self.button_visible=True
        
    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        if self.button_visible:
            self.screen.fill(self.button_color,self.rect)
            self.screen.blit(self.msg_image,self.msg_image_rect)
        