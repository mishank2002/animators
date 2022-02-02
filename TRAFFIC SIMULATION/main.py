import pygame
from car_class import car
import random 
pygame.init()

c1=car()

game_window=pygame.display.set_mode((900,600))

background=pygame.image.load("background.jpg")
background=pygame.transform.scale(background,(900,400)).convert_alpha()
exit_game=False


font=pygame.font.SysFont(None,30)

i=0
clock=pygame.time.Clock()

def car_move():
    global exit_game
    global i
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
        game_window.fill([255,255,255])
        game_window.blit(background,(0,0))
        game_window.blit(c1.car_image,(c1.car_x,c1.car_y))
        c1.car_x+=2
        
        if i==1.200:
            print("H")

        game_window.blit(font.render("Time taken : "+str(int(i)),True,(255,221,122)),[200,0])
        clock.tick(60)
        pygame.display.update()
        i+=1/60
car_move()


