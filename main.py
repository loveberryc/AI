# 这是一个pygame的最小开发框架
import pygame
import sys

pygame.init()  # 初试化pygame
screen = pygame.display.set_mode((600, 400))  # 设置pygame游戏框大小
pygame.display.set_caption("Pygame游戏之旅")  # 设置游戏标题

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
