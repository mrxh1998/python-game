import pygame
import pygame.font
def status_bar_and_boundary(hero,screen):
    #边框
    image = pygame.image.load('resouce/地形/wall 3.png')
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect()
    rect.left = -50
    rect.top = 0
    for i in range(0,18):
        rect.left += 50
        screen.blit(image,rect)
    for i in range(0,12):
        rect.top += 50
        screen.blit(image,rect)
    for i in range(0,18):
        screen.blit(image,rect)
        rect.left -= 50
    rect.left += 50
    for i in range(0,11):
        rect.top -= 50
        screen.blit(image,rect)
    rect.left = 250
    rect.top = 0
    for i in range(0,18):
        screen.blit(image,rect)
        rect.top += 50
    rect.left = 50
    rect.top = 550
    for i in range(0,4):
        for j in range(0,2):
            screen.blit(image,rect)
            rect.top += 50
        rect.top = 550
        rect.left += 50
    #状态栏
    image = pygame.image.load('resouce/地形/ground.png')
    image = pygame.transform.scale(image, (50, 50))
    rect = image.get_rect()
    rect.left = 50
    rect.top = 50
    for i in range(0,4):
        rect.top = 50
        for j in range(0,10):
            screen.blit(image,rect)
            rect.top += 50
        rect.left += 50
    #人物信息
    wordcolor = (230,230,230)
    image = pygame.image.load('resouce/勇者/Down 0.png')
    image = pygame.transform.scale(image, (60, 60))
    blit(image,60,60,screen)
    image = pygame.image.load('resouce/道具/y_key.png')
    image = pygame.transform.scale(image, (50, 50))
    blit(image,60,300,screen)
    image = pygame.image.load('resouce/道具/b_key.png')
    image = pygame.transform.scale(image, (50, 50))
    blit(image,60,360,screen)
    image = pygame.image.load('resouce/道具/r_key.png')
    image = pygame.transform.scale(image, (50, 50))
    blit(image,60,420,screen)

    font = pygame.font.SysFont(None,36)
    msg_image = font.render('Lv:  '+str(hero.level),True,wordcolor)
    blit(msg_image,130,100,screen)
    msg_image = font.render('HP:   ' + str(hero.HP), True, wordcolor)
    blit(msg_image,60,135,screen)
    msg_image = font.render('ATK: '+str(hero.attack),True,wordcolor)
    blit(msg_image,60,170,screen)
    msg_image = font.render('DEF: '+str(hero.defence),True,wordcolor)
    blit(msg_image,60,205,screen)
    msg_image = font.render('GOLD: '+str(hero.gold),True,wordcolor)
    blit(msg_image,60,240,screen)
    msg_image = font.render('EXP: '+str(hero.exp),True,wordcolor)
    blit(msg_image,60,275,screen)
    font = pygame.font.SysFont(None, 55)
    msg_image = font.render(str(hero.y_key),True,wordcolor)
    blit(msg_image,160,310,screen)
    msg_image = font.render(str(hero.b_key),True,wordcolor)
    blit(msg_image,160,370,screen)
    msg_image = font.render(str(hero.r_key),True,wordcolor)
    blit(msg_image,160,430,screen)
    font = pygame.font.SysFont("SimHei", 40)
    if hero.floor != 0 and hero.floor != 22:
        msg_image = font.render(str(hero.floor)+'F', True, wordcolor)
        blit(msg_image, 110, 490, hero.screen)
    elif hero.floor == 0:
        msg_image = font.render('序章', True, wordcolor)
        blit(msg_image, 110, 490, hero.screen)
    elif hero.floor == 22:
        msg_image = font.render('魔塔最深处', True, wordcolor)
        blit(msg_image, 50, 490, hero.screen)

def blit(image,left,top,screen):
    image_rect = image.get_rect()
    image_rect.left = left
    image_rect.top = top
    screen.blit(image,image_rect)


