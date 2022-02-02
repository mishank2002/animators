from random import randint
from termios import VEOL
from xml.etree.ElementTree import C14NWriterTarget
import pygame

pygame.init()
game_window=pygame.display.set_mode((900,600))

class car:

    car_image=pygame.image.load("car.png")
    car_image=pygame.transform.smoothscale(car_image,(50,70)).convert_alpha()
    car_image=pygame.transform.rotate(car_image,270)

    car_x=-20
    car_y=randint(100,340)      


