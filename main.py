import pygame
import os
import random

pygame.font.init()

FPS = 10
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RockPaperScissors")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 32, 255)
TITLE_FONT = pygame.font.SysFont('calibri', 70)
CHOICE_FONT = pygame.font.SysFont('ariel', 70)

ROCK = 1
PAPER = 2
SCISSORS = 3

def show_front():
    WIN.fill(WHITE)
    title_text = "Rock Paper Scissors!"
    draw_text1 = TITLE_FONT.render(title_text, 1, BLUE)
    WIN.blit(draw_text1, (WIDTH//2 - draw_text1.get_width()//2,
    HEIGHT//3 - draw_text1.get_height()//2))

    rect_1p = ((2 * WIDTH//10), (5 * HEIGHT//9) + 10, WIDTH//5, WIDTH//5)
    pygame.draw.rect(WIN, BLACK, rect_1p)

    choice1_text = "1P"
    draw_text2 = CHOICE_FONT.render(choice1_text, 1, RED)
    WIN.blit(draw_text2, ((3 * WIDTH//10) - draw_text2.get_width()//2,
    (2 * HEIGHT//3) - draw_text2.get_height()//2))


    rect_2p = ((6 * WIDTH//10), (5 * HEIGHT//9) + 10, WIDTH//5, WIDTH//5)
    pygame.draw.rect(WIN, BLACK, rect_2p)

    choice2_text = "2P"
    draw_text3 = CHOICE_FONT.render(choice2_text, 1, RED)
    WIN.blit(draw_text3, ((7 * WIDTH//10) - draw_text3.get_width()//2,
    (2 * HEIGHT//3) - draw_text3.get_height()//2))


     
    pygame.display.update()


def front_click(pos):
    if ((pos[1] <= ((5 * HEIGHT//9) + 10 + WIDTH//5)) and (pos[1] >= (5 * HEIGHT//9) + 10)):
        if ((pos[0] <= ((2 * WIDTH//10) + WIDTH//5)) and (pos[0] >= (2 * WIDTH//10))):
            return 1
        elif ((pos[0] <= ((6 * WIDTH//10) + WIDTH//5)) and (pos[0] >= (6 * WIDTH//10))):
            return 2
        else:
            return 0
    else:
        return 0

def bot_choice():
    num = random.randint(1,3)
    if num == ROCK:
        return "rock"
    elif num == PAPER:
        return "paper"
    else:
        return "scissors"


def draw_singleplayer():
    WIN.fill(BLACK)


def win_check(p1, p2):
    if (p1 == "rock"):
        if (p2 == "rock"):
            return 0
        elif (p2 == "paper"):
            return 2
        else:
            return 1
    elif (p1 == "paper"):
        if (p2 == "rock"):
            return 1
        elif (p2 == "paper"):
            return 0
        else:
            return 2
    else:
        if (p2 == "rock"):
            return 2
        elif (p2 == "paper"):
            return 1
        else:
            return 0



def main():
    clock = pygame.time.Clock()
    run = True
    front_page = True
    wins = [0, 0]
    numofplayers = 0
    p1_choice = "none"
    p2_choice = "none"

    while front_page:
        clock.tick(FPS)
        show_front()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                front_page = False
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                numofplayers = front_click(pos)
                if numofplayers != 0:
                    front_page = False

    if numofplayers == 1:
        p2_choice = bot_choice()
        while run:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  run = False
                  pygame.quit()

            clock.tick(FPS)
            draw_singleplayer()
            pygame.display.update()
    else:
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        
            clock.tick(FPS)
            WIN.fill(BLUE)
            pygame.display.update()

    

if __name__ == '__main__':
    main()