import pygame

pygame.init()

# initialize color variables
blue = (0, 0, 255)
red = (255, 0, 0)

# creates screen using pygame
game_display = pygame.display.set_mode((600, 600))
pygame.display.update()
pygame.display.set_caption('Snake')

# default start spot
x1 = 300
y1 = 300

# coordinates on change
x1_change = 0
y1_change = 0

# creates loop to run game
game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        # allows user to close game
        if event.type == pygame.QUIT:
            game_over = True
        # key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    # move snake
    x1 += x1_change
    y1 += y1_change

    # draw rectangles
    pygame.draw.rect(game_display, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)
    
pygame.quit()
quit()