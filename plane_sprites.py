import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
SCREEN_RATE = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT  # 创建事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):   # 继承的父类不是object,所以必须调用父类的初始化方法

        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    def __init__(self):
        # 调用父类方法，创建敌机，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类的方法，保持垂直方向的飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组删除...")
            self.kill()

    def __del__(self):
        # print("敌机内存回收 %s" % self.rect)
        pass


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)    # 指定英雄的初始速度为0
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # self.bullets = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()      # 创建子弹精灵 空的组

    def update(self):
        #  水平方向上移动
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):

            # 创建子弹精灵
            bullet = Bullet()
            # 设置子弹的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将子弹精灵添加到精灵组
            self.bullets_group.add(bullet)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)
        if self.rect.bottom < 0:
            self.kill()

    def update(self):
        super().update()

    def __del__(self):
        # print("子弹被销毁...")
        pass
