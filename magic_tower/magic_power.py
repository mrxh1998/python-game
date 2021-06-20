from Setting import settings
from Hero import *
import pygame
import game_function as gf
import json
from Status_bar_and_boundary import *
from DrawScene import drawscene
from time import sleep
# 初始化及设置
def rungame():
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("魔塔")
    pygame.mixer.music.load("resouce/BGM/bgm.mp3")
    pygame.mixer.music.set_volume(0.04)
    pygame.mixer.music.play(-1)
    Heros = hero(screen)
    while True:

        #gf.check_events(Heros)
        screen.fill((230, 230, 230))
        status_bar_and_boundary(Heros,screen)
        drawscene(Heros,screen)
        Heros.blitme()
        gf.check_events(Heros)
        pygame.display.flip()
rungame()
