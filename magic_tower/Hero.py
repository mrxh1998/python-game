import pygame
from game_function import check_map
import json
class hero():

    def __init__(self,screen):
        # 总体楼层信息
        self.floors = {}
        self.floors = json.load(open("data/floors_data.json", encoding="utf-8"))
        # 总体怪兽信息
        self.monsters = {}
        self.monsters = json.load(open("data/monsters_data.json",encoding="utf_8"))
        self.monster_id = {}
        self.monster_id = json.load(open("data/monster_id.json",encoding="utf_8"))
        self.screen = screen
        self.image = pygame.image.load('resouce/勇者/Down 0.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
       #self.rect = pygame.Rect(550,500,500,500)
        self.rect = self.image.get_rect()
        self.rect.left = self.floors["location"][0]*50
        self.rect.top = self.floors["location"][1]*50

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.attack =  10000 #基本信息
        self.defence = 10000
        self.HP = 1000
        self.gold = 500
        self.exp = 500
        self.y_key = 10
        self.b_key = 10
        self.r_key = 10
        self.level = 1
        self.floor = 20
        self.crucifix = 1
        self.SGJ = 1
        self.SGD = 1
        self.LP = 0
        self.book = 0
        self.CT = 0
        self.XNfirst = 0
        self.thief_first = 0
        #当前楼层信息
        self.info_floor = []
        self.info_floor = self.floors['floors'][self.floor]['scene']
        print(1)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            self.image = pygame.image.load('resouce/勇者/Right 0.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.left <= 750:
                self.rect.left += 50
                if check_map(self) == False:
                    self.rect.left -= 50
        if self.moving_left:
            self.image = pygame.image.load('resouce/勇者/Left 0.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.left >= 350:
                self.rect.left -= 50
                if check_map(self) == False:
                    self.rect.left += 50
        if self.moving_up:
            self.image = pygame.image.load('resouce/勇者/Up 0.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.top >= 100:
                self.rect.top -= 50
                if check_map(self) == False:
                    self.rect.top += 50
        if self.moving_down:
            self.image = pygame.image.load('resouce/勇者/Down 0.png')
            self.image = pygame.transform.scale(self.image, (50, 50))
            if self.rect.top <= 500:
                self.rect.top += 50
                if check_map(self) == False:
                    self.rect.top -= 50
