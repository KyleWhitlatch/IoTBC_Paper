import pygame


class edge_device(pygame.sprite.Sprite):
    def __init__(self, eid):
        super(edge_device, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.id = eid







