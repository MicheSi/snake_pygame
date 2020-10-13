import pygame
import time
import random

pygame.init()

# initialize color variables
white = (255, 255, 255)
black = (0, 0, 0)
blue = (30, 144, 255)
red = (255, 0, 0)
green = (50, 205, 50)

# creates screen using pygame
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

# size of block
block = 10

font_style = pygame.font.SysFont('arial', 30)
score_font = pygame.font.SysFont('bahnschrift', 20)

# renders score
def myScore(score):
    value = score_font.render('Score: ' + str(score), True, blue)
    game_display.blit(value, [0, 0])

# renders snake blocks
def mySnake(block, snake_list):
    for b in snake_list:
        pygame.draw.rect(game_display, green, [b[0], b[1], block, block])

# renders game over message
def message(msg, color):
    display_msg = font_style.render(msg, True, color)
    game_display.blit(display_msg, [display_width/6, display_height/3])

# creates loop to run game
def gameLoop():
    game_over = False
    game_close = False

    # default start spot
    x1 = display_width/2
    y1 = display_height/2

    # coordinates on change
    x1_change = 0
    y1_change = 0

    # initialize the snake with just a head
    snake_list = []
    snake_length = 1

    # default speed of snake
    speed = 10

    # coordinates of apple
    appleX = round(random.randrange(0, display_width - block)  / 10.0) * 10
    appleY = round(random.randrange(0, display_height - block) / 10.0) * 10

    while not game_over:
        while game_close == True:
            message('Game Over! Press Q to Quit or C to Play Again', white)
            myScore(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        # game over if snake runs into itself or walls
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # move snake
        x1 += x1_change
        y1 += y1_change

        # draw snake and apple
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [appleX, appleY, block, block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for b in snake_list[:-1]:
            if b == snake_head:
                game_close = True
        
        # increase speed of snake
        if snake_length == 11:
            speed = 15
        if snake_length == 21:
            speed = 20
        if snake_length == 31:
            speed = 25
        if snake_length == 41:
            speed = 30

        mySnake(block, snake_list)
        myScore(snake_length - 1)

        pygame.display.update()

        # moves apple to new random spot when eaten and adds block to snake
        if x1 == appleX and y1 == appleY:
            appleX = round(random.randrange(0, display_width - block) / 10) * 10
            appleY = round(random.randrange(0, display_height - block) / 10) * 10
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()