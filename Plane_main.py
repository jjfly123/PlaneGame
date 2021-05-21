import random
import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprite()

        pygame.init()   # 加一条初始化，不加初始化代码运行不了
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)  # 隔1000ms创建一架敌机
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprite(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)  # 创建背景精灵组

        self.enemy_group = pygame.sprite.Group()     # 创建敌机精灵组

        self.hero = Hero()      # 创建英雄飞机
        self.hero_group = pygame.sprite.Group(self.hero)       # 创建英雄组

    def start_game(self):
        print("游戏开始...")
        while True:
            self.clock.tick(SCREEN_RATE)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:  # 判断事件类型是不是之前的事件常量
                print("敌机出场...")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_RIGHT]:        # 使用键盘模块移动，可以按住方向键不动连续移动，第一种必须抬起键盘才行
                # print("向右移动...")
                self.hero.speed = 5
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -5
            else:
                self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets_group, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()   # 更新背景组
        self.back_group.draw(self.screen)  # 这句是把背景组绘制在括号里的内容上

        self.enemy_group.update()    # 更新敌机组
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets_group.update()      # 这里的hero是已经实例化的Hero类
        self.hero.bullets_group.draw(self.screen)

    @classmethod
    def __game_over(cls):
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    game = PlaneGame()
    game.start_game()

