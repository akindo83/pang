import pygame

pygame.init()

player_group = pygame.sprite.RenderUpdates()
missile_group = pygame.sprite.RenderUpdates()
ball_group = pygame.sprite.RenderUpdates()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("팡팡")

clock = pygame.time.Clock();


is_playing = True

while is_playing :
    for event in pygame.event.get() :
        if event.type in (pygame.QUIT, pygame.KEYDOWN) :
            is_playing = False

    #screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
