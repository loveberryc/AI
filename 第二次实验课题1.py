import pygame
import sys
from pygame.locals import *
pygame.init()  # 初试化pygame

white_colour = pygame.Color(255, 255, 255)  # 白色
black_colour = pygame.Color(0, 0, 0)  # 黑色
game_surface = pygame.display.set_mode((600, 400))  # 设置pygame游戏框大小
pygame.display.set_caption("贪吃蛇")  # 设置游戏标题

def main():
    head_position = [100, 100]  # 蛇的初试位置
    while True:
        game_surface.fill(black_colour) # 背景填充为黑色
        pygame.draw.rect(game_surface, white_colour, Rect(head_position[0], head_position[1], 20, 20))  # 在[100, 100]处画20*20的矩形
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 如果是退出键则退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == 27:  # 按esc键退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == 119:
                head_position[1] = head_position[1] - 20
            elif event.type == pygame.KEYDOWN and event.key == 115:
                head_position[1] = head_position[1] + 20
            elif event.type == pygame.KEYDOWN and event.key == 100:
                head_position[0] = head_position[0] + 20
            elif event.type == pygame.KEYDOWN and event.key == 97:
                head_position[0] = head_position[0] - 20
            pygame.display.update()

main()