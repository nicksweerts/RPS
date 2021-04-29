import pygame
import os

pygame.font.init()

FPS = 10
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RockPaperScissors")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
TITLE_FONT = pygame.font.SysFont('calibri', 70)
CHOICE_FONT = pygame.font.SysFont('ariel', 70)

def draw_front():
    WIN.fill(WHITE)
    title_text = "Rock Paper Scissors!"
    draw_text1 = TITLE_FONT.render(title_text, 1, BLACK)
    WIN.blit(draw_text1, (WIDTH//2 - draw_text1.get_width()//2,
    HEIGHT//3 - draw_text1.get_height()//2))

    choice1_text = "1P"
    draw_text2 = CHOICE_FONT.render(choice1_text, 1, RED)
    WIN.blit(draw_text2, ((3 * WIDTH//10) - draw_text2.get_width()//2,
    (2 * HEIGHT//3) - draw_text2.get_height()//2))

    choice2_text = "2P"
    draw_text3 = CHOICE_FONT.render(choice2_text, 1, RED)
    WIN.blit(draw_text3, ((7 * WIDTH//10) - draw_text3.get_width()//2,
    (2 * HEIGHT//3) - draw_text3.get_height()//2))

     
    pygame.display.update()

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
        if front_page:
            draw_front()

    

if __name__ == '__main__':
    main()