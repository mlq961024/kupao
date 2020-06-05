#_*_coding:utf-8 _*_
#开发人员：莫立庆
#开发时间：2019/7/7 21:36
#文件名称： main.py
#开发工具： PyCharm
import pygame,sys
from pygame.locals import *
from src.role import *
from src.bullet import *
from src.moster import *
from  src.porp import *


#窗体高度宽度
size_width=1000
size_height=420
bg_size=(size_width,size_height)
bg_speed = 0 #背景速度
pygame.init()
pygame.display.set_caption("重力小猪——")
#载入音乐
bg_music=pygame.mixer.music.load("../music/bg_music.wav")
pygame.mixer.music.play(-1)
bullet_sound = pygame.mixer.Sound("../music/子弹.wav")
porp_sound_1 = pygame.mixer.Sound("../music/吃到道具1.wav")
porp_sound_2 = pygame.mixer.Sound("../music/吃到道具2.wav")
porp_sound_3 =pygame.mixer.Sound("../music/获得子弹道具.wav")
role_die_sound =pygame.mixer.Sound("../music/死亡.wav")
moster_die_sound=pygame.mixer.Sound("../music/怪物死.wav")
role_re_sound=pygame.mixer.Sound("../music/复活.wav")
role_re_sound=pygame.mixer.Sound("../music/复活.wav")
backgroung_1= pygame.image.load('../image/background_1.jpg')
singal=pygame.image.load("../image/logo.png")
backgroung_2= pygame.image.load('../image/background_2.jpg')
distance_image=pygame.image.load('../image/距离.png')
score_image=pygame.image.load('../image/得分.png')
die_bg_image=pygame.image.load("../image/死亡背景.png")
start_bg_image=pygame.image.load("../image/开始背景背景.png")
screen=pygame.display.set_mode(bg_size)
width=backgroung_1.get_width() #获得背景宽度
ourrole=Role(bg_size) #创建我方角色
ourrole_1=Role_1(bg_size)
def add_Moster_1(group1,group2,num):#上方怪物
    for i in range(num):
        sm=Moster_1(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_2(group1,group2,num):#中间怪物
    for i in range(num):
        sm = Moster_2(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_3(group1,group2,num):#下方怪物
    for i in range(num):
        sm = Moster_3(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_4(group1,group2,num):#会跳的怪物
    for i in range(num):
        sm = Moster_4(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_5(group1,group2,num):#斜飞的怪物
    for i in range(num):
        sm = Moster_5(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_6(group1,group2,num):#会抖的怪物
    for i in range(num):
        sm = Moster_6(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_Moster_7(group1,group2,num):#大怪物
    for i in range(num):
        sm = Moster_7(bg_size)
        group1.add(sm)
        group2.add(sm)

def add_porp(group1,group2,num):#随机出现的道具
    for i in range(num):
        por = Porp(bg_size)
        group1.add(por)
        group2.add(por)

def delay_moster(moster,bg_speed):#产生正常怪物
    for each in moster:
        if each.active:
            each.move(bg_speed)
            screen.blit(each.image_enemy_1, each.rect)
        else:
            each.reset()
def delay_moster_1(moster,bg_speed,score):#产生2，7怪物
    for each in moster:
        if each.active:
            each.move(bg_speed)
            if score%10:
                screen.blit(each.image_enemy_1, each.rect)
            else:
                screen.blit(each.image_enemy_2, each.rect)
        else:
            each.reset()
def main():
    runing=True#程序运行状态
    index=0#得分
    score=0#判断图片循环
    score_1=0#记距离
    score_3 = -1000  # 恢复暂停
    score_4=0#道具存在时间
    switch_suspend=True #按空格暂停关键
    switch_trun=False#角色图片翻转关键
    switch_pengzhung=True#无敌状态关键
    switch_prop=0#吃道具选择
    switch_speed=True#加速状态关键
    x=0#图片循环坐标
    max_speed=3#最大速度
    delay = max_speed+15#加速状态值
    speed=[0, 0]#角色移动速度
    start=True#重新开始或结束
    end=False#结束动画控制

    prop_time=0#道具作用时间
    deffict=1#难度---------------------调节
    mosters=pygame.sprite.Group()#怪物组
    moster_1 = pygame.sprite.Group()#上方怪物组（3个）
    add_Moster_1(mosters,moster_1,3)

    moster_2 = pygame.sprite.Group()#中间怪物组（难度）
    add_Moster_2(mosters,moster_2, deffict)

    moster_3 = pygame.sprite.Group()#下方怪物组
    add_Moster_3(mosters,moster_3, 2)

    moster_4 = pygame.sprite.Group()#跳动怪物组
    add_Moster_4(mosters,moster_4, deffict+1)

    moster_5 = pygame.sprite.Group()#斜飞鸟
    add_Moster_5(mosters,moster_5, deffict+2)

    moster_6 = pygame.sprite.Group()#抖动组
    add_Moster_6(mosters, moster_6, deffict+1)

    moster_7 = pygame.sprite.Group()#大怪兽
    add_Moster_7(mosters, moster_7, deffict)

    moster_8 = pygame.sprite.Group()#上方怪物组多
    add_Moster_1(mosters, moster_8, deffict+3)

    moster_9 = pygame.sprite.Group()#中间怪物组多
    add_Moster_2(mosters, moster_9, deffict+1)

    moster_10 = pygame.sprite.Group()#下方怪物组
    add_Moster_3(mosters, moster_10, deffict+3)

    porps=pygame.sprite.Group()#随机道具组
    porp_1 = pygame.sprite.Group()#一个道具
    add_porp(porps, porp_1, 1)

    porp_2 = pygame.sprite.Group()#两个道具
    add_porp(porps, porp_2, 2)
    porp_3 = pygame.sprite.Group()#三个道具
    add_porp(porps, porp_3, 3)
    bullet1 = []#创建子弹
    BULLET1_NUM = 4#子弹数量
    for i in range(BULLET1_NUM):#添加子弹到组
        bullet=Bullet((ourrole.rect.right, ourrole.rect.top + ourrole.high // 2),bg_size)
        bullet1.append(bullet)
    ourroles = []#产生我方角色组
    ourroles.append(ourrole)
    going=True#开始界面进入动画
    max_distance=0.0#最远距离
    max_index=0.0#最大积分
    x_distance = 60
    while runing:#开始
        if start==False:#结束界面
            if end==False:
                if max_distance<score_1:
                    max_distance=score_1
                if max_index < index:
                    max_index = index
                screen.blit(backgroung_1, (0, 0))
                screen.blit(die_bg_image,(0,0))
                fontObj6 = pygame.font.SysFont('..font/font.ttf', 40)
                textSurface = fontObj6.render('%.d'%(max_distance/10), True,(255,97, 0))
                textRect = textSurface.get_rect()
                textRect.center = (750,110)
                screen.blit(textSurface, textRect)
                fontObj6 = pygame.font.SysFont('..font/font.ttf', 40)
                textSurface = fontObj6.render('%.d' % max_index , True, (255, 97, 0))
                textRect = textSurface.get_rect()
                textRect.center = (750, 40)
                screen.blit(textSurface, textRect)
                fontObj6 = pygame.font.SysFont('..font/font.ttf', 50)
                textSurface = fontObj6.render('%.d' % index, True, (255, 97, 0))
                textRect = textSurface.get_rect()
                textRect.center = (560, 205)
                screen.blit(textSurface, textRect)

            for event in pygame.event.get():  # 检测是否是退出时间
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key==K_r:#重新开始
                        start = True
                        role_re_sound.play()
                        score_1=0
                        index=0
                        speed=[0,0]
                        switch_prop=0
                        if switch_trun:
                            ourrole.image_one = pygame.transform.flip(ourrole.image_one, False, True)
                            ourrole.image_two = pygame.transform.flip(ourrole.image_two, False, True)
                            switch_trun=False
                        ourrole.reset()
                        for i in mosters:
                            i.active=False
                        for i in porps:
                            i.active=False
                    elif event.key==K_c:#结束
                        end=True
                    else:
                        pass
            x_x=80
            y_y=275
            while end:
                screen.blit(backgroung_1, (0, 0))
                if ourrole_1.active:
                    if x_distance % 2:  # 绘制角色
                        screen.blit(ourrole_1.image_one, (x_x,y_y))
                    else:
                        screen.blit(ourrole_1.image_two, (x_x,y_y))
                    if x_x < width // 2 :
                        x_x += 1
                    else:
                        x_x=width//2
                        y_y -= 2
                        ourrole_1.image_one=ourrole_1.update()
                        if y_y <=100:
                            end=False
                            runing=False
                pygame.display.flip()
                x_distance -= 1
                if x_distance<=0:
                    x_distance = 60
        else:
            if going==True:#开始界面
                x -=2
                screen.blit(backgroung_1, (x, 0))
                screen.blit(backgroung_1, (x + width, 0))
                screen.blit(start_bg_image, (0, 0))
                if x_distance % 2:  # 绘制角色
                    screen.blit(ourrole_1.image_one, (90,275))
                else:
                    screen.blit(ourrole_1.image_two, (90,275))
                x_distance-=1
                if x <= 10 - size_width:
                    x = 0
                    x_distance=60
                for event in pygame.event.get():  # 检测是否是退出时间
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == KEYDOWN:
                        going=False
            else:#正式游戏
                '''背景循环'''
                if score_1 // 1000 <= max_speed:
                    bg_speed = score_1 // 1000 + 1
                else:
                    bg_speed = max_speed
                if score<=1000:
                    x-=bg_speed
                    screen.blit(backgroung_1, (x, 0))
                    screen.blit(backgroung_1, (x + width, 0))
                elif 1000<score<=2000:
                    x -= bg_speed
                    screen.blit(backgroung_2, (x, 0))
                    screen.blit(backgroung_2, (x + width, 0))
                elif score>2000:
                    score=0
                '''积分绘制'''
                screen.blit(distance_image,(850,10))
                fontObj4 = pygame.font.SysFont('..font/font.ttf', 30)
                textSurface_1 = fontObj4.render('%d' % (score_1/10.0), True, (255, 97, 0))
                textRect_1 = textSurface_1.get_rect()
                textRect_1.center = (930, 19)
                screen.blit(textSurface_1, textRect_1)
                '''距离绘制'''
                screen.blit(score_image, (850, 38))
                fontObj5 = pygame.font.SysFont('..font/font.ttf', 30)
                textSurface_2 = fontObj5.render('%d' % index, True, (255,97, 0))
                textRect_2 = textSurface_2.get_rect()
                textRect_2.center = (930, 47)
                screen.blit(textSurface_2, textRect_2)
                if ourrole.active:#角色存活
                    if score%2:#绘制角色
                        screen.blit(ourrole.image_one, ourrole.rect)
                    else:
                        screen.blit(ourrole.image_two, ourrole.rect)
                    if prop_time>10-deffict:#道具使用时间复位
                        #print("道具到期")
                        switch_prop=0
                        score_4=0
                        prop_time=0
                        switch_pengzhung = True
                        switch_speed = True
                    else:#简化道具时间方法
                        if (not score_4%1050)and(score_4!=0):
                            prop_time+=1
                        '''发射子弹'''
                        if switch_prop==1:
                            switch_pengzhung = True
                            switch_speed=True
                            for b in bullet1:
                                if b.active:
                                    screen.blit(b.image, b.rect)
                                    bullet_sound.play()
                                    b.move_bullet(bg_speed)
                                    score_4 += 1
                                    '''子弹碰撞检测'''
                                    enemy_hit = pygame.sprite.spritecollide(b, mosters, False, pygame.sprite.collide_mask)
                                    if enemy_hit:
                                        b.active = False
                                        for e in enemy_hit:
                                            if e in moster_7 or e in moster_2:
                                                index+=150
                                            elif e in moster_5 or e in moster_6 or e in moster_4:
                                                index+=500
                                            else:
                                                index+=31

                                            e.active = False
                                            moster_die_sound.play()

                                else:#子弹死亡复位
                                    b.reset((ourrole.rect.right, ourrole.rect.top + ourrole.high // 2))
                            '''无敌光圈'''
                        elif switch_prop==2:
                            switch_speed = True
                            switch_pengzhung=False
                            screen.blit(ourrole.image_three,ourrole.rect)
                            score_4+=3
                            '''加速'''
                        elif switch_prop==3:
                            switch_pengzhung=False
                            screen.blit(ourrole.image_four, ourrole.rect)
                            switch_speed=False
                            score_4 += 3
                            '''加速效果实现'''
                        if switch_speed==False:
                            score_2 = max_speed
                            max_speed = delay
                            delay = score_2
                else:#角色死亡
                    ourrole.reset()
                    start=False
                #怪物，道具出现
                if score_1<2000:
                    delay_moster(mosters,bg_speed)
                elif score_1<6000:

                    delay_moster(porp_1, bg_speed)

                elif score_1<8000:

                    delay_moster(mosters, bg_speed)

                elif score_1<10000:

                    delay_moster(porp_1, bg_speed)


                else:
                    delay_moster(porp_1, bg_speed)



                if switch_suspend:#暂停相关
                    score+=1
                    score_1+=1
                # 时间计时器：设置图片帧数
                clock = pygame.time.Clock()
                clock.tick(200)  # 调速
                # 图片自动滚动相关
                if x<=10-size_width:
                    x=0
                    '''吃道具碰撞检测'''
                for en in ourroles:
                    enemies_down = pygame.sprite.spritecollide(en,porps, False, pygame.sprite.collide_mask)
                    if enemies_down:
                        for i in enemies_down:
                            if i.flash==1:#子弹道具
                                porp_sound_3.play()
                                switch_prop=1
                                score_4 = 0
                                prop_time = 0
                            elif i.flash==2:#无敌道具
                                porp_sound_1.play()
                                switch_prop=2
                                score_4 = 0
                                prop_time = 0
                            elif i.flash==3:#加速道具
                                porp_sound_2.play()
                                switch_prop=3
                                score_4 = 0
                                prop_time = 0
                            i.active = False
                            index += 50#积分
                            '''角色碰撞怪物检测'''
                for en in ourroles:
                    enemies_down = pygame.sprite.spritecollide(en, mosters, False, pygame.sprite.collide_mask)
                    if enemies_down:
                        if switch_pengzhung:
                            role_die_sound.play()
                            en.active = False
                        for i in enemies_down:
                            index += 150
                            moster_die_sound.play()
                            i.active = False
                            '''键盘控制'''
                for event in pygame.event.get():  # 检测是否是退出时间
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == KEYDOWN:
                        if switch_trun==False:
                            if event.key == K_UP:

                                speed = [0, -3]
                                switch_trun = True#图片反转
                                ourrole.image_one = pygame.transform.flip(ourrole.image_one, False, True)
                                ourrole.image_two = pygame.transform.flip(ourrole.image_two, False, True)
                        if switch_trun==True:
                            if event.key == K_DOWN:
                                speed = [0, 3]
                                switch_trun = False
                                ourrole.image_one = pygame.transform.flip(ourrole.image_one, False, True)
                                ourrole.image_two = pygame.transform.flip(ourrole.image_two, False, True)
                        if event.key==K_SPACE:#暂停
                            switch_suspend=not switch_suspend
                            score_2=score_1
                            score_1 = score_3
                            score_3=score_2
                # 移动图像
                ourrole.rect = ourrole.rect.move(speed)
                if ourrole.rect.top <=-20:
                    speed=[0,0]
                    ourrole.rect.top=-20
                elif ourrole.rect.bottom>=370:
                    speed = [0, 0]
                    ourrole.rect.bottom=370
        pygame.display.flip()


if __name__ == '__main__':
    main()
