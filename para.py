'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 11:34:32
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2023-03-16 10:47:43
FilePath: \\chrome-dinosaur\\para.py
Description: Initial values of various variables and constants parameters.
             游戏中使用的各种常数参数或可变参数的初始值。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''


class Para:
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # Modifiable Parameters 可改参数            单位

    # 定义窗口
    WIDTH = 1600                            # 像素
    HEIGHT = 900                            # 像素
    FPS = 120                               # 帧
    BACKGROUND_COLOR = (255, 255, 255)      # RGB

    # 定义速度
    SPEED_INIT = (int)(WIDTH/FPS*0.6)       # 像素/帧   参数单位：秒
    SPEED_ADDER = (int)(WIDTH/FPS*0.1)      # 像素/帧   参数单位：秒

    # 文字尺寸
    SIZE_OF_TITLE = 75                      # 字体大小
    SIZE_OF_SCORE = 50                      # 字体大小

    # 各个事件的时间
    RUN_CHANGE_FOOT_TIME = (int)(FPS*0.1)   # 帧        参数单位：秒
    DUCK_CHANGE_FOOT_TIME = (int)(FPS*0.1)  # 帧        参数单位：秒
    FLAP_CHANGE_WING_TIME = (int)(FPS*0.5)  # 帧        参数单位：秒

    JUMP_TIME = (int)(FPS*0.6)              # 帧        参数单位：秒
    JUMP_HEIGHT_MAX = (int)(HEIGHT*0.3)     # 像素      参数单位：占窗口高度的比值

    # 生成器使用的概率值
    PROBABILITY_OF_BIRD = 0.3               # 概率值
    PROBABILITY_OF_DOUBLE_OBSTACLE = 0.4    # 概率值

    # --------------------------------------------------------------------------
    # Enlargement factor 放大倍数
    # 所有参数皆为倍率，无单位

    # 恐龙尺寸
    FACTOR_OF_DINO = 1.5
    FACTOR_OF_DUCK_DINO = 1.5
    FACTOR_OF_DEAD_DINO = 1.5

    # 大仙人掌尺寸
    FACTOR_OF_LARGE_CACTUS_1 = 1.7
    FACTOR_OF_LARGE_CACTUS_2 = 1.7
    FACTOR_OF_LARGE_CACTUS_3 = 1.7

    # 小仙人掌尺寸
    FACTOR_OF_SMALL_CACTUS_1 = 1.7
    FACTOR_OF_SMALL_CACTUS_2 = 1.7
    FACTOR_OF_SMALL_CACTUS_3 = 1.7

    # 鸟尺寸
    FACTOR_OF_BIRD = 1.5

    # 图标尺寸
    FACTOR_OF_GAME_OVER = 1.5
    FACTOR_OF_RESET = 1

    # 鸟速相对地速的倍率
    FACTOR_OF_BIRD_MAX_SPEED = 1.4
    FACTOR_OF_BIRD_MIN_SPEED = 0.8

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # Fixed Parameters 固定参数

    # 窗口大小元组
    RESOLUTION = (WIDTH, HEIGHT)

    # 重力加速度
    ACCELERATION = 2*JUMP_HEIGHT_MAX / (JUMP_TIME**2)  # 单位：像素/帧^2

    # 初始化最高分
    highestScore = 0

    # --------------------------------------------------------------------------
    # attribute of Sprite dinosaur
    WIDTH_OF_DINO = FACTOR_OF_DINO*87
    HEIGHT_OF_DINO = FACTOR_OF_DINO*94
    SIZE_OF_DINO = (WIDTH_OF_DINO, HEIGHT_OF_DINO)

    WIDTH_OF_DUCK_DINO = FACTOR_OF_DUCK_DINO*117
    HEIGHT_OF_DUCK_DINO = FACTOR_OF_DUCK_DINO*60
    SIZE_OF_DUCK_DINO = (WIDTH_OF_DUCK_DINO, HEIGHT_OF_DUCK_DINO)

    WIDTH_OF_DEAD_DINO = FACTOR_OF_DEAD_DINO*86
    HEIGHT_OF_DEAD_DINO = FACTOR_OF_DEAD_DINO*101
    SIZE_OF_DEAD_DINO = (WIDTH_OF_DEAD_DINO, HEIGHT_OF_DEAD_DINO)

    # --------------------------------------------------------------------------
    # attribute of Sprite large cactus
    WIDTH_OF_LARGE_CACTUS_1 = FACTOR_OF_LARGE_CACTUS_1*48
    HEIGHT_OF_LARGE_CACTUS_1 = FACTOR_OF_LARGE_CACTUS_1*95
    SIZE_OF_LARGE_CACTUS_1 = (WIDTH_OF_LARGE_CACTUS_1,
                              HEIGHT_OF_LARGE_CACTUS_1)

    WIDTH_OF_LARGE_CACTUS_2 = FACTOR_OF_LARGE_CACTUS_2*99
    HEIGHT_OF_LARGE_CACTUS_2 = FACTOR_OF_LARGE_CACTUS_2*95
    SIZE_OF_LARGE_CACTUS_2 = (WIDTH_OF_LARGE_CACTUS_2,
                              HEIGHT_OF_LARGE_CACTUS_2)

    WIDTH_OF_LARGE_CACTUS_3 = FACTOR_OF_LARGE_CACTUS_3*102
    HEIGHT_OF_LARGE_CACTUS_3 = FACTOR_OF_LARGE_CACTUS_3*95
    SIZE_OF_LARGE_CACTUS_3 = (WIDTH_OF_LARGE_CACTUS_3,
                              HEIGHT_OF_LARGE_CACTUS_3)

    # --------------------------------------------------------------------------
    # attribute of Sprite small cactus
    WIDTH_OF_SMALL_CACTUS_1 = FACTOR_OF_SMALL_CACTUS_1*40
    HEIGHT_OF_SMALL_CACTUS_1 = FACTOR_OF_SMALL_CACTUS_1*71
    SIZE_OF_SMALL_CACTUS_1 = (WIDTH_OF_SMALL_CACTUS_1,
                              HEIGHT_OF_SMALL_CACTUS_1)

    WIDTH_OF_SMALL_CACTUS_2 = FACTOR_OF_SMALL_CACTUS_2*68
    HEIGHT_OF_SMALL_CACTUS_2 = FACTOR_OF_SMALL_CACTUS_2*71
    SIZE_OF_SMALL_CACTUS_2 = (WIDTH_OF_SMALL_CACTUS_2,
                              HEIGHT_OF_SMALL_CACTUS_2)

    WIDTH_OF_SMALL_CACTUS_3 = FACTOR_OF_SMALL_CACTUS_3*105
    HEIGHT_OF_SMALL_CACTUS_3 = FACTOR_OF_SMALL_CACTUS_3*71
    SIZE_OF_SMALL_CACTUS_3 = (WIDTH_OF_SMALL_CACTUS_3,
                              HEIGHT_OF_SMALL_CACTUS_3)

    # --------------------------------------------------------------------------
    # attribute of Sprite bird
    WIDTH_OF_BIRD = FACTOR_OF_BIRD*93
    HEIGHT_OF_BIRD = FACTOR_OF_BIRD*62
    SIZE_OF_BIRD = (WIDTH_OF_BIRD, HEIGHT_OF_BIRD)

    # --------------------------------------------------------------------------
    # attribute of picture GameOver
    WIDTH_OF_GAME_OVER = FACTOR_OF_GAME_OVER*386
    HEIGHT_OF_GAME_OVER = FACTOR_OF_GAME_OVER*40
    SIZE_OF_GAME_OVER = (WIDTH_OF_GAME_OVER, HEIGHT_OF_GAME_OVER)

    # --------------------------------------------------------------------------
    # attribute of picture reset
    WIDTH_OF_RESET = FACTOR_OF_RESET*75
    HEIGHT_OF_RESET = FACTOR_OF_RESET*101
    SIZE_OF_RESET = (WIDTH_OF_RESET, HEIGHT_OF_RESET)
