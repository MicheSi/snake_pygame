import pygame
import time

pygame.init()

# initialize color variables
blue = (0, 0, 255)
red = (255, 0, 0)

# creates screen using pygame
display_width = 600
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

# default start spot
x1 = display_width/2
y1 = display_height/2

block = 10

# coordinates on change
x1_change = 0
y1_change = 0

# creates loop to run game
game_over = False

clock = pygame.time.Clock()
speed = 20

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    display_msg = font_style.render(msg, True, color)
    game_display.blit(display_msg, [display_width/2, display_height/2])

while not game_over:
    for event in pygame.event.get():
        # allows user to close game
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

    if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
        game_over = True

    # move snake
    x1 += x1_change
    y1 += y1_change

    # draw rectangles
    pygame.draw.rect(game_display, blue, [x1, y1, block, block])
    pygame.display.update()

    clock.tick(speed)
    
message('Game over', red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()