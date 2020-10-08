import pygame

pygame.init()

# creates screen using pygame
game_display = pygame.display.set_mode((600, 600))
pygame.display.update()
pygame.display.set_caption('Snake')

# initialize color variables
blue = (0, 0, 255)
red = (255, 0, 0)

# creates loop to run game
game_over = False
while not game_over:
    for event in pygame.event.get():
        # allows user to close game
        if event.type == pygame.QUIT:
            game_over = True

    # draw rectangles
    pygame.draw.rect(game_display, blue, [200, 150, 10, 10])
    pygame.display.update()

pygame.quit()
quit()