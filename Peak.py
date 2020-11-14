import sys
import pygame

pygame.init()
from pygame import mixer

# size of the playing screen
screen_width = 1000
screen_height = 1500
screen = pygame.display.set_mode((screen_width, screen_height))

# Player sprites:





Playerleft = pygame.image.load('Balloon.png')
Playerright = pygame.image.load('Playerright.png')
Playerleft_rect = Playerleft.get_rect()
Playerright_rect = Playerright.get_rect()

# Background
bg = pygame.image.load('Background.jpg')

# color of playing screen
blue = 0, 0, 205

# position of the sprite
x = 500
y = 500

# size of the player
width = 64
height = 64

# speed of player
vel = 33

# Enemy Sprite
Enemy = pygame.image.load("Enemy.png")
Enemy_rect = Enemy.get_rect()

# Enemy speed
speed = [20, 20]

# player's abilities to jump variables
Is_jump = False
jumpCount = 10

# Drawing and animations
screen.fill(blue)
screen.blit(Playerleft, Playerleft_rect)
screen.blit(Playerright, Playerright_rect)

# Time frames
clock = pygame.time.Clock()

# Timer
font = pygame.font.Font(None, 54)
font_color = pygame.Color('springgreen')
passed_time = 0
timer_started = False
done = False

# Starting screen
over_font = pygame.font.Font('freesansbold.ttf', 100)


def menutext():
    overtext = over_font.render("Fast Food Fury", True, (255, 255, 0))
    screen.blit(overtext, (305, 105))
    overtext = over_font.render("Fast Food Fury", True, (255, 0, 0))
    screen.blit(overtext, (300, 100))
    text = font.render("To Start, double tap F", True, (255, 255, 0))
    screen.blit(text, (453, 203))
    text = font.render("To Start, double tap F", True, (255, 0, 0))
    screen.blit(text, (450, 200))
    text = font.render("SPACE = Jump   Arrow Keys = Move", True, (255, 255, 0))
    screen.blit(text, (323, 303))
    text = font.render("SPACE = Jump   Arrow Keys = Move", True, (255, 0, 0))
    screen.blit(text, (320, 300))




























































































