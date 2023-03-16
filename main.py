'''
Author: MaseChen CYXSam2003@126.com
Date: 2022-11-15 23:27:00
LastEditors: MaseChen CYXSam2003@126.com
LastEditTime: 2022-11-22 22:15:22
FilePath: \\dino\\main.py
Description: Used to launch the game.
             启动游戏。

Copyright (c) 2022 by MaseChen CYXSam2003@126.com, All Rights Reserved.
'''


import menu

"""
Operating environment:
运行环境：
Windows 10 22H2
Python 3.10.6 64bit
"""

"""
Main problems:
Obstacle generation logic is weak and the obstacles occasionally overlaps.
Abnormal display when dying in dinosaur.duck state.
Displayed obstacles will not accelerate in real time
when the acceleration threshold is reached.

主要问题：
障碍物生成逻辑稀烂，偶尔还会重叠在一起
在dinosaur.duck状态死亡时显示异常
达到加速阈值时已显示的障碍物不会自动加速
"""


def main():
    play = menu.Menu()
    play.menu()


if __name__ == "__main__":
    main()
