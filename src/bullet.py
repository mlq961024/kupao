#_*_coding:utf-8 _*_
#开发人员：莫立庆
#开发时间：2019/7/8 20:57
#文件名称： bullet.py
#开发工具： PyCharm
#_*_coding:utf-8 _*_
#开发人员：莫立庆
#开发时间：2019/7/8 14:16
#文件名称： bullet.py
#开发工具： PyCharm
'''子弹实体类'''
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,bg_size):
        super(Bullet,self).__init__()
        self.image=pygame.image.load('../image/子弹.png')
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        #获得人物位置(右，上)
        self.rect.right,self.rect.top=position
        self.rect.right += 20


        self.active=True
        self.mask = pygame.mask.from_surface(self.image)
    def move_bullet(self,speed):
        if self.rect.right>=self.width:
            self.active=False
        else:
            self.rect.right+=(speed*4)
    def reset(self,position):
        if self.rect.right>self.width or self.active==False:
            self.active=True
            self.rect.right, self.rect.top = position
            self.rect.right += 20
