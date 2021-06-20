from time import sleep
import pygame
import sys
from Status_bar_and_boundary import blit
from Status_bar_and_boundary import status_bar_and_boundary
from DrawScene import  drawscene
def XN_program(hero,x,y):
    if hero.XNfirst == 0:
        XN_program1(hero,x,y)
    elif hero.crucifix == 0:
        XN_program2(hero,x,y)
    else:
        XN_program3(hero,x,y)
def XN_program1(hero,x,y):
    for i in range(0,9):
        image = pygame.image.load("resouce/对话/仙女1"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = 0
    hero.info_floor[x][y-1] = {"o_type":"NPC","name":"仙女"}
    hero.floors['floors'][hero.floor]['scene'][x][y] = 0
    hero.floors['floors'][hero.floor]['scene'][x][y-1] = {"o_type":"NPC","name":"仙女"}
    hero.XNfirst = 1
def XN_program2(hero,x,y):
    image = pygame.image.load("resouce/对话/仙女20.png")
    image = pygame.transform.scale(image, (400, 100))
    blit(image, 400, 300, hero.screen)
    pygame.display.flip()
    sleep(1)
def XN_program3(hero,x,y):
    for i in range(0,2):
        image = pygame.image.load("resouce/对话/仙女3"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
    sound.play()
    hero.HP *= 4/3
    hero.HP = int(hero.HP)
    hero.attack *= 4/3
    hero.attack = int(hero.attack)
    hero.defence *= 4/3
    hero.defence = int(hero.defence)
    hero.info_floor[x][y] = 0
    hero.floors['floors'][hero.floor]['scene'][x][y] = 0
def blue_old_man(hero,x,y):
    if hero.info_floor[x][y]['id'] == 1:
        blue_old_man1(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 2:
        blue_old_man2(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 3:
        blue_old_man3(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 4:
        blue_old_man4(hero,x,y)
def blue_old_man1(hero,x,y):
    for i in range(0,3):
        image = pygame.image.load("resouce/对话/蓝袍老人1"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    sound = pygame.mixer.Sound('resouce/音效/get.ogg')
    sound.play()
    wordcolor = (230, 230, 230)
    font = pygame.font.SysFont("SimHei", 36)
    msg_image = font.render("获得钢剑，攻击力加30", True, wordcolor, "Black")
    blit(msg_image, 400, 300, hero.screen)
    pygame.display.flip()
    sleep(1)
    hero.info_floor[x][y] = 0
    hero.floors['floors'][hero.floor]['scene'][x][y] = 0
    hero.attack += 30
def blue_old_man2(hero,x,y):
    i = 0
    image = pygame.image.load("resouce/对话/蓝袍老人20.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 3:
                    i += 1
                    image = pygame.image.load("resouce/对话/蓝袍老人2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 0:
                    i -= 1
                    image = pygame.image.load("resouce/对话/蓝袍老人2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 0 and hero.exp >=100:
                        hero.attack += 7
                        hero.level += 1
                        hero.defence += 7
                        hero.HP += 1000
                        hero.exp -= 100
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 1 and hero.exp >=30:
                        hero.attack += 5
                        hero.exp -= 30
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 2 and hero.exp >= 30:
                        hero.defence += 5
                        hero.exp -= 30
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 3:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()
def blue_old_man3(hero,x,y):
    i = 0
    image = pygame.image.load("resouce/对话/蓝袍老人30.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 3:
                    i += 1
                    image = pygame.image.load("resouce/对话/蓝袍老人3" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 0:
                    i -= 1
                    image = pygame.image.load("resouce/对话/蓝袍老人3" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 0 and hero.exp >=270:
                        hero.attack += 21
                        hero.level += 3
                        hero.defence += 21
                        hero.HP += 3000
                        hero.exp -= 270
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 1 and hero.exp >=95:
                        hero.attack += 17
                        hero.exp -= 95
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 2 and hero.exp >= 95:
                        hero.defence += 17
                        hero.exp -= 95
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 3:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()
def blue_old_man4(hero,x,y):
    for i in range(0,3):
        image = pygame.image.load("resouce/对话/蓝袍老人4"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    if hero.exp >= 500:
        image = pygame.image.load("resouce/对话/蓝袍老人43.png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
        hero.attack += 120
        hero.exp -= 500
        hero.SGJ = 1
        status_bar_and_boundary(hero, hero.screen)
        wordcolor = (230, 230, 230)
        font = pygame.font.SysFont("SimHei", 36)
        msg_image = font.render("获得圣光剑，攻击力加120", True, wordcolor, "Black")
        blit(msg_image, 400, 300, hero.screen)
        pygame.display.flip()
        sound = pygame.mixer.Sound('resouce/音效/get.ogg')
        sound.play()
        sleep(1)
        hero.info_floor[x][y] = 0
        hero.floors['floors'][hero.floor]['scene'][x][y] = 0
    else:
        for i in range(1, 3):
            image = pygame.image.load("resouce/对话/蓝袍老人44" + str(i) + ".png")
            image = pygame.transform.scale(image, (400, 100))
            blit(image, 400, 300, hero.screen)
            pygame.display.flip()
            sleep(1)
def red_old_man(hero,x,y):
    if hero.info_floor[x][y]['id'] == 1:
        red_old_man1(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 2:
        red_old_man2(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 3:
        red_old_man3(hero,x,y)
    elif hero.info_floor[x][y]['id'] == 4:
        red_old_man4(hero,x,y)
def red_old_man1(hero,x,y):
    for i in range(0,3):
        image = pygame.image.load("resouce/对话/红袍老人1"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    sound = pygame.mixer.Sound('resouce/音效/get.ogg')
    sound.play()
    wordcolor = (230, 230, 230)
    font = pygame.font.SysFont("SimHei", 36)
    msg_image = font.render("获得钢盾，攻击力加30", True, wordcolor, "Black")
    blit(msg_image, 400, 300, hero.screen)
    pygame.display.flip()
    sleep(1)
    hero.info_floor[x][y] = 0
    hero.floors['floors'][hero.floor]['scene'][x][y] = 0
    hero.defence += 30
def red_old_man2(hero,x,y):
    i = 0
    image = pygame.image.load("resouce/对话/红袍老人20.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 3:
                    i += 1
                    image = pygame.image.load("resouce/对话/红袍老人2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 0:
                    i -= 1
                    image = pygame.image.load("resouce/对话/红袍老人2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 0 and hero.gold >=10:
                        hero.y_key += 1
                        hero.gold -= 10
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 1 and hero.gold >=50:
                        hero.b_key += 1
                        hero.gold -= 50
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 2 and hero.gold >= 100:
                        hero.r_key += 1
                        hero.gold -= 100
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 3:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()
def red_old_man3(hero,x,y):
    i = 0
    image = pygame.image.load("resouce/对话/红袍老人30.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 3:
                    i += 1
                    image = pygame.image.load("resouce/对话/红袍老人3" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 0:
                    i -= 1
                    image = pygame.image.load("resouce/对话/红袍老人3" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 0 and hero.y_key:
                        hero.y_key -= 1
                        hero.gold += 7
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 1 and hero.b_key:
                        hero.b_key -= 1
                        hero.gold += 35
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 2 and hero.r_key :
                        hero.r_key -= 1
                        hero.gold += 70
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/gold.ogg')
                        sound.play()
                    elif i == 3:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()
def red_old_man4(hero,x,y):
    for i in range(0,3):
        image = pygame.image.load("resouce/对话/红袍老人4"+str(i)+".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
    if hero.gold >= 500:
        image = pygame.image.load("resouce/对话/红袍老人43.png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image,400,300,hero.screen)
        pygame.display.flip()
        sleep(1)
        hero.defence += 120
        hero.gold -= 500
        hero.SGD = 1
        status_bar_and_boundary(hero, hero.screen)
        wordcolor = (230, 230, 230)
        font = pygame.font.SysFont("SimHei", 36)
        msg_image = font.render("获得圣光盾，防御力加120", True, wordcolor, "Black")
        blit(msg_image, 400, 300, hero.screen)
        pygame.display.flip()
        sound = pygame.mixer.Sound('resouce/音效/get.ogg')
        sound.play()
        sleep(1)
        hero.info_floor[x][y] = 0
        hero.floors['floors'][hero.floor]['scene'][x][y] = 0
    else:
        for i in range(1, 3):
            image = pygame.image.load("resouce/对话/红袍老人44" + str(i) + ".png")
            image = pygame.transform.scale(image, (400, 100))
            blit(image, 400, 300, hero.screen)
            pygame.display.flip()
            sleep(1)
def shop(hero,x,y):
    if hero.info_floor[x][y]['name'] == '初级商店':
        first_shop(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '高级商店':
        first_shop2(hero,x,y)
def first_shop(hero,x,y):
    i = 1
    image = pygame.image.load("resouce/对话/商店11.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 4:
                    i += 1
                    image = pygame.image.load("resouce/对话/商店1" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 1:
                    i -= 1
                    image = pygame.image.load("resouce/对话/商店1" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 1 and hero.gold >=25:
                        hero.HP += 800
                        hero.gold -= 25
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 2 and hero.gold >= 25:
                        hero.attack += 4
                        hero.gold -= 25
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 3 and hero.gold >= 25:
                        hero.defence += 4
                        hero.gold -= 25
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i== 4:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()
def first_shop2(hero,x,y):
    i = 1
    image = pygame.image.load("resouce/对话/商店21.png")
    image = pygame.transform.scale(image, (400, 400))
    blit(image, 400, 200, hero.screen)
    pygame.display.flip()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and i != 4:
                    i += 1
                    image = pygame.image.load("resouce/对话/商店2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_UP and i != 1:
                    i -= 1
                    image = pygame.image.load("resouce/对话/商店2" + str(i) + ".png")
                    image = pygame.transform.scale(image, (400, 400))
                    blit(image, 400, 200, hero.screen)
                    pygame.display.flip()
                elif event.key == pygame.K_SPACE:
                    if i == 1 and hero.gold >=100:
                        hero.HP += 4000
                        hero.gold -= 100
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 2 and hero.gold >= 100:
                        hero.attack += 20
                        hero.gold -= 100
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i == 3 and hero.gold >= 100:
                        hero.defence += 20
                        hero.gold -= 100
                        status_bar_and_boundary(hero,hero.screen)
                        sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
                        sound.play()
                    elif i== 4:
                        return
            elif event.type == pygame.QUIT:
                sys.exit()

def thief(hero,x,y):
    if hero.thief_first == 0:
        thief1(hero,x,y)
        return
    elif hero.thief_first == 1:
        if hero.CT == 0:
            thief2(hero,x,y)
            return
        else:
            thief3(hero,x,y)
def thief1(hero,x,y):
    for i in range(0, 9):
        image = pygame.image.load("resouce/对话/小偷1" + str(i) + ".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = 0
    image = pygame.image.load("resouce/地形/ground.png")
    image = pygame.transform.scale(image,(50,50))
    blit(image,(y+6)*50,(x+1)*50,hero.screen)
    pygame.display.flip()
    sleep(1)
    sound = pygame.mixer.Sound('resouce/音效/open_door2.ogg')
    sound.play()
    hero.info_floor[x][y] = {"o_type":"NPC","name":"小偷"}
    image = pygame.image.load("resouce/NPC/小偷.png")
    image = pygame.transform.scale(image,(50,50))
    blit(image,(y+6)*50,(x+1)*50,hero.screen)
    pygame.display.flip()
    for i in range(9, 12):
        image = pygame.image.load("resouce/对话/小偷1" + str(i) + ".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.thief_first = 1
    hero.floors["floors"][2]['scene'][6][1] = 0
def thief2(hero,x,y):
    image = pygame.image.load("resouce/对话/小偷20.png")
    image = pygame.transform.scale(image, (400, 100))
    blit(image, 400, 300, hero.screen)
    pygame.display.flip()
    sleep(1)
def thief3(hero,x,y):
    image = pygame.image.load("resouce/对话/小偷30.png")
    image = pygame.transform.scale(image, (400, 100))
    blit(image, 400, 300, hero.screen)
    pygame.display.flip()
    sleep(1)
    hero.info_floor[x][y] = 0
    image = pygame.image.load("resouce/地形/ground.png")
    image = pygame.transform.scale(image, (50, 50))
    blit(image, (y + 6) * 50, (x + 1) * 50, hero.screen)
    pygame.display.flip()
    sleep(1)
    sound = pygame.mixer.Sound('resouce/音效/yes.ogg')
    sound.play()
    hero.info_floor[x][y] = {"o_type": "NPC", "name": "小偷"}
    image = pygame.image.load("resouce/NPC/小偷.png")
    image = pygame.transform.scale(image, (50, 50))
    blit(image, (y + 6) * 50, (x + 1) * 50, hero.screen)
    pygame.display.flip()
    for i in range(1,4):
        image = pygame.image.load("resouce/对话/小偷3" + str(i) + ".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = 0
    hero.floors['floors'][18]['scene'][8][5] = 0
    hero.floors['floors'][18]['scene'][9][5] = 0
    hero.floors['floors'][18]['scene'][10][10] = {"o_type":"上楼梯","goto":19, "location":[15,11]}
def princess(hero,x,y):
    if hero.info_floor[x][y]['status'] == "normal":
        for i in range(0, 7):
            image = pygame.image.load("resouce/对话/公主1" + str(i) + ".png")
            image = pygame.transform.scale(image, (400, 100))
            blit(image, 400, 300, hero.screen)
            pygame.display.flip()
            sleep(1)
        hero.info_floor[x][y]['status'] = 'donot_talk'
    elif hero.info_floor[x][y]['status'] == "evil":
        princess2(hero,x,y)
def princess2(hero,x,y):
    for i in range(0, 7):
        image = pygame.image.load("resouce/对话/公主2" + str(i) + ".png")
        image = pygame.transform.scale(image, (400, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    if hero.SGJ == 1 and hero.SGD == 1:
        hero.info_floor[x][y] = {"o_type":"monster","name":"魔龙弱"}
        hero.info_floor[x][y-1] = {"o_type": "monster", "name": "魔龙6"}
        hero.info_floor[x][y+1] = {"o_type": "monster", "name": "魔龙7"}
        hero.info_floor[x-1][y] = {"o_type": "monster", "name": "魔龙4"}
        hero.info_floor[x-1][y-1] = {"o_type": "monster", "name": "魔龙3"}
        hero.info_floor[x-1][y+1] = {"o_type": "monster", "name": "魔龙5"}
        hero.info_floor[x-2][y] = {"o_type": "monster", "name": "魔龙1"}
        hero.info_floor[x-2][y-1] = {"o_type": "monster", "name": "魔龙0"}
        hero.info_floor[x-2][y+1] = {"o_type": "monster", "name": "魔龙2"}
    else:
        bad_ending2(hero)
def devil(hero,x,y):
    if hero.info_floor[x][y]['status'] == 'normal':
        devil_1(hero,x,y)
    elif hero.info_floor[x][y]['status'] == 'defeat1':
        devil_2(hero,x,y)
    elif hero.info_floor[x][y]['status'] == 'rage':
        devil_3(hero,x,y)
    elif hero.info_floor[x][y]['status'] == 'defeat2':
        devil_4(hero,x,y)
def devil_1(hero,x,y):
    for i in range(0, 3):
        image = pygame.image.load("resouce/对话/魔王1" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = {"o_type":"monster","name":"冥灵魔王1"}
    hero.floors['floors'][hero.floor]['scene'][x][y] = {"o_type":"monster","name":"冥灵魔王1"}
def devil_2(hero,x,y):
    for i in range(0, 3):
        image = pygame.image.load("resouce/对话/魔王2" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = 0
    hero.floors['floors'][hero.floor]['scene'][x][y] = 0
def devil_3(hero,x,y):
    for i in range(0, 4):
        image = pygame.image.load("resouce/对话/魔王3" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.info_floor[x][y] = {"o_type":"monster","name":"冥灵魔王2"}
    hero.floors['floors'][hero.floor]['scene'][x][y] = {"o_type":"monster","name":"冥灵魔王2"}
def devil_4(hero, x, y):
    for i in range(0, 2):
        image = pygame.image.load("resouce/对话/魔王4" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    sleep(1)
    if hero.crucifix == 1:
        hero.info_floor[x][y] = {"o_type": "NPC", "name": "魔法阵"}
        hero.floors['floors'][hero.floor]['scene'][x][y] = {"o_type": "NPC", "name": "魔法阵"}
    else:
        bad_ending(hero)
def bad_ending(hero):
    #pygame.mixer.music.stop()
   # pygame.mixer.init()
   # pygame.mixer.music.load("resouce/BGM/badending.mp3")
   # pygame.mixer.music.set_volume(0.04)
   # pygame.mixer.music.play()

    for i in range(0, 3):
        image = pygame.image.load("resouce/对话/badending" + str(i) + ".png")
        image = pygame.transform.scale(image, (900, 650))
        blit(image, 0, 0, hero.screen)
        pygame.display.flip()
        sleep(5)
    sys.exit()
def bad_ending2(hero):
    image = pygame.image.load("resouce/对话/badending10.png")
    image = pygame.transform.scale(image, (900, 650))
    blit(image, 0, 0, hero.screen)
    pygame.display.flip()
    sleep(5)
    sys.exit()
def happyending(hero):
    for i in range(0, 4):
        image = pygame.image.load("resouce/对话/happyending" + str(i) + ".png")
        image = pygame.transform.scale(image, (900, 650))
        blit(image, 0, 0, hero.screen)
        pygame.display.flip()
        sleep(5)
    sys.exit()
def magic(hero,x,y):
    for i in range(0, 6):
        image = pygame.image.load("resouce/对话/魔法阵" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    hero.floor = 22
    hero.rect.left = 11 * 50
    hero.rect.top = 10 * 50
    hero.info_floor = hero.floors['floors'][hero.floor]['scene']
    sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
    sound.play()
def dragon(hero,x,y):
    for i in range(0, 5):
        image = pygame.image.load("resouce/对话/魔龙2" + str(i) + ".png")
        image = pygame.transform.scale(image, (500, 100))
        blit(image, 400, 300, hero.screen)
        pygame.display.flip()
        sleep(1)
    sleep(1)
    happyending(hero)

