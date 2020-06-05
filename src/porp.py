#_*_coding:utf-8_*_
#开发人员：王鑫
#开发时间：2019/7/9 20:18
#文件名称： porp.py
#开发工具： PyCharm

#道具1
import pygame
from random import randint

class Porp(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(Porp, self).__init__()
        i=randint(1,3)
        if i==1:
            self.image_enemy_1 = pygame.image.load('../image/道具1.png')
            self.flash=1
        if i==2:
            self.image_enemy_1 = pygame.image.load('../image/道具2.png')
            self.flash = 2
        if i==3:
            self.image_enemy_1 = pygame.image.load('../image/道具3.png')
            self.flash = 3

        self.rect = self.image_enemy_1.get_rect()
        self.speed=2
        self.width, self.height = bg_size[0], bg_size[1]

        self.mask = pygame.mask.from_surface(self.image_enemy_1)


        # 敌机初始位置
        self.rect.left, self.rect.top = (
            randint(self.width, self.width + 500), randint(0, self.height - self.rect.height))
        # 生存状态
        self.active = True
    def move(self,speed):
        if speed != 0:
            if self.rect.right > 0:
                self.rect.right -= 2 * speed
                if self.rect.top <= 0 or self.rect.bottom >= self.height:
                    self.speed = 0 - self.speed
                self.rect.top -= self.speed
            else:
                self.reset()
    def reset(self):
        self.active=True
        i = randint(1, 3)
        if i == 1:
            self.image_enemy_1 = pygame.image.load('../image/道具1.png')
            self.flash = 1
        if i == 2:
            self.image_enemy_1 = pygame.image.load('../image/道具2.png')
            self.flash = 2
        if i == 3:
            self.image_enemy_1 = pygame.image.load('../image/道具3.png')
            self.flash = 3
        self.rect = self.image_enemy_1.get_rect()

        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        # 敌机初始位置

        self.active = True
        self.rect.left, self.rect.top = (
            randint(self.width, self.width + 500), randint(0, self.height -self.rect.height))
