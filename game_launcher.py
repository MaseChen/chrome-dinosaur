'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-14 14:31:35
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2022-11-25 12:52:42
FilePath: \\dino\\game_launcher.py
Description: The main body of the game, implement the main logic.
             游戏的主类，跑主要逻辑。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''

import pygame
import sys
import random

import para
import dino
import obstacle
import maps


class GameLauncher:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 初始化窗口、载入素材
        pygame.init()
        pygame.display.set_caption("dino")
        self.screen = pygame.display.set_mode(para.Para.RESOLUTION)

        # --------------------------------------------------------------------
        # 实例化精灵列表和组件
        self.obstacleGroup = pygame.sprite.Group()

        self.background = maps.Map()
        self.dinosour = dino.Dinosaur()

        # --------------------------------------------------------------------
        # 初始速度
        self.speed = para.Para.SPEED_INIT

        # 游戏时钟
        self.clock = pygame.time.Clock()

    # 游戏运行函数
    def launch(self):
        while True:
            # ----------------------------------------------------------------
            # 事件监测

            # 恐龙死亡结束游戏
            if not self.dinosour.life:
                return

            for event in pygame.event.get():
                # 关闭窗口
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Esc键返回菜单
                    if event.key == pygame.K_ESCAPE:
                        return
                    # SPACE、W、方向上键跳跃
                    if event.key == pygame.K_SPACE\
                            or event.key == pygame.K_w\
                            or event.key == pygame.K_UP:
                        self.dinosour.jump()

                    # 按下S、方向下键下蹲
                    if event.key == pygame.K_s\
                            or event.key == pygame.K_DOWN:
                        self.dinosour.duck()

                if event.type == pygame.KEYUP:
                    # 松开S、方向下键起立
                    if event.key == pygame.K_s\
                            or event.key == pygame.K_DOWN:
                        self.dinosour.unduck()

            # ----------------------------------------------------------------
            # 画背景
            assert self.dinosour.image is not None\
                and self.dinosour.rect is not None

            # 背景颜色
            self.screen.fill(para.Para.BACKGROUND_COLOR)

            # 背景图片
            self.screen.blit(self.background.track1.image,
                             self.background.track1.rect)
            self.screen.blit(self.background.track2.image,
                             self.background.track2.rect)

            # 分数
            self.screen.blit(self.background.scorer.text,
                             self.background.scorer.textRect)

            # 如果不是首次游戏，显示最高分
            if para.Para.highestScore != 0:
                self.screen.blit(self.background.scorer.highestText,
                                 self.background.scorer.highestTextRect)

            # ----------------------------------------------------------------
            # 游戏的核心内容

            # 生成随机数量的障碍物
            self.randObstacleNum()

            # 画障碍物
            self.obstacleGroup.draw(self.screen)

            # 画恐龙
            self.screen.blit(self.dinosour.image, self.dinosour.rect)

            # 检测碰撞
            self.checkCollision()

            # 删除障碍物
            self.deleteObstacle()

            # ----------------------------------------------------------------
            # 更新组件的状态
            self.background.update(self.speed)
            self.obstacleGroup.update()
            self.dinosour.update()

            # 更新速度
            self.updateSpeed()

            # ----------------------------------------------------------------
            # 更新窗口、设置帧率
            pygame.display.update()
            self.clock.tick(para.Para.FPS)

    # 游戏结束界面函数
    def gameOver(self) -> bool:
        # 更新最高分
        self.updateHighestScore()

        # --------------------------------------------------------------------
        # 恐龙撞上障碍物死去时
        if not self.dinosour.life:
            while True:
                # ------------------------------------------------------------
                # 事件监测
                for event in pygame.event.get():
                    # 关闭窗口
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        # Esc键返回False
                        if event.key == pygame.K_ESCAPE:
                            return False

                        # SPACE、W、方向上键返回True
                        if event.key == pygame.K_SPACE\
                                or event.key == pygame.K_w\
                                or event.key == pygame.K_UP:
                            return True

                # ------------------------------------------------------------
                # 画背景
                assert self.dinosour.image and self.dinosour.rect is not None

                # 恐龙图片
                self.screen.blit(self.dinosour.image, self.dinosour.rect)

                # 背景颜色
                self.screen.blit(self.background.gameOver.image,
                                 self.background.gameOver.rect)
                self.screen.blit(self.background.reset.image,
                                 self.background.reset.rect)

                # ------------------------------------------------------------
                # 更新组件的状态
                self.background.update(self.speed)
                self.obstacleGroup.update()
                self.dinosour.update()

                # ------------------------------------------------------------
                # 更新窗口、设置帧率
                pygame.display.update()
                self.clock.tick(para.Para.FPS)

        # --------------------------------------------------------------------
        # 玩家手动返回菜单时
        else:
            return False

    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # 功能函数

    # 分数每上升100，恐龙速度增加1单位
    def updateSpeed(self):
        if (self.background.scorer.score/para.Para.FPS) % 10 == 0:
            self.speed += para.Para.SPEED_ADDER

    # 如果当前分数更高，则以当前分数覆盖历史最高分
    def updateHighestScore(self):
        if para.Para.highestScore < self.background.scorer.score:
            para.Para.highestScore = self.background.scorer.score

    # 通过规则随机确定下一批障碍物的数量
    def randObstacleNum(self):
        if len(self.obstacleGroup) < 2:

            self.randObstacleKind()
            if random.random() < 0.4:
                self.randObstacleKind()

    # 通过规则随机确定下一个障碍物的种类并实例化此障碍物
    def randObstacleKind(self):
        temp = random.random()

        if temp < para.Para.PROBABILITY_OF_BIRD:
            self.obstacleGroup.add(obstacle.Bird(self.speed))
        elif temp < 1-((1-para.Para.PROBABILITY_OF_BIRD)/2):
            self.obstacleGroup.add(obstacle.LargeCactus(self.speed))
        else:
            self.obstacleGroup.add(obstacle.SmallCactus(self.speed))

    # 删除已超出屏幕外的障碍物
    def deleteObstacle(self):
        for item in self.obstacleGroup.sprites():
            assert item.image is not None and item.rect is not None

            if -item.rect.x > item.rect.width:
                self.obstacleGroup.remove(item)

    # 若检测到恐龙与障碍物碰撞，则判定恐龙死亡
    def checkCollision(self):
        if pygame.sprite.spritecollideany(
                self.dinosour, self.obstacleGroup,
                pygame.sprite.collide_mask) is not None:  # type: ignore
            self.dinosour.life = False
