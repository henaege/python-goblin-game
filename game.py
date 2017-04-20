# 1. include pygame, which we got from pip
import pygame

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
    "x": 100,
    "y": 100,
    "speed": 10
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down": False
}
screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')

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
    # RENDER!
    # 6. Screen.fill (background_color)
    pygame_screen.blit(background_image, [0, 0])

    # dare the hero
    pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
    # 7. clear the screen for next time (flip the screen) - the image gets drawn in every loop
    pygame.display.flip()


