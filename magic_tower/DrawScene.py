import pygame
from Status_bar_and_boundary import blit
def drawscene(hero,screen):
    top = 50
    for i in  hero.info_floor:
        left = 300
        for j in i:
            if type(j) == int:
                if j == 0:
                    image = pygame.image.load('resouce/地形/ground.png')
                    image = pygame.transform.scale(image,(50,50))
                    blit(image,left,top,screen)
                elif j == 1:
                    image = pygame.image.load('resouce/地形/wall.png')
                    image = pygame.transform.scale(image,(50,50))
                    blit(image,left,top,screen)
                elif j == 2:
                    image = pygame.image.load('resouce/地形/star 0.png')
                    image = pygame.transform.scale(image,(50,50))
                    blit(image,left,top,screen)
                elif j == 3:
                    image = pygame.image.load('resouce/地形/lava 0.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
            else:
                image = pygame.image.load('resouce/地形/ground.png')
                image = pygame.transform.scale(image, (50, 50))
                blit(image, left, top, screen)
                if j['o_type'] == '上楼梯':
                    image = pygame.image.load('resouce/地形/上楼梯.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == '下楼梯':
                    image = pygame.image.load('resouce/地形/下楼梯.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == 'NPC':
                    image = pygame.image.load('resouce/NPC/'+j['name']+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "钥匙":
                    image = pygame.image.load('resouce/道具/'+j['color']+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "monster":
                    image = pygame.image.load('resouce/怪物/'+j['name']+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "宝物":
                    image = pygame.image.load('resouce/道具/'+j['name']+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "door":
                    image = pygame.image.load('resouce/地形/门/'+j['color']+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "栅栏":
                    image = pygame.image.load('resouce/地形/门/栅栏.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
                elif j['o_type'] == "商店":
                    image = pygame.image.load('resouce/素材/商店'+str(j['flag'])+'.png')
                    image = pygame.transform.scale(image, (50, 50))
                    blit(image, left, top, screen)
            left += 50
        top += 50