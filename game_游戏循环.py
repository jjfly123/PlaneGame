import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")

screen.blit(bg, (0, 0))


hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

clock = pygame.time.Clock()
hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)

    hero_rect.y -= 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("GAME OVER...")
            pygame.quit()
            exit()

    # event_list = pygame.event.get()
    #
    # if len(event_list) > 0:
    #     print(event_list)

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()
    pass

pygame.quit()