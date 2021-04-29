import pygame
import os

pygame.font.init()

FPS = 10
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RockPaperScissors")

def main():
    clock = pygame.time.Clock()
    run = True
    front_page = True
    wins = [0, 0]
    Numofplayers = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        clock.tick(FPS)
        
    

if __name__ == '__main__':
    main()