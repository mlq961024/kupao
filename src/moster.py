#_*_coding:utf-8 _*_
#开发人员：莫立庆
#开发时间：2019/7/8 20:33
#文件名称： moster.py
#开发工具： PyCharm
'''怪物类'''
import pygame
from random import randint,choice


#怪物1
class Moster_1(pygame.sprite.Sprite):#上
    energy=1
    def __init__(self,bg_size):
        super(Moster_1,self).__init__()
        i = randint(1, 3)
        if i == 1:
            self.image_enemy_1 = pygame.image.load('../image/飞机.png')
        elif i == 2:
            self.image_enemy_1 = pygame.image.load('../image/鸟1.png')
        else:
            self.image_enemy_1 = pygame.image.load('../image/鸟3.png')
        self.rect = self.image_enemy_1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        #敌机初始位置
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,100)), 20)  # 上

        #生存状态
        self.active=True
        self.energy=Moster_1.energy
        '''死亡状态'''

        #移动方法
    def move(self,speed):
        if self.rect.right > 0:
            self.rect.right -= speed
        else:
            self.reset()


    def reset(self):
        i = randint(1, 3)
        if i == 1:
            self.image_enemy_1 = pygame.image.load('../image/飞机.png')
        elif i == 2:
            self.image_enemy_1 = pygame.image.load('../image/鸟1.png')
        else:
            self.image_enemy_1 = pygame.image.load('../image/鸟3.png')
        self.rect = self.image_enemy_1.get_rect()

        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        # 敌机初始位置
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width, 100)), 20)  # 上

        # 生存状态
        self.active = True
        self.energy = Moster_1.energy
class Moster_2(pygame.sprite.Sprite):#中
    energy=2
    def __init__(self,bg_size):
        super(Moster_2,self).__init__()
        self.image_enemy_1 = pygame.image.load('../image/火箭1.png')
        self.image_enemy_2 = pygame.image.load('../image/火箭1_1.png')
        self.rect=self.image_enemy_1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        #敌机初始位置
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,200)), self.height//2-self.rect.height)  # 中

        #生存状态
        self.active=True
        self.energy=Moster_1.energy
        '''死亡状态'''
        #移动方法
    def move(self,speed):
        if self.rect.right > 0:
            self.rect.right -=((speed*2)/3)
        else:
            self.reset()


    def reset(self):
        self.active=True
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,200)), self.height//2-self.rect.height)  # 中

class Moster_3(pygame.sprite.Sprite):  # xia
    energy = 2

    def __init__(self, bg_size):
        super(Moster_3, self).__init__()
        i=randint(1,4)
        if i==1:
            self.image_enemy_1 = pygame.image.load('../image/炸弹.png')
        if i==2:
            self.image_enemy_1 = pygame.image.load('../image/树桩.png')
        if i==3:
            self.image_enemy_1 = pygame.image.load('../image/仙人掌2.png')
        if i==4:
            self.image_enemy_1 = pygame.image.load('../image/狮子.png')

        self.rect = self.image_enemy_1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)
        # 敌机初始位置
        self.rect.left, self.rect.top = (
        choice(range(self.width, 2 * self.width,100)),350-self.rect.height)  # 下

        # 生存状态
        self.active = True
        self.energy = Moster_1.energy
        '''死亡状态'''
        # 移动方法

    def move(self,speed):
        if self.rect.right > 0:
            self.rect.right -=speed
        else:
            self.reset()

    def reset(self):
        i = randint(1,4)
        if i == 1:
            self.image_enemy_1 = pygame.image.load('../image/炸弹.png')
        if i == 2:
            self.image_enemy_1 = pygame.image.load('../image/仙人掌2.png')
        if i == 3:
            self.image_enemy_1 = pygame.image.load('../image/树桩.png')
        if i == 4:
            self.image_enemy_1 = pygame.image.load('../image/狮子.png')


        self.rect = self.image_enemy_1.get_rect()

        self.mask = pygame.mask.from_surface(self.image_enemy_1)
        # 敌机初始位置
        self.rect.left, self.rect.top = (
            choice(range(self.width, 2 * self.width, 100)), 350 - self.rect.height)  # 下

        # 生存状态
        self.active = True
        self.energy = Moster_1.energy

class Moster_4(pygame.sprite.Sprite):  # 跳
    energy = 5

    def __init__(self, bg_size):
        super(Moster_4, self).__init__()
        self.image_enemy_1 = pygame.image.load('../image/小怪兽.png')
        self.rect = self.image_enemy_1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        # 敌机初始位置
        self.rect.left, self.rect.top = (
        choice(range(self.width, 2 * self.width,100)),350-self.rect.height)  # 下
        self.speed = 5
        # 生存状态
        self.active = True
        self.energy = Moster_1.energy
        '''死亡状态'''

        # 移动方法

    def move(self,speed):
        if speed!=0:
            if self.rect.right > 0:
                self.rect.right -= 2*speed
                if self.rect.top <= 0 or self.rect.bottom >= self.height:
                    self.speed = 0-self.speed
                self.rect.top -= self.speed
            else:
                self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = (
            choice(range(self.width, 2 * self.width, 100)), 350 - self.rect.height)


class Moster_5(pygame.sprite.Sprite):#斜飞
    energy=1
    def __init__(self,bg_size):
        super(Moster_5,self).__init__()
        self.image_enemy_1 = pygame.image.load('../image/鸟2.png')
        self.rect = self.image_enemy_1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)
        self.speed = 3.0
        #敌机初始位置
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,100)), 20)  # 上

        #生存状态
        self.active=True
        self.energy=Moster_1.energy
        '''死亡状态'''

        #移动方法
    def move(self,speed):
        if speed!=0:
            if self.rect.right > 0:
                self.rect.right -= 2*speed
                if self.rect.left<self.width:
                    self.rect.top+=1
            else:
                self.reset()


    def reset(self):
        self.active=True
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,100)), 20)  # 上
class Moster_6(pygame.sprite.Sprite):#dou
    energy=5
    def __init__(self,bg_size):
        super(Moster_6,self).__init__()
        self.image_enemy_1 = pygame.image.load('../image/小汽车.png')
        self.rect = self.image_enemy_1.get_rect()
        self.bg_size=bg_size
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)

        #敌机初始位置
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width,100)),350-self.rect.height )  # 上

        #生存状态
        self.active=True
        self.energy=Moster_1.energy
        '''死亡状态'''
        #移动方法
    def move(self,speed):
        if speed!=0:
            if self.rect.right > 0:
                self.rect.right -= 2*speed
                if self.rect.top <= 310:
                    speed = -speed
                self.rect.top -= speed
            else:
                self.reset()


    def reset(self):
        self.active=True
        self.rect.left, self.rect.top = (choice(range(self.width, 2 * self.width, 100)), 350 - self.rect.height)  # 上


class Moster_7(pygame.sprite.Sprite):  # 大怪物
    energy = 2

    def __init__(self, bg_size):
        super(Moster_7, self).__init__()
        self.image_enemy_1 = pygame.image.load('../image/大怪兽1.png')
        self.image_enemy_2 = pygame.image.load('../image/大怪物1_1.png')
        self.rect = self.image_enemy_1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_enemy_1)
        # 敌机初始位置
        self.rect.left, self.rect.top = (self.width,350-self.rect.height)  # 下

        # 生存状态
        self.active = True
        self.energy = Moster_1.energy
        '''死亡状态'''
        # 移动方法

    def move(self,speed):
        if self.rect.right > 0:
            self.rect.right -=speed*3
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = (self.width,350-self.rect.height)  # 下
