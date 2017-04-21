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
    "kills": 0,
    "health": 60
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
    "speed": 10,
    'direction': 1
}

monster = {
    'x': 300,
    'y': 50,
    'speed': 50,
    'direction': 2
}

rand_x = randint(0, screen["width"]-50)
rand_y = randint(0, screen["height"]-200)
health_boost = {
    'x': rand_x,
    'y': rand_y,
    'speed': 5,
    'direction': 1
}


screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")

background_image = pygame.image.load('images/dungeon1.png')
hero_image = pygame.image.load('images/warrior3.png')
hero_image_scaled = pygame.transform.scale(hero_image, (50, 80))
goblin_image = pygame.image.load('images/beholder.png')
goblin_image_scaled = pygame.transform.scale(goblin_image, (60, 60))
monster_image = pygame.image.load('images/dragon.png')
health_boost_image = pygame.image.load('./images/heart.png')

# ADD MUSIC
pygame.mixer.music.load('./sounds/culex.wav')
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('./sounds/orc_die.ogg')
lose_sound = pygame.mixer.Sound('./sounds/hits/6.ogg')
heal_sound = pygame.mixer.Sound('./sounds/heal.wav')

# ///////////////////// MAIN GAME LOOP ///////////////////

# 4. create game loop
loop_count = 0
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
        # elif hero["health"] <= 0:
        #     lose_font = pygame.font.Font(None, 80)
        #     loss_text = font.render("Wins: %d " % (hero["wins"]), True, (0,0,0))
        #     pygame_screen.blit(loss_text, [200, 250])
            # game_on = False

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

    # Monster Movement
    if loop_count % 50 == 0:
        goblin['direction'] = randint(1,4)
    
    if loop_count % 20 == 0:
        monster['direction'] = randint(1,4)
    

    if hero['health'] <= 30:
        pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])
        if loop_count % 30 == 0:
            health_boost['speed'] = 10
            health_boost['direction'] = randint(1,4)
    loop_count += 1

    if keys_down["up"]:
        if hero["y"] > 20:
            hero["y"] -= hero["speed"]
    elif keys_down["down"]:
        if hero["y"] < screen["height"] - 200:
            hero["y"] += hero["speed"]
    elif keys_down["left"]:
        if hero["x"] > 20:
            hero["x"] -= hero["speed"]
    elif keys_down["right"]:
        if hero["x"] < screen["width"] - 50:
            hero["x"] += hero["speed"]    

        # COLLISION DETECTION
    distance_between = fabs(hero["x"] - goblin["x"]) + fabs(hero["y"] - goblin["y"])
    distance_from_monster = fabs(hero["x"] - monster['x']) + fabs(hero["y"] - monster['y'])
    distance_from_wall = fabs(hero["x"] - screen["width"]) + fabs(hero["y"] - screen["height"])
    distance_from_health = fabs(hero['x'] - health_boost['x']) + fabs(hero['y'] - health_boost['y'])
    if distance_between < 50:
        # generate a random x greater than 0 and less than screen width
        rand_x = randint(0, screen["width"]-50)
        rand_y = randint(0, screen["height"]-200)
        goblin["x"] = rand_x
        goblin["y"] = rand_y
        hero["kills"] += 1
        win_sound.play()
    elif loop_count % 10 == 0:
        if goblin['direction'] == 1:
            if goblin["y"] > 20:
                goblin["y"] -= goblin["speed"]
        elif goblin['direction'] == 2:
            if goblin["y"] < screen["height"] - 200:
                goblin["y"] += goblin["speed"]
        elif goblin['direction'] == 3:
            if goblin["x"] > 20:
                goblin["x"] -= goblin["speed"]
        elif goblin['direction'] == 4:
            if goblin["x"] < screen["width"] - 50:
                goblin["x"] += goblin["speed"]
        if monster['direction'] == 1:
            if monster["y"] > 20:
                monster["y"] -= monster["speed"]
        elif monster['direction'] == 2:
            if monster["y"] < screen["height"] - 200:
                monster["y"] += monster["speed"]
        elif monster['direction'] == 3:
            if monster["x"] > 20:
                monster["x"] -= monster["speed"]
        elif monster['direction'] == 4:
            if monster["x"] < screen["width"] - 200:
                monster["x"] += monster["speed"]
        if health_boost['direction'] == 1:
            if health_boost["y"] > 20:
                health_boost["y"] -= health_boost["speed"]
        elif health_boost['direction'] == 2:
            if health_boost["y"] < screen["height"] - 200:
                health_boost["y"] += health_boost["speed"]
        elif health_boost['direction'] == 3:
            if health_boost["x"] > 20:
                health_boost["x"] -= health_boost["speed"]
        elif health_boost['direction'] == 4:
            if health_boost["x"] < screen["width"] - 200:
                health_boost["x"] += health_boost["speed"]
    
    if distance_from_health < 50:
        hero['health'] += 30
        heal_sound.play()
        health_boost['x'] = 550
        health_boost['y'] = 500
        health_boost['speed'] = 0
    
    if distance_from_monster < 75:
        rand_x = randint(0, screen["width"]-50)
        rand_y = randint(0, screen["height"]-100)
        lose_sound.play()
        hero["x"] = rand_x
        hero["y"] = rand_y
        hero["health"] -= 10
       
       
    # random_motion(goblin["x"], goblin["y"])
    # RENDER!
    # 6. Screen.fill (background_color)
    pygame_screen.blit(background_image, [0, 0])

    # draw the hero's wins on the screen'
    kill_font = pygame.font.Font(None, 40)
    kill_text = kill_font.render("Kills: %d " % (hero["kills"]), True, (241,43,36))
    pygame_screen.blit(kill_text, [40, 40])

    health_font = pygame.font.Font(None, 40)
    health_text = health_font.render("Health: %d " % (hero["health"]), True, (44,136,145))
    pygame_screen.blit(health_text, [340, 40])
    # draw the hero
    pygame_screen.blit(hero_image_scaled, [hero["x"], hero["y"]])
    pygame_screen.blit(goblin_image_scaled, [goblin["x"], goblin["y"]])
    pygame_screen.blit(monster_image, [monster['x'], monster['y']])
    pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])

    
    # 7. clear the screen for next time (flip the screen) - the image gets drawn in every loop
    pygame.display.flip()
    

