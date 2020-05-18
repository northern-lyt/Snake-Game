import random
import time
import pygame

pygame.init()
clock = pygame.time.Clock()
orangecolor = (255, 123, 7)
blackcolor = (0, 0, 0)
redcolor = (255, 255, 255)
greencolor = (0, 204, 102)
bluecolor = (0, 0, 51)
yellowcolor = (255, 128, 0)
pinkcolor = (255, 51, 51)

display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15
snake_list = []


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, greencolor, [x[0], x[1], snake_block, snake_block])

def snakegame():
    game_over = False
    game_end = False

    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, display_height - snake_block) / 10) * 10


    while not game_over:
        while game_end == True:
            dis.fill(bluecolor)
            font_style = pygame.font.SysFont("comicsansms", 25)
            mesg = font_style.render("You lost...!!!!! Wanna play again? Press P", True, redcolor)
            dis.blit(mesg, [display_width / 8, display_height / 2.5])


            score = Length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms", 30)
            value = score_font.render("Your Score: " + str(score), True, pinkcolor)
            dis.blit(value, [display_width / 3, display_height / 5])
            font_style = pygame.font.SysFont("comicsansms", 20)
            nesg = font_style.render("Press backspace to go back to main menu", True, redcolor)
            dis.blit(nesg, [display_width / 16, display_height / 1.5])
            pygame.display.update()
            fp = open("sample.txt", "r")
            no = int(fp.readline())
            h = max(no, score)
            fp.close()
            fp = open("sample.txt", "w")
            fp.write(str(h))
            fp.close()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snakegame()
                    if event.key == pygame.K_BACKSPACE:
                            welcome()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_end = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis, yellowcolor, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_end = True
        snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, display_height - snake_block) / 10) * 10
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

def highscore():
    over = False
    dis.fill(bluecolor)
    fp = open("sample.txt", "r")
    no = int(fp.readline())
    fp.close()
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("1. THe HIGHEST SCORE IS: "+ str(no), True, redcolor)
    dis.blit(nesg, [display_width / 8, display_height / 3])
    font_style = pygame.font.SysFont("comicsansms", 20)
    nesg = font_style.render("Press backspace to go back to main menu", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 1.5])
    pygame.display.update()
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    welcome()
            if event.type == pygame.QUIT:
                over = True

def instruction():
    over = False
    dis.fill(bluecolor)
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("HOW TO PLAY GAME", True, redcolor)
    dis.blit(nesg, [display_width / 4, display_height / 8])
    font_style = pygame.font.SysFont("Arial", 15)
    nesg = font_style.render("You have to navigate the snake to get its food without touching the borders of the window screen.", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 4])
    font_style = pygame.font.SysFont("Arial", 15)
    nesg = font_style.render("Use arrow keys to help navigate the snake.", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 3.4])
    font_style = pygame.font.SysFont("Arial", 15)
    nesg = font_style.render("Use Up and DOWN arrow to move the snake upward and downward.", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height /2.9])
    font_style = pygame.font.SysFont("Arial", 15)
    nesg = font_style.render("Use the RIGHT and LEFT arrow key to move the snake right and left. ", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 2.6])
    font_style = pygame.font.SysFont("Arial", 15)
    nesg = font_style.render("When snakes east the food, it grows and when it touches the borders or itself it dies.", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 2.3])
    font_style = pygame.font.SysFont("comicsansms", 20)
    nesg = font_style.render("Press backspace to go back to main menu", True, redcolor)
    dis.blit(nesg, [display_width / 16, display_height / 1.5])
    pygame.display.update()
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    welcome()
            if event.type == pygame.QUIT:
                over = True

def welcome():
    screen_over = False
    dis.fill(bluecolor)
    font_style = pygame.font.SysFont("comicsansms", 32)
    nesg = font_style.render("WELCOME TO SNAKE GAME", True, pinkcolor)
    dis.blit(nesg, [display_width / 7, display_height / 15])
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("1. Play Game", True, redcolor)
    dis.blit(nesg, [display_width / 8, display_height / 4.5])
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("2. High Score", True, redcolor)
    dis.blit(nesg, [display_width / 8, display_height / 3])
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("3. Instruction", True, redcolor)
    dis.blit(nesg, [display_width / 8, display_height / 2.2])
    font_style = pygame.font.SysFont("comicsansms", 25)
    nesg = font_style.render("4. Quit", True, redcolor)
    dis.blit(nesg, [display_width / 8, display_height / 1.8])
    pygame.display.update()
    while not screen_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snakegame()
                if event.key == pygame.K_2:
                    highscore()
                if event.key == pygame.K_3:
                    instruction()
                if event.key == pygame.K_4:
                    quit()
            if event.type == pygame.QUIT:
                screen_over = True
welcome()
