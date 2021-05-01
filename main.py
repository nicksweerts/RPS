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
GREY = (128, 128, 128)
DARK_BLUE = (0, 0, 139)
LIGHT_RED = (255, 51, 51)
TITLE_FONT = pygame.font.SysFont('calibri', 80)
CHOICE_FONT = pygame.font.SysFont('ariel', 70)
SINGLE_FONT = pygame.font.SysFont('ariel', 100)
WIN_SCREEN_FONT = pygame.font.SysFont('calibri', 50)

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


def draw_singleplayer(wins):
    WIN.fill(WHITE)
    rect1 = (50, 50, WIDTH - 100, HEIGHT - 100)
    pygame.draw.rect(WIN, BLACK, rect1)

    rect2 = (75, 75, WIDTH - 150, HEIGHT - 150)
    pygame.draw.rect(WIN, WHITE, rect2)

    top_text = "CHOOSE YOUR ATTACK"
    draw_text = CHOICE_FONT.render(top_text, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,0))

    box_text = "Your Choices:"
    c1_text = "z = ROCK"
    c2_text = "x = PAPER"
    c3_text = "c = SCISSORS"

    draw_text1 = SINGLE_FONT.render(box_text, 1, DARK_BLUE)
    draw_text2 = SINGLE_FONT.render(c1_text, 1, GREY)
    draw_text3 = SINGLE_FONT.render(c2_text, 1, BLUE)
    draw_text4 = SINGLE_FONT.render(c3_text, 1, LIGHT_RED)

    WIN.blit(draw_text1, (WIDTH//2 - draw_text1.get_width()//2, 90))
    WIN.blit(draw_text2, (WIDTH//2 - draw_text2.get_width()//2, 180))
    WIN.blit(draw_text3, (WIDTH//2 - draw_text3.get_width()//2, 270))
    WIN.blit(draw_text4, (WIDTH//2 - draw_text4.get_width()//2, 360))

    wins_text1 = "Wins: " + str(wins[0])
    wins_text2 = "Wins: " + str(wins[1])
    draw_wins1 = CHOICE_FONT.render(wins_text1, 1, BLACK)
    draw_wins2 = CHOICE_FONT.render(wins_text2, 1, BLACK)
    WIN.blit(draw_wins1, (80, HEIGHT - 150))
    WIN.blit(draw_wins2, (WIDTH - 80 - draw_wins2.get_width(), HEIGHT - 150))

def single_key(key_pressed):
    if key_pressed[pygame.K_z]:
        return "rock"
    elif key_pressed[pygame.K_x]:
        return "paper"
    elif key_pressed[pygame.K_c]:
        return "scissors"
    else:
        return "none"

    


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

def draw_p1_choice(p1_choice):
    text = "Player One chose:"
    draw_text = WIN_SCREEN_FONT.render(text, 1, RED)
    draw_text1 = WIN_SCREEN_FONT.render(p1_choice, 1, RED)
    WIN.blit(draw_text, (WIDTH//3 - draw_text.get_width()//2, 150))
    WIN.blit(draw_text1, (WIDTH//3 - draw_text1.get_width()//2, HEIGHT//2))

def draw_p2_choice(p2_choice):
    text = "Player Two chose:"
    draw_text = WIN_SCREEN_FONT.render(text, 1, BLUE)
    draw_text1 = WIN_SCREEN_FONT.render(p2_choice, 1, BLUE)
    WIN.blit(draw_text, ((2 * WIDTH//3) - draw_text.get_width()//2, 150))
    WIN.blit(draw_text1, ((2 * WIDTH//3) - draw_text1.get_width()//2, HEIGHT//2))

def draw_winner_text(winner):
    text = "Tie"
    if winner == 1:
        text = "P1 Wins"
    elif winner == 2:
        text = "P2 Wins"
    draw_text = TITLE_FONT.render(text, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))

def cont_click(pos):
    if ((pos[1] <= ((5 * HEIGHT//9) + 80 + WIDTH//5)) and (pos[1] >= (5 * HEIGHT//9) + 80)):
        if ((pos[0] <= ((2 * WIDTH//10) - 40 + WIDTH//5)) and (pos[0] >= (2 * WIDTH//10 - 40))):
            return 1
        elif ((pos[0] <= ((6 * WIDTH//10) + 45 + WIDTH//5)) and (pos[0] >= (6 * WIDTH//10 + 45))):
            return 2
        else:
            return 0
    else:
        return 0


def draw_continue(wins):
    show = 0
    while show == 0:
        WIN.fill(WHITE)
        rect1 = (50, 50, WIDTH - 100, HEIGHT - 100)
        pygame.draw.rect(WIN, BLACK, rect1)

        rect2 = (75, 75, WIDTH - 150, HEIGHT - 150)
        pygame.draw.rect(WIN, WHITE, rect2)

        text = "Continue?"
        draw_text = TITLE_FONT.render(text, 1, RED)
        WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))

        rect_yes = ((2 * WIDTH//10) - 40, (5 * HEIGHT//9) + 80, WIDTH//5, WIDTH//5)
        pygame.draw.rect(WIN, BLACK, rect_yes)
        text1 = "Yes"
        draw_text1 = CHOICE_FONT.render(text1, 1, RED)
        WIN.blit(draw_text1, (WIDTH//4 - draw_text1.get_width()//2, HEIGHT - 225))


        rect_no = ((6 * WIDTH//10) + 45, (5 * HEIGHT//9) + 80, WIDTH//5, WIDTH//5)
        pygame.draw.rect(WIN, BLACK, rect_no)

        text2 = "No"
        draw_text2 = CHOICE_FONT.render(text2, 1, RED)
        WIN.blit(draw_text2, ((3 * WIDTH//4) - draw_text2.get_width()//2, HEIGHT - 225))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    show = cont_click(pos)
                    if show != 0:
                        if show == 1:
                            return True
                        else:
                            return False

        wins_text1 = "Wins: " + str(wins[0])
        wins_text2 = "Wins: " + str(wins[1])
        draw_wins1 = WIN_SCREEN_FONT.render(wins_text1, 1, BLACK)
        draw_wins2 = WIN_SCREEN_FONT.render(wins_text2, 1, BLACK)
        WIN.blit(draw_wins1, (80, 75))
        WIN.blit(draw_wins2, (WIDTH - 80 - draw_wins2.get_width(), 75))

        pygame.display.update()


def screen_init():
    WIN.fill(WHITE)
    rect1 = (50, 50, WIDTH - 100, HEIGHT - 100)
    pygame.draw.rect(WIN, BLACK, rect1)

    rect2 = (75, 75, WIDTH - 150, HEIGHT - 150)
    pygame.draw.rect(WIN, WHITE, rect2)


def choose_wins(wins, p1_choice, p2_choice):
    winner = win_check(p1_choice, p2_choice)
    screen_init()
    
    if winner == 1:
        wins[0] += 1
    elif winner == 2:
        wins[1] += 1

    draw_p1_choice(p1_choice)
    pygame.display.update()
    pygame.time.delay(2000)

    screen_init()
    draw_p2_choice(p2_choice)
    pygame.display.update()
    pygame.time.delay(2000)

    screen_init()
    draw_winner_text(winner)
    pygame.display.update()
    pygame.time.delay(2000)

    return draw_continue(wins)


def draw_multiplayer(wins):
    WIN.fill(WHITE)
    rect1 = (50, 50, WIDTH - 100, HEIGHT - 100)
    pygame.draw.rect(WIN, BLACK, rect1)

    rect2 = (75, 75, WIDTH - 150, HEIGHT - 150)
    pygame.draw.rect(WIN, WHITE, rect2)

    top_text = "CHOOSE YOUR ATTACK"
    draw_text = CHOICE_FONT.render(top_text, 1, RED)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2,0))

def multi_key(key_pressed, p1_choice, p2_choice):
    if (key_pressed[pygame.K_COMMA] or key_pressed[pygame.K_PERIOD] or key_pressed[pygame.K_SLASH]):
        return 2
    elif (key_pressed[pygame.K_z] or key_pressed[pygame.K_x] or key_pressed[pygame.K_c]):
        return 1
    else:
        return 0


def second_key(key_pressed):
    if key_pressed[pygame.K_COMMA]:
        return "rock"
    elif key_pressed[pygame.K_PERIOD]:
        return "paper"
    elif key_pressed[pygame.K_SLASH]:
        return "scissors"
    else:
        return "none"


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
        player_choice = False
        will_continue = True
        while run:
            draw_singleplayer(wins)
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  run = False
                  pygame.quit()

            keys_pressed = pygame.key.get_pressed()
            p1_choice = single_key(keys_pressed)

            if p1_choice != "none":
                will_continue = choose_wins(wins, p1_choice, p2_choice)
                if will_continue:
                    p1_choice = "none"
                    p2_choice = bot_choice()
                    player_choice = False
                else:
                    run = False
                    break

            clock.tick(FPS)
            pygame.display.update()
    elif numofplayers == 2:
        will_continue = True
        player_choice = 0
        while run:
            draw_multiplayer(wins)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            
            keys_pressed = pygame.key.get_pressed()
            player_choice = multi_key(keys_pressed, p1_choice, p2_choice)

            if (player_choice == 1 and p1_choice == "none"):
                p1_choice = single_key(keys_pressed)
            elif (player_choice == 2 and p2_choice == "none"):
                p2_choice = second_key(keys_pressed)
            
            if (p1_choice != "none" and p2_choice != "none"):
                will_continue = choose_wins(wins, p1_choice, p2_choice)
                if will_continue:
                    p1_choice = "none"
                    p2_choice = "none"
                    player_choice = 0
                else:
                    run = False
                    break
        
            clock.tick(FPS)
            pygame.display.update()

    

if __name__ == '__main__':
    main()