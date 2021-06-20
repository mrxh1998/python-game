import sys
import pygame
from time import sleep
import json
from Status_bar_and_boundary import blit
from Program import *
def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            Kdown(hero,event)
        elif event.type == pygame.KEYUP:
            KUP(hero)
def Kdown(hero,event):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
        hero.update()
    if event.key == pygame.K_LEFT:
        hero.moving_left = True
        hero.update()
    if event.key == pygame.K_UP:
        hero.moving_up = True
        hero.update()
    if event.key == pygame.K_DOWN:
        hero.moving_down = True
        hero.update()
def KUP(hero):
    hero.moving_right = False
    hero.moving_left = False
    hero.moving_down = False
    hero.moving_up = False
def check_map(hero):
    x = int((hero.rect.top - 50)/50)
    y = int((hero.rect.left - 300)/50)
    if hero.info_floor[x][y] == 0:
        return True
    elif type(hero.info_floor[x][y]) == dict:
        if hero.info_floor[x][y]['o_type'] == '上楼梯':
            hero.floor = hero.info_floor[x][y]['goto']
            hero_location_update(hero,hero.info_floor[x][y]['location'][0],hero.info_floor[x][y]['location'][1])
            sound = pygame.mixer.Sound('resouce/音效/open_door.ogg')
            sound.play()
        elif hero.info_floor[x][y]['o_type'] == '下楼梯':
            hero.floor = hero.info_floor[x][y]['goto']
            hero_location_update(hero, hero.info_floor[x][y]['location'][0], hero.info_floor[x][y]['location'][1])
            sound = pygame.mixer.Sound('resouce/音效/open_door.ogg')
            sound.play()
        elif hero.info_floor[x][y]['o_type'] == 'door':
            check_door(hero,x,y)
            return False
        elif hero.info_floor[x][y]['o_type'] == '商店':
            shop(hero,x,y)
            return False
        elif hero.info_floor[x][y]['o_type'] == '钥匙':
            upadate_key(hero,x,y)
            return False
        elif hero.info_floor[x][y]['o_type'] == '宝物':
            check_treasure(hero,x,y)
            return False
        elif  hero.info_floor[x][y]['o_type'] == 'monster':
            check_monster(hero,x,y)
            return False
        elif hero.info_floor[x][y]['o_type'] == '栅栏':
            if hero.info_floor[x][y]["flag"]:
                hero.info_floor[x][y] = 0
                hero.floors["floors"][hero.floor]['scene'][x][y] = 0
                sound = pygame.mixer.Sound('resouce/音效/close_door.ogg')
                sound.play()
            return False
        elif hero.info_floor[x][y]['o_type'] == 'NPC':
            check_NPC(hero,x,y)
            return False
    elif hero.info_floor[x][y] != 0:
        return False

def hero_location_update(hero,x,y):
    hero.rect.left = x * 50
    hero.rect.top = y * 50
    hero.info_floor = hero.floors['floors'][hero.floor]['scene']
def check_door(hero,x,y):
    flag = 0
    if hero.info_floor[x][y]['color'] == 'yellow' and hero.y_key != 0:
        hero.y_key -= 1
        flag = 1
    elif hero.info_floor[x][y]['color'] == 'blue' and hero.b_key != 0:
        hero.b_key -= 1
        flag = 1
    elif hero.info_floor[x][y]['color'] == 'red' and hero.r_key != 0:
        hero.r_key -= 1
        flag = 1
    if flag:
        hero.info_floor[x][y] = 0
        hero.floors["floors"][hero.floor]['scene'][x][y] = 0
        sound = pygame.mixer.Sound('resouce/音效/open_door.ogg')
        sound.play()
def upadate_key(hero,x,y):
    if hero.info_floor[x][y]['color'] == "y_key":
        hero.y_key+=1
        play_bgm_word("error","黄钥匙",hero.screen)
    elif hero.info_floor[x][y]['color'] == "b_key":
        hero.b_key+=1
        play_bgm_word("error", "蓝钥匙", hero.screen)
    elif hero.info_floor[x][y]['color'] == "r_key":
        hero.r_key += 1
        play_bgm_word("error", "红钥匙", hero.screen)
    elif hero.info_floor[x][y]['color'] == "special":
        hero.y_key+=1
        hero.b_key += 1
        hero.r_key += 1
        play_bgm_word("error", "特殊钥匙", hero.screen)
    hero.info_floor[x][y] = 0
    hero.floors["floors"][hero.floor]['scene'][x][y] = 0
def check_treasure(hero,x,y):
    if hero.info_floor[x][y]['name'] == "红宝石":
        hero.attack += 3
        play_bgm_word("error",hero.info_floor[x][y]['name'],hero.screen)
    elif hero.info_floor[x][y]['name'] == "蓝宝石":
        hero.defence += 3
        play_bgm_word("error", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "金块":
        hero.gold += 300
        play_bgm_word("error", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "红药":
        hero.HP += 200
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "蓝药":
        hero.HP += 500
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "圣水":
        hero.HP *= 2
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "怪物数值书":
        hero.book = 1
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "铁剑":
        hero.attack += 10
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "青锋剑":
        hero.attack += 70
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "星光神剑":
        hero.attack += 150
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "黄金盾":
        hero.defence += 85
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "星光神盾":
        hero.defence += 150
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "小飞羽":
        hero.attack += 7
        hero.level += 1
        hero.defence += 7
        hero.HP += 1000
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "大飞羽":
        hero.attack += 21
        hero.level += 3
        hero.defence += 21
        hero.HP += 3000
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "铁盾":
        hero.defence += 10
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "十字架":
        hero.crucifix = 1
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "锄头":
        hero.CT = 1
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    elif hero.info_floor[x][y]['name'] == "神秘轮盘":
        hero.LP = 1
        play_bgm_word("get", hero.info_floor[x][y]['name'], hero.screen)
    hero.info_floor[x][y] = 0
    hero.floors["floors"][hero.floor]['scene'][x][y] = 0
def check_monster(hero,x,y):
    monstername = hero.info_floor[x][y]['name']
    monster_id = hero.monster_id[monstername]
    monster = hero.monsters['monster'][monster_id]
    monster_HP = monster['hp']
    hero_HP = hero.HP
    if hero.attack <= monster['dfs']:
        return
    if monster['skill'] == 1:
        hero_HP -= int(hero_HP*monster['damage'])
    elif monster['skill'] == 2:
        hero_HP -= monster['damage']
    while monster_HP > 0:
        if hero.attack > monster['dfs']:
            monster_HP -= hero.attack - monster['dfs']
        if monster['atk'] > hero.defence:
            hero_HP -= monster['atk'] - hero.defence
    if hero_HP < 0:
        sound = pygame.mixer.Sound('resouce/音效/error.ogg')
        sound.play()
        return
    else :
        if monster['skill']:
            sound = pygame.mixer.Sound('resouce/音效/magic.ogg')
            sound.play()
        hero.HP = hero_HP
        hero.exp += monster['exp']
        hero.gold += monster['money']
        play_bgm_word("error", (monster['money'], monster['exp']), hero.screen)
    if monster['name'] == '冥灵魔王1':
        hero.info_floor[x][y] = {"o_type":"NPC","name":"冥灵魔王","status":"defeat1"}
    elif monster['name'] == '冥灵魔王2':
        hero.info_floor[x][y] = {"o_type": "NPC", "name": "冥灵魔王", "status": "defeat2"}
    elif monster['name'] == '魔龙弱':
        hero.info_floor[x][y] = {"o_type": "NPC", "name": "魔龙弱"}
    else:
        hero.info_floor[x][y] = 0
        hero.floors["floors"][hero.floor]['scene'][x][y] = 0

def check_NPC(hero,x,y):
    if hero.info_floor[x][y]['name'] == '仙女':
       XN_program(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '蓝袍老人':
        blue_old_man(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '红袍老人':
        red_old_man(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '小偷':
        thief(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '公主':
        princess(hero, x, y)
    elif hero.info_floor[x][y]['name'] == '冥灵魔王':
        devil(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '魔法阵':
        magic(hero,x,y)
    elif hero.info_floor[x][y]['name'] == '魔龙弱':
        dragon(hero,x,y)
def play_bgm_word(path,treasure,screen):
    wordcolor = (230, 230, 230)
    sound = pygame.mixer.Sound('resouce/音效/'+path+'.ogg')
    sound.play()
    font = pygame.font.SysFont("SimHei",36)
    if treasure == "红宝石":
        msg_image = font.render("获得红宝石，攻击力加3",True,wordcolor,"Black")
    elif treasure == "蓝宝石":
        msg_image = font.render("获得蓝宝石，防御力加3", True, wordcolor, "Black")
    elif treasure == "圣水":
        msg_image = font.render("获得圣水，生命值翻倍", True, wordcolor, "Black")
    elif treasure == "金块":
        msg_image = font.render("获得金块，金币加300", True, wordcolor, "Black")
    elif treasure == "红药":
        msg_image = font.render("获得红药，生命值加200", True, wordcolor, "Black")
    elif treasure == "蓝药":
        msg_image = font.render("获得蓝药，生命值加500", True, wordcolor, "Black")
    elif treasure == "铁剑":
        msg_image = font.render("获得铁剑，攻击力加10", True, wordcolor, "Black")
    elif treasure == "青锋剑":
        msg_image = font.render("获得青锋剑，攻击力加70", True, wordcolor, "Black")
    elif treasure == "星光神剑":
        msg_image = font.render("获得星光神剑，攻击力加150", True, wordcolor, "Black")
    elif treasure == "黄金盾":
        msg_image = font.render("获得黄金盾，防御力加85", True, wordcolor, "Black")
    elif treasure == "星光神盾":
        msg_image = font.render("获得星光神盾，防御力加150", True, wordcolor, "Black")
    elif treasure == "铁盾":
        msg_image = font.render("获得铁盾，防御力加10", True, wordcolor, "Black")
    elif treasure == "黄钥匙":
        msg_image = font.render("获得黄钥匙", True, wordcolor, "Black")
    elif treasure == "蓝钥匙":
        msg_image = font.render("获得蓝钥匙", True, wordcolor, "Black")
    elif treasure == "红钥匙":
        msg_image = font.render("获得红钥匙", True, wordcolor, "Black")
    elif treasure == "特殊钥匙":
        msg_image = font.render("获得钥匙盒，所有钥匙加一", True, wordcolor, "Black")
    elif treasure == "怪物数值书":
        msg_image = font.render("获得怪物数值书，按L可查看", True, wordcolor, "Black")
    elif treasure == "小飞羽":
        msg_image = font.render("获得小飞羽，提升1级", True, wordcolor, "Black")
    elif treasure == "大飞羽":
        msg_image = font.render("获得大飞羽，提升3级", True, wordcolor, "Black")
    elif treasure == "锄头":
        msg_image = font.render("获得小偷的锄头", True, wordcolor, "Black")
    elif treasure == "十字架":
        msg_image = font.render("获得十字架", True, wordcolor, "Black")
        blit(msg_image,400,300,screen)
        pygame.display.flip()
        sleep(1)
        return
    elif treasure == "神秘轮盘":
        msg_image = font.render("获得神秘轮盘，按J可飞跃楼层", True, wordcolor, "Black")
        blit(msg_image, 400, 300, screen)
        pygame.display.flip()
        sleep(1)
        return
    elif type(treasure) == tuple:
        msg_image = font.render("获得"+str(treasure[0])+'金币,获得'+str(treasure[1])+'经验', True, wordcolor, "Black")
    blit(msg_image,400,300,screen)
    pygame.display.flip()
    sleep(0.1)