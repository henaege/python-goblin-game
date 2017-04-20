# include pygame, which we got from pip
import pygame

# inorder to run pygame we have to run the init method
pygame.init()

# create a screen with a size
screen = {
    "height": 512,
    "width": 480
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

# create game loop
game_on = True
while game_on:
    # main game loop will run as long as game_on is true
    for event in pygame.event.get():
        # looping through all events that happen this game loop cycle
        if event.type == pygame.QUIT:
            # add a quit event (requires sys)
            # user clicked on red X to leave game
            game_on = False
            # update boolean so pygame can escape


