import pygame
import sys

# Настройка Pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
AQUA = (0, 255, 255)
ORANGE = (255, 167, 29)


WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-Нолики")
screen.fill(WHITE)
font = pygame.font.Font(None, 40)
bg = pygame.image.load("bg.jpg")


def main():
    screen.blit(bg, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            x, y = pygame.mouse.get_pos()
            print("Mouse position: ({}, {})".format(x, y))
            print(pygame.MOUSEBUTTONDOWN)
        hello = font.render(f"Лучшие на свете", True, BLACK)
        hello1 = font.render(f'"КРЕСТИКИ-НОЛИКИ"!', True, BLACK)
        screen.blit(hello, (140, 30))
        screen.blit(hello1, (95, 60))
        pygame.draw.rect(screen, BLACK, pygame.Rect(100, 150, 300, 70))
        play = font.render(f"Играть", True, WHITE)
        screen.blit(play, (206, 172))
        pygame.draw.rect(screen, BLACK, pygame.Rect(100, 270, 300, 70))
        custom = font.render(f"Кастомизация", True, WHITE)
        screen.blit(custom, (153, 292))
        pygame.draw.rect(screen, BLACK, pygame.Rect(100, 390, 300, 70))
        custom = font.render(f"Статистика", True, WHITE)
        screen.blit(custom, (178, 412))
        pygame.display.flip()


if __name__ == "__main__":
    main()
