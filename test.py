'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 23:33:33
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2022-11-18 17:21:55
FilePath: \dino\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import para
import pygame
import obstacle
import sys

pygame.init()
screen = pygame.display.set_mode((1600, 900))
group = pygame.sprite.Group()
clock = pygame.time.Clock()


group.add(obstacle.LargeCactus())

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    group.draw(screen)
    group.update()

    # if group.empty():
    #     group.add(cactus.LargeCactus())

    pygame.display.update()
    clock.tick(120)
