'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 22:48:03
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2023-03-16 10:47:14
FilePath: \\chrome-dinosaur\\obstacle.py
Description: Implement the obstacles:
             Large Cactus, Small Cactus and Bird,
             with their parent class Obstacles.

             障碍物类。
             实现Obstacle父类下的三种障碍物Large Cactus、Small Cactus、Bird。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''


import random
import pygame

import para


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed, *groups) -> None:
        super().__init__(*groups)
        self.speed = speed

    # 随机返回一个生成障碍物的位置
    def randRectRight(self) -> int:
        temp = random.randint(0, 2)

        match temp:
            case 0:
                return (int)(para.Para.WIDTH*1)
            case 1:
                return (int)(para.Para.WIDTH*1.5)
            case 2:
                return (int)(para.Para.WIDTH*2)

        return 0

    # ------------------------------------------------------------------------
    # 障碍物状态更新函数
    def update(self, * args, **kwargs) -> None:
        assert self.rect is not None
        self.rect.left -= self.speed
        return super().update(*args, **kwargs)

    # ------------------------------------------------------------------------
    # 功能函数
    def setImage(self, image, SIZE):
        # 更改图片本体、尺寸并取mask蒙版
        self.image = image
        self.image = pygame.transform.scale(self.image, SIZE)
        self.mask = pygame.mask.from_surface(self.image)


class LargeCactus(Obstacle):
    def __init__(self, speed, *groups) -> None:
        super().__init__(speed, *groups)
        # --------------------------------------------------------------------
        # 随机初始化一种大仙人掌
        match random.randint(0, 2):
            case 0:
                self.image1 = pygame.image.load(
                    "Assets\\Cactus\\LargeCactus1.png").convert_alpha()
                self.setImage(self.image1,
                              para.Para.SIZE_OF_LARGE_CACTUS_1)
            case 1:
                self.image2 = pygame.image.load(
                    "Assets\\Cactus\\LargeCactus2.png").convert_alpha()
                self.setImage(self.image2,
                              para.Para.SIZE_OF_LARGE_CACTUS_2)
            case 2:
                self.image3 = pygame.image.load(
                    "Assets\\Cactus\\LargeCactus3.png").convert_alpha()
                self.setImage(self.image3,
                              para.Para.SIZE_OF_LARGE_CACTUS_3)

        # ----------------------------------------------------------------------
        # 生成rect
        assert self.image is not None
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.randRectRight(),
                                 (int)(para.Para.HEIGHT*(2/3)))

    def setImage(self, image, SIZE):
        return super().setImage(image, SIZE)

    def randRectRight(self) -> int:
        return super().randRectRight()

    def update(self, *args, **kwargs) -> None:
        return super().update(*args, **kwargs)


class SmallCactus(Obstacle):
    def __init__(self, speed, *groups) -> None:
        super().__init__(speed, *groups)
        # --------------------------------------------------------------------
        # 随机初始化一种小仙人掌
        match random.randint(0, 2):
            case 0:
                self.image1 = pygame.image.load(
                    "Assets\\Cactus\\SmallCactus1.png").convert_alpha()
                self.setImage(self.image1,
                              para.Para.SIZE_OF_SMALL_CACTUS_1)
            case 1:
                self.image2 = pygame.image.load(
                    "Assets\\Cactus\\SmallCactus2.png").convert_alpha()
                self.setImage(self.image2,
                              para.Para.SIZE_OF_SMALL_CACTUS_2)
            case 2:
                self.image3 = pygame.image.load(
                    "Assets\\Cactus\\SmallCactus3.png").convert_alpha()
                self.setImage(self.image3,
                              para.Para.SIZE_OF_SMALL_CACTUS_3)

        # ----------------------------------------------------------------------
        # 生成rect
        assert self.image is not None
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.randRectRight(),
                                 (int)(para.Para.HEIGHT*(2/3)))

    def setImage(self, image, SIZE):
        return super().setImage(image, SIZE)

    def randRectRight(self) -> int:
        return super().randRectRight()

    def update(self, *args, **kwargs) -> None:
        return super().update(*args, **kwargs)


class Bird(Obstacle):
    def __init__(self, speed, *groups) -> None:
        super().__init__(speed, *groups)
        # --------------------------------------------------------------------
        # 载入鸟素材
        self.image1 = pygame.image.load(
            "Assets\\Bird\\Bird1.png").convert_alpha()
        self.image2 = pygame.image.load(
            "Assets\\Bird\\Bird2.png").convert_alpha()

        self.setImage(self.image1, para.Para.SIZE_OF_BIRD)

        # ----------------------------------------------------------------------
        # 随机位置生成rect
        match random.randint(0, 2):
            case 0:
                self.bottom = (int)(para.Para.HEIGHT*(2/3))
            case 1:
                self.bottom = (int)(para.Para.HEIGHT*(13/24))
            case 2:
                self.bottom = (int)(para.Para.HEIGHT*(1/2))

        assert self.image is not None
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.randRectRight(), self.bottom

        # ----------------------------------------------------------------------
        # 随机速度生成
        self.MAX_SPEED_OF_BIRD = (int)(
            para.Para.FACTOR_OF_BIRD_MAX_SPEED*speed)
        self.MIN_SPEED_OF_BIRD = (int)(
            para.Para.FACTOR_OF_BIRD_MIN_SPEED*speed)

        self.speed = random.randint(self.MIN_SPEED_OF_BIRD,
                                    self.MAX_SPEED_OF_BIRD)

        # ----------------------------------------------------------------------
        # 计时器
        self.flapTimer = 0

    def setImage(self, image, SIZE):
        return super().setImage(image, SIZE)

    def randRectRight(self) -> int:
        return super().randRectRight()

    # 实时更新鸟拍翅膀动作
    def update(self, *args, **kwargs) -> None:
        assert self.rect is not None

        self.flapTimer += 1

        if (self.flapTimer//para.Para.FLAP_CHANGE_WING_TIME) % 2 == 0:
            self.setImage(self.image1, para.Para.SIZE_OF_BIRD)
            self.rect.bottom = self.bottom
        else:
            self.setImage(self.image2, para.Para.SIZE_OF_BIRD)
            self.rect.bottom = self.bottom-(int)(para.Para.HEIGHT*(1/36))

        # 更新速度
        return super().update(*args, **kwargs)
