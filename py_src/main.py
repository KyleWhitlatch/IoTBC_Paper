from iot_sim import iot
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_SPACE

pygame.init()
clock = pygame.time.Clock()


SC_W = 1920
SC_H = 1080

sc = pygame.display.set_mode((SC_W, SC_H))
TICK = pygame.USEREVENT + 1




# surf_iot = pygame.Surface((25, 25))
# surf_iot.fill((0, 0, 0))
#
# rect = surf_iot.get_rect()
#
# surf_center = (
#     (SC_W-surf_iot.get_width())/2,
#     (SC_H-surf_iot.get_height())/2
# )

iot_group = pygame.sprite.Group()
edge_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for x in range(100):
    iot_group.add(iot())


live = True

while live:
    for e in pygame.event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                live = False
        elif e.type == QUIT:
            live = False

    sc.fill((112, 234, 250))
    sc.blit(surf_iot, surf_center)
    pygame.display.flip()
    clock.tick(1)



