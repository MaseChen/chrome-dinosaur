'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 10:19:41
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2022-11-23 20:04:51
FilePath: \\dino\\dino.py
Description: Implement class Dinosaur,
             which includes states like run, jump, duck and die.

             恐龙类。
             实现dinosaur的run、jump、duck、die等状态。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''

import pygame

import para


class Dinosaur(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)

        # --------------------------------------------------------------------
        # 载入恐龙各种状态的图片
        self.imageRun1 = pygame.image.load(
            "Assets\\Dino\\DinoRun1.png").convert_alpha()
        self.imageRun2 = pygame.image.load(
            "Assets\\Dino\\DinoRun2.png").convert_alpha()
        self.imageJump = pygame.image.load(
            "Assets\\Dino\\DinoJump.png").convert_alpha()
        self.imageDuck1 = pygame.image.load(
            "Assets\\Dino\\DinoDuck1.png").convert_alpha()
        self.imageDuck2 = pygame.image.load(
            "Assets\\Dino\\DinoDuck2.png").convert_alpha()
        self.imageDead = pygame.image.load(
            "Assets\\Dino\\DinoDead.png").convert_alpha()

        self.setImage(self.imageRun1, para.Para.SIZE_OF_DINO)

        # --------------------------------------------------------------------
        # 初始化rect
        self.runningLeft = (int)(para.Para.WIDTH * (1/16))
        self.runningBottom = (int)(para.Para.HEIGHT * (6/9))
        self.runningRect = (self.runningLeft, self.runningBottom)

        self.duckingLeft = (int)(para.Para.HEIGHT*(1/16))
        self.duckingBottom = (int)(para.Para.HEIGHT*(13/18))
        self.duckingRect = (self.duckingLeft, self.duckingBottom)

        assert self.image is not None
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.runningRect

        # --------------------------------------------------------------------
        # 恐龙生命状态
        self.life = True

        # 状态指示器
        self.isRunning = True
        self.isJumping = False
        self.isDucking = False

        # 状态计时器
        self.runTimer = 0
        self.jumpTimer = 0
        self.duckTimer = 0

    # ------------------------------------------------------------------------
    # 恐龙状态更新函数
    def update(self, *args, **kwargs) -> None:
        if self.life:
            if self.isRunning:
                self.run()

            if self.isJumping:
                self.jump()

            if self.isDucking:
                self.duck()
        else:
            self.die()
        return super().update(*args, **kwargs)

    # ------------------------------------------------------------------------
    # 状态函数

    # 跑步时一直调用此函数实现恐龙的跑步特效
    def run(self):
        self.runTimer += 1

        if (self.runTimer//para.Para.RUN_CHANGE_FOOT_TIME) % 2 == 0:
            self.setImage(self.imageRun1, para.Para.SIZE_OF_DINO)
        else:
            self.setImage(self.imageRun2, para.Para.SIZE_OF_DINO)

    # 跳跃时一直调用此函数设定恐龙位置
    def jump(self):
        assert self.rect is not None

        # 从run状态转向jump状态
        if not self.isJumping:
            self.isJumping = True
            self.isRunning = False

            self.runTimer = 0

            self.setImage(self.imageJump, para.Para.SIZE_OF_DINO)

            # 若恐龙在duck状态，则打断此状态
            if self.isDucking:
                self.isDucking = False

        self.jumpTimer += 1

        # 实时计算恐龙位置的表达式
        # 上跳和下落可以用同一个表达式表示
        self.rect.bottom = self.runningBottom-para.Para.JUMP_HEIGHT_MAX\
            + (int)((para.Para.ACCELERATION *
                     (para.Para.JUMP_TIME/2-self.jumpTimer)**2)/2)

        # 从jump状态转向run状态
        if self.jumpTimer == para.Para.JUMP_TIME:
            self.isRunning = True
            self.isJumping = False

            self.jumpTimer = 0

            self.setImage(self.imageRun1, para.Para.SIZE_OF_DINO)
            self.rect.bottomleft = self.runningRect

    # 蹲起时一直调用此函数设定恐龙位置
    def duck(self):
        assert self.rect is not None
        if not self.isDucking:
            self.isDucking = True
            self.isRunning = False

            self.runTimer = 0

            self.setImage(self.imageDuck1, para.Para.SIZE_OF_DUCK_DINO)
            self.rect.bottomleft = self.duckingRect

            # 若恐龙在run状态，则打断此状态
            if self.isJumping:
                self.isJumping = False

        self.duckTimer += 1

        # 实现恐龙duck状态的跑步特效
        if (self.duckTimer//para.Para.DUCK_CHANGE_FOOT_TIME) % 2 == 0:
            self.setImage(self.imageDuck1, para.Para.SIZE_OF_DUCK_DINO)
        else:
            self.setImage(self.imageDuck2, para.Para.SIZE_OF_DUCK_DINO)

    # 从duck状态起立时调用此函数
    def unduck(self):
        assert self.rect is not None

        self.isRunning = True
        self.isDucking = False

        self.duckTimer = 0

        self.setImage(self.imageRun1, para.Para.SIZE_OF_DINO)
        self.rect.bottomleft = self.runningRect

    # 恐龙死亡时调用此函数加载死亡图片
    def die(self):

        assert self.image and self.rect is not None
        self.setImage(self.imageDead, para.Para.SIZE_OF_DEAD_DINO)

        # duck状态死亡时，rect回到run状态（死亡图片中的恐龙是run状态）
        if self.isDucking:
            self.rect.bottomleft = self.runningRect

    # ------------------------------------------------------------------------
    # 功能函数

    # 更改图片本体、尺寸并取mask蒙版
    def setImage(self, image, SIZE):
        self.image = image
        self.image = pygame.transform.scale(self.image, SIZE)
        self.mask = pygame.mask.from_surface(self.image)
