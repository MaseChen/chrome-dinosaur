'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 10:18:16
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2022-11-24 23:14:54
FilePath: \\dino\\maps.py
Description: Implement the background elements:
             Score, Track, game over icon and reset icon,
             with class Map to manage them.
             Class SetImage is a mathod shared by the classes.

            地图元素类。
            由类Map管理地图中的Score游戏分数、Track跑道、Game over、reset图标。
            类SetImage中有一个地图元素共用的类方法。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''

import pygame

import para


class Map:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 实例化分数类
        self.scorer = Score()

        # --------------------------------------------------------------------
        # 实例化跑道类
        self.track1 = Track()
        self.track2 = Track()
        # 将跑道2接在跑道1的前方
        self.track2.rect.left = self.track1.rect.right

        # --------------------------------------------------------------------
        # 实例化图标类
        self.gameOver = GameOver()
        self.reset = Reset()

    # 更新各个组件
    def update(self, speed):
        # 更新分数
        self.scorer.update()

        # 传入速度更新跑道
        self.track1.update(speed)
        self.track2.update(speed)

        # 将已超出屏幕外的跑道接在现跑道的前方
        if self.track1.rect.right <= 0:
            self.track1.rect.left = self.track2.rect.right

        if self.track2.rect.right <= 0:
            self.track2.rect.left = self.track1.rect.right


class Score:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 每局游戏开始时初始化分数
        self.score = 0

        # --------------------------------------------------------------------
        # 载入当前分数和最高分的文字
        self.f = pygame.font.Font(
            "Assets\\consola.ttf", para.Para.SIZE_OF_SCORE)

        self.text = self.f.render((str(self.score)).zfill(5),
                                  True, (0, 0, 0), (255, 255, 255))

        self.highestText = self.f.render("HI " +
                                         ((str((int)(para.Para.highestScore /
                                          para.Para.FPS*10))).zfill(5)),
                                         True, (0, 0, 0), (255, 255, 255))

        # --------------------------------------------------------------------
        # 初始化rect
        self.textRect = self.text.get_rect()
        self.textRect.topright = (para.Para.WIDTH, 0)

        self.highestTextRect = self.text.get_rect()
        self.highestTextRect.topright = ((int)(para.Para.WIDTH*0.85), 0)

    # 实时更新游戏分数及其对应的文字
    def update(self):
        self.score += 1
        self.text = self.f.render(
            (str((int)(self.score/para.Para.FPS*10)).zfill(5)),
            True, (0, 0, 0), (255, 255, 255))


class Track:
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 载入跑道图片
        self.image = pygame.image.load(
            "Assets\\Other\\Track.png").convert_alpha()

        # --------------------------------------------------------------------
        # 初始化rect
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, (int)(para.Para.HEIGHT * 0.63)

    # 更新跑道位置，实现相对运动
    def update(self, speed):
        assert self.rect is not None
        self.rect.left -= speed

# 背景云只是提了设想而并未实现，
# 原因之一是背景云不影响整个游戏的游玩，之二是还有好多deadline等我赶。
# class Cloud:
#     def __init__(self) -> None:
#         self.image = pygame.image.load(
#             "Assets\\Other\\Cloud.png").convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.center = ((int)(para.Para.WIDTH/2),
#                             (int)(para.Para.HEIGHT/2))


class SetImage:
    def __init__(self) -> None:
        pass

    # 更改图片本体、尺寸并取mask蒙版
    # 由于这个函数在游戏中运用得太广泛了，因此我把它封装成类了
    def setImage(self, image, SIZE):
        self.image = image
        self.image = pygame.transform.scale(
            self.image, SIZE)
        self.mask = pygame.mask.from_surface(self.image)


class GameOver(SetImage):
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 载入game over图标
        self.image = pygame.image.load(
            "Assets\\Other\\GameOver.png").convert_alpha()
        self.setImage(self.image, para.Para.SIZE_OF_GAME_OVER)

        # --------------------------------------------------------------------
        # 初始化rect
        self.rect = self.image.get_rect()
        self.rect.center = ((int)(para.Para.WIDTH*(1/2)),
                            (int)(para.Para.HEIGHT*(1/3)))
        super().__init__()

    def setImage(self, image, SIZE):
        return super().setImage(image, SIZE)


class Reset(SetImage):
    def __init__(self) -> None:
        # --------------------------------------------------------------------
        # 载入reset图标
        self.image = pygame.image.load(
            "Assets\\Other\\Reset.png").convert_alpha()
        self.setImage(self.image, para.Para.SIZE_OF_RESET)

        # --------------------------------------------------------------------
        # 初始化rect
        self.rect = self.image.get_rect()
        self.rect.center = ((int)(para.Para.WIDTH/2),
                            (int)(para.Para.HEIGHT/2))
        super().__init__()

    def setImage(self, image, SIZE):
        return super().setImage(image, SIZE)
