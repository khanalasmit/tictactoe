import pygame as game
from pygame.sprite import Sprite
from settings import Settings
import screenfunctions as sf
from boxes import Boxes
from pygame.sprite import Group
from gamestats import Stats
def run_game():
    game.init() 
    ai_settings=Settings()
    screen=game.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    box=Boxes(screen,ai_settings)
    stat=Stats(screen)
    circles=Group()
    crosses=Group()
    while True:
        sf.check_events(screen,ai_settings,box,circles,crosses,stat)
        sf.update_screen(screen,ai_settings,box,circles,crosses,stat)
        
run_game()