import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turbo Titans")

BLUE = (0, 150, 255)

FPS = 60


Ferrari = pygame.image.load(
    os.path.join('Ferrari_car.png'))
ROAD = pygame.image.load(
    os.path.join('road.jpg'))
ROAD = pygame.transform.scale(ROAD, (900, 500))




def draw_window():
    WIN.blit(ROAD, (0, 0))
    WIN.blit(Ferrari, (450, 250))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()