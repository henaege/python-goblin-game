# 1. include pygame, which we got from pip
import pygame
# import math for collision detection
from math import fabs
# get the random module
from random import randint

# 2. in order to run pygame we have to run the init method
pygame.init()

# 3. create a screen with a size
screen = {
    "height": 512,
    "width": 480
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down": 274
}

hero = {
    "x": 50,
    "y": 50,
    "speed": 10,
    "wins": 0
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down": False
}

goblin = {
    "x": 350,
    "y": 300,
    "speed": 10
}
screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

background_image = pygame.image.load('images/dungeon1.png')
hero_image = pygame.image.load('images/warrior3.png')
hero_image_scaled = pygame.transform.scale(hero_image, (50, 80))
goblin_image = pygame.image.load('images/beholder.png')
goblin_image_scaled = pygame.transform.scale(goblin_image, (60, 60))

# ///////////////////// MAIN GAME LOOP ///////////////////

# 4. create game loop
game_on = True
while game_on:
    # main game loop will run as long as game_on is true
    # EVENTS!
    for event in pygame.event.get():
        # looping through all events that happen this game loop cycle
        # 5. add a quit event (requires sys)
        if event.type == pygame.QUIT:
            # user clicked on red X to leave game
            game_on = False
            # update boolean so pygame can escape
        elif event.type == pygame.KEYDOWN:
            if event.key == keys["up"]:
                print("User pressed up")
                keys_down["up"] = True
            elif event.key == keys["down"]:
                print("User pressed down")
                keys_down["down"] = True
            elif event.key == keys["left"]:
                print("User pressed left")
                keys_down["left"] = True
            elif event.key == keys["right"]:
                print("User pressed right")
                keys_down["right"] = True
        elif event.type == pygame.KEYUP:
            print "The user let go of the key"
            if event.key == keys["up"]:
                keys_down["up"] = False
            if event.key == keys["down"]:
                keys_down["down"] = False
            if event.key == keys["left"]:
                keys_down["left"] = False
            if event.key == keys["right"]:
                keys_down["right"] = False
   
    if keys_down["up"]:
        hero["y"] -= hero["speed"]
    elif keys_down["down"]:
        hero["y"] += hero["speed"]
    elif keys_down["left"]:
        hero["x"] -= hero["speed"]
    elif keys_down["right"]:
        hero["x"] += hero["speed"]    

        # COLLISION DETECTION
    distance_between = fabs(hero["x"] - goblin["x"]) + fabs(hero["y"] - goblin["y"])
    distance_from_wall = fabs(hero["x"] - screen["width"]) + fabs(hero["y"] - screen["height"])
    if distance_between < 50:
        # generate a random x greater than 0 and less than screen width
        rand_x = randint(0, screen["width"]-50)
        rand_y = randint(0, screen["height"]-100)
        goblin["x"] = rand_x
        goblin["y"] = rand_y

        hero["wins"] += 1
    if distance_from_wall < 50:
        hero["x"] = hero["x"]
        hero["y"] = hero["y"]

    # RENDER!
    # 6. Screen.fill (background_color)
    pygame_screen.blit(background_image, [0, 0])

    # draw the hero's wins on the screen'
    font = pygame.font.Font(None, 25)
    wins_text = font.render("Wins: %d " % (hero["wins"]), True, (0,0,0))
    pygame_screen.blit(wins_text, [40, 40])
    # dare the hero
    pygame_screen.blit(hero_image_scaled, [hero["x"], hero["y"]])
    pygame_screen.blit(goblin_image_scaled, [goblin["x"], goblin["y"]])
    
    # 7. clear the screen for next time (flip the screen) - the image gets drawn in every loop
    pygame.display.flip()


