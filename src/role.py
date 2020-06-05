#_*_coding:utf-8 _*_
#开发人员：莫立庆
#开发时间：2019/7/7 23:08
#文件名称： role.py
#开发工具： PyCharm
import  pygame

class Role(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        super(Role, self).__init__()
        # 确定玩家的两张图片
        self.image_one = pygame.image.load('../image/主角猪1_1.png')
        self.image_two = pygame.image.load('../image/主角猪1_2.png')
        self.image_three = pygame.image.load('../image/无敌光圈.png')
        self.image_four=pygame.image.load("../image/加速火焰.png")

        self.high=self.image_one.get_height()
        # 获取角色位置
        self.rect = self.image_one.get_rect()
        # 获取背景图片宽高
        self.width, self.height = bg_size[0], bg_size[1]
        self.or_speed=[0,0]
        # 获取角色图片的掩模，用来精确碰撞
        self.mask = pygame.mask.from_surface(self.image_one)
        # 设置玩家初始位置
        self.rect.left, self.rect.top = (120, 370+self.high)

        self.active = True
        '''角色死亡效果'''
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = (120, 370-self.high)

class Role_1(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        super(Role_1, self).__init__()
        # 确定玩家的两张图片
        self.image_one = pygame.image.load('../image/主角猪1_1.png')
        self.image_two = pygame.image.load('../image/主角猪1_2.png')
        self.high=self.image_one.get_height()
        # 获取角色位置
        self.rect = self.image_one.get_rect()
        # 获取背景图片宽高
        self.width, self.height = bg_size[0], bg_size[1]
        self.or_speed=[0,0]
        # 获取角色图片的掩模，用来精确碰撞
        self.mask = pygame.mask.from_surface(self.image_one)
        # 设置玩家初始位置
        self.rect.left, self.rect.top = (120, 370+self.high)

        self.active = True
        '''角色死亡效果'''

    # def update(self, *args):
    #     #     self.image = self.images[args[0] % len(self.images)]
    #     #     if self.is_click:
    #     #         self.rect.left -= (self.rect.left - 250) / self.times
    #     #         self.rect.top -= (self.rect.top - 30) / self.times
    #     #
    #     #         self.image = pygame.transform.smoothscale(self.image, (
    #     #         self.rect.width // self.times * self.scale, self.rect.height // self.times * self.scale))
    #     #         if self.scale > 1:
    #     #             self.scale -= 1
    #     #
    #     #         print(self.rect.left)
    #     #         if self.rect.left <= 250 and self.rect.top <= 30:
    #     #             self.kill()






