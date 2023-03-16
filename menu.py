'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-19 20:04:04
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2023-03-16 10:48:16
FilePath: \\chrome-dinosaur\\menu.py
Description: Implement the main menu.
             实现游戏的主菜单。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''


import pygame
import sys

import game_launcher
import para


class Menu:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 初始化窗口、载入素材
        pygame.init()
        pygame.display.set_caption("dino")
        self.screen = pygame.display.set_mode(para.Para.RESOLUTION)

        f = pygame.font.Font("Assets\\consola.ttf", para.Para.SIZE_OF_TITLE)

        self.text = f.render("Press space to start", True,
                             (0, 0, 0), (255, 255, 255))

        self.dino = pygame.image.load(
            "Assets\\Dino\\DinoStart.png").convert_alpha()
        self.dino = pygame.transform.scale(self.dino, para.Para.SIZE_OF_DINO)

        # --------------------------------------------------------------------
        # 初始化rect
        self.textRect = self.text.get_rect()
        self.textRect.center = ((int)(para.Para.WIDTH*(1/2)),
                                (int)(para.Para.HEIGHT*(1/3)))

        self.rect = self.dino.get_rect()
        self.rect.bottomleft = ((int)(para.Para.WIDTH * (1/16)),
                                (int)(para.Para.HEIGHT * (6/9)))

        # --------------------------------------------------------------------
        # 是否重开游戏
        self.isReset = False

        # 菜单时钟
        self.clock = pygame.time.Clock()

        # 实例化游戏类
        self.game = game_launcher.GameLauncher()

    def menu(self):
        while True:
            # ----------------------------------------------------------------
            # 事件监测

            # 重开游戏
            if self.isReset:
                self.new()

            for event in pygame.event.get():
                # 关闭窗口
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Esc键返回（结束游戏）
                    if event.key == pygame.K_ESCAPE:
                        return
                    # SPACE、W、方向上键重开游戏
                    if event.key == pygame.K_SPACE\
                            or event.key == pygame.K_w\
                            or event.key == pygame.K_UP:
                        self.new()

            # ----------------------------------------------------------------
            # 画背景

            # 背景颜色
            self.screen.fill(para.Para.BACKGROUND_COLOR)

            # 写字、画初始恐龙
            self.screen.blit(self.text, self.textRect)
            self.screen.blit(self.dino, self.rect)

            # ----------------------------------------------------------------
            # 更新窗口、设置帧率
            pygame.display.update()
            self.clock.tick(para.Para.FPS)

    # 运行新游戏
    def new(self):
        self.game.launch()
        self.isReset = self.game.gameOver()

        # 重新实例化，为重新开始做准备
        self.game = game_launcher.GameLauncher()
