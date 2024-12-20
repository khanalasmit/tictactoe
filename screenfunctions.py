import pygame as game
import sys
from drawcircle import Circles
from drawcross import Cross
from drawbutton import Button
import time
def check_events(screen,ai_settings,box,circles,crosses,stat):
    for event in game.event.get():
        if event.type == game.QUIT:
            sys.exit()
        if event.type ==game.MOUSEBUTTONDOWN:
            x,y=game.mouse.get_pos()
            addsign(x,y,screen,ai_settings,box,circles,crosses,stat)
            
            
            
def update_screen(screen,ai_settings,box,circles,crosses,stat):
    screen.fill(ai_settings.bg_color)
    if not stat.game_active:
        box.draw_lines()
        box.draw_boxes()
        for circel in circles:
            circel.blitme()
        for cross in crosses:
            cross.blitme()
        if stat.gameover():
            if stat.winner()==1:
                button=Button(screen,"Side A won")
                button.button_visible=True
                button.draw_button()
                circles.empty()
                crosses.empty()
                game.display.flip()
                time.sleep(2)
                stat.board=["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                button.button_visible=False
                
            elif stat.winner() ==-1:
                button=Button(screen,"Side B won")
                button.button_visible=True
                button.draw_button()
                crosses.empty()
                circles.empty()
                game.display.flip()
                time.sleep(2)
                stat.board=["-", "-", "-", "-", "-", "-", "-", "-", "-"]
                button.button_visible=False
                
            
    game.display.flip()
    
    
def addsign(x,y,screen,ai_settings,box,circles,crosses,stat):
    box_clicked1=box.boxrect1.collidepoint(x,y)
    if box_clicked1:
        a=box.boxrect1.centerx
        b=box.boxrect1.centery
        if stat.signstat==1 and stat.board[0]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(0)
            stat.board[0]='O'
        elif stat.signstat==-1 and stat.board[0]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(0)
            stat.board[0]='X'
    box_clicked2=box.boxrect2.collidepoint(x,y)
    if box_clicked2:
        a=box.boxrect2.centerx
        b=box.boxrect2.centery
        if stat.signstat==1 and stat.board[1]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(1)
            stat.board[1]='O'
        elif stat.signstat==-1 and stat.board[1]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(1)
            stat.board[1]='X'
        
    box_clicked3=box.boxrect3.collidepoint(x,y)
    if box_clicked3:
        a=box.boxrect3.centerx
        b=box.boxrect3.centery
        if stat.signstat==1 and stat.board[2]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(2)
            stat.board[2]='O'
        elif stat.signstat==-1 and stat.board[2]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(2)
            stat.board[2]='X'
    box_clicked4=box.boxrect4.collidepoint(x,y)
    if box_clicked4:
        a=box.boxrect4.centerx
        b=box.boxrect4.centery
        if stat.signstat==1 and stat.board[3]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(3)
            stat.board[3]='O'
        elif stat.signstat==-1 and stat.board[3]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(3)
            stat.board[3]='X'
        
    box_clicked5=box.boxrect5.collidepoint(x,y)
    if box_clicked5:
        a=box.boxrect5.centerx
        b=box.boxrect5.centery
        if stat.signstat==1 and stat.board[4]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(4)
            stat.board[4]='O'
        elif stat.signstat==-1 and stat.board[4]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(4)
            stat.board[4]='X'
        
    box_clicked6=box.boxrect6.collidepoint(x,y)
    if box_clicked6:
        a=box.boxrect6.centerx
        b=box.boxrect6.centery
        if stat.signstat==1 and stat.board[5]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(5)
            stat.board[5]='O'
        elif stat.signstat==-1 and stat.board[5]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(5)
            stat.board[5]='X'
        
    box_clicked7=box.boxrect7.collidepoint(x,y)
    if box_clicked7:
        a=box.boxrect7.centerx
        b=box.boxrect7.centery
        if stat.signstat==1 and stat.board[6]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(6)
            stat.board[6]='O'
        elif stat.signstat==-1 and stat.board[6]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(6)
            stat.board[6]='X'
        
    box_clicked8=box.boxrect8.collidepoint(x,y)
    if box_clicked8:
        a=box.boxrect8.centerx
        b=box.boxrect8.centery
        if stat.signstat==1 and stat.board[7]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(7)
            stat.board[7]='O'
        elif stat.signstat==-1 and stat.board[7]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(7)
            stat.board[7]='X'
        
    box_clicked9=box.boxrect9.collidepoint(x,y)
    if box_clicked9:
        a=box.boxrect9.centerx
        b=box.boxrect9.centery
        if stat.signstat==1 and stat.board[8]=='-':
            sign=Circles(ai_settings,screen,a,b)
            circles.add(sign)
            stat.signstat *=-1
            stat.sideA.append(8)
            stat.board[8]='O'
        elif stat.signstat==-1 and stat.board[8]=='-':
            cross=Cross(ai_settings,screen,a,b)
            crosses.add(cross)
            stat.signstat *=-1
            stat.sideB.append(8)
            stat.board[8]='X'
    