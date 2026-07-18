import pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event – Change Sprite Colour")

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self, new_color):
        self.image.fill(new_color)

# Create two sprites
sprite1 = Sprite((255, 0, 0), 200, 200)   # Red
sprite2 = Sprite((0, 0, 255), 400, 200)   # Blue

all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Custom event ID
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Trigger the event every 2 seconds
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event: change both sprite colours
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color((0, 255, 0))   # Green
            sprite2.change_color((255, 255, 0)) # Yellow

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
