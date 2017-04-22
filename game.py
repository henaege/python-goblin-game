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
    "speed": 5,
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
    "speed": 3,
    'direction': 'N'
}

monster = {
    'x': 300,
    'y': 50,
    'speed': 10,
    'direction': 'SE',
    'damage': 10

}

rand_x = randint(0, screen["width"]-50)
rand_y = randint(0, screen["height"]-200)
health_boost = {
    'x': rand_x,
    'y': rand_y,
    'speed': 5,
    'direction': 'S',
    'amount': 30
}

directions = ['N','S','E','W','NE','NW','SE','SW']

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
kill_sound = pygame.mixer.Sound('./sounds/orc_die.ogg')
lose_sound = pygame.mixer.Sound('./sounds/hits/6.ogg')
heal_sound = pygame.mixer.Sound('./sounds/heal.wav')
win_sound = pygame.mixer.Sound('./sounds/victory.wav')
# ///////////////////// MAIN GAME LOOP ///////////////////

# 4. create game loop
loop_count = 0
game_on = True
game_paused = False
hero_won = False
level = 10
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
            elif event.key == 32:
				# user pushed space!
				game_paused = not game_paused
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
    if loop_count % 30 == 0:
        goblin_dir_index = randint(0, len(directions)-1)
        goblin['direction'] = directions[goblin_dir_index]
    
    if loop_count % 20 == 0:
        monster_dir_index = randint(0, len(directions)-1)
        monster['direction'] = directions[monster_dir_index]
    

    if hero['health'] <= 30:
        pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])
        if loop_count % 30 == 0:
            health_boost['speed'] = 3
            health_dir_index = randint(0, len(directions)-1)
            health_boost['direction'] = directions[health_dir_index]
    
    loop_count += 1
    if not game_paused and not hero_won:
        if keys_down["up"]:
            if hero["y"] > 20:
                hero["y"] -= hero["speed"]
        elif keys_down["down"]:
            if hero["y"] < screen["height"] - 200:
                hero["y"] += hero["speed"]
        if keys_down["left"]:
            if hero["x"] > 20:
                hero["x"] -= hero["speed"]
        elif keys_down["right"]:
            if hero["x"] < screen["width"] - 50:
                hero["x"] += hero["speed"]    

    if not game_paused and not hero_won:    # COLLISION DETECTION
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
            kill_sound.play()
        elif (goblin['direction'] == 'N'):
            if goblin['y'] > 20:
                goblin['y'] -= goblin['speed']
        elif (goblin['direction'] == 'S'):
            if goblin['y'] < screen["height"] - 200:
                goblin['y'] += goblin['speed']
        elif (goblin['direction'] == 'E'):
            if goblin['x'] < screen['width'] - 200:
                goblin['x'] += goblin['speed']
        elif (goblin['direction'] == 'W'):
            if goblin['x'] > 20:
                goblin['x'] -= goblin['speed']
        elif (goblin['direction'] == 'NE'):
            if goblin['y'] > 20 and goblin['x'] < screen['width'] - 200:
                goblin['y'] -= goblin['speed']
                goblin['x'] += goblin['speed']
        elif (goblin['direction'] == 'NW'):
            if goblin['y'] > 20 and goblin['x'] > 20:
                goblin['y'] -= goblin['speed']
                goblin['x'] -= goblin['speed']
        elif (goblin['direction'] == 'SE'):
            if goblin['y'] < screen["height"] - 200 and goblin['x'] < screen['width'] - 200:
                goblin['y'] += goblin['speed']
                goblin['x'] += goblin['speed']
        elif (goblin['direction'] == 'SW'):
            if goblin['y'] < screen["height"] - 200 and goblin['x'] > 20:
                goblin['y'] += goblin['speed']
                goblin['x'] -= goblin['speed']
        
        if distance_from_monster < 75:
            rand_x = randint(0, screen["width"]-50)
            rand_y = randint(0, screen["height"]-100)
            lose_sound.play()
            hero["x"] = rand_x
            hero["y"] = rand_y
            hero["health"] -= monster['damage']
        elif (monster['direction'] == 'N'):
            if monster['y'] > 20:
                monster['y'] -= monster['speed']
        elif (monster['direction'] == 'S'):
            if monster['y'] < screen["height"] - 200:
                monster['y'] += monster['speed']
        elif (monster['direction'] == 'E'):
            if monster['x'] < screen['width'] - 200:
                monster['x'] += monster['speed']
        elif (monster['direction'] == 'W'):
            if monster['x'] > 20:
                monster['x'] -= monster['speed']
        elif (monster['direction'] == 'NE'):
            if monster['y'] > 20 and monster['x'] < screen['width'] - 200:
                monster['y'] -= monster['speed']
                monster['x'] += monster['speed']
        elif (monster['direction'] == 'NW'):
            if monster['y'] > 20 and monster['x'] > 20:
                monster['y'] -= monster['speed']
                monster['x'] -= monster['speed']
        elif (monster['direction'] == 'SE'):
            if monster['y'] < screen["height"] - 200 and monster['x'] < screen['width'] - 200:
                monster['y'] += monster['speed']
                monster['x'] += monster['speed']
        elif (monster['direction'] == 'SW'):
            if monster['y'] < screen["height"] - 200 and monster['x'] > 20:
                monster['y'] += monster['speed']
                monster['x'] -= monster['speed']
        
        if distance_from_health < 50:
            hero['health'] += health_boost['amount']
            heal_sound.play()
            health_boost['x'] = 550
            health_boost['y'] = 500
            health_boost['speed'] = 0
        elif (health_boost['direction'] == 'N'):
            if health_boost['y'] > 20:
                health_boost['y'] -= health_boost['speed']
        elif (health_boost['direction'] == 'S'):
            if health_boost['y'] < screen["height"] - 200:
                health_boost['y'] += health_boost['speed']
        elif (health_boost['direction'] == 'E'):
            if health_boost['x'] < screen['width'] - 200:
                health_boost['x'] += health_boost['speed']
        elif (health_boost['direction'] == 'W'):
            if health_boost['x'] > 20:
                health_boost['x'] -= health_boost['speed']
        elif (health_boost['direction'] == 'NE'):
            if health_boost['y'] > 20 and health_boost['x'] < screen['width'] - 200:
                health_boost['y'] -= health_boost['speed']
                health_boost['x'] += health_boost['speed']
        elif (health_boost['direction'] == 'NW'):
            if health_boost['y'] > 20 and health_boost['x'] > 20:
                health_boost['y'] -= health_boost['speed']
                health_boost['x'] -= health_boost['speed']
        elif (health_boost['direction'] == 'SE'):
            if health_boost['y'] < screen["height"] - 200 and health_boost['x'] < screen['width'] - 200:
                health_boost['y'] += health_boost['speed']
                health_boost['x'] += health_boost['speed']
        elif (health_boost['direction'] == 'SW'):
            if health_boost['y'] < screen["height"] - 200 and health_boost['x'] > 20:
                health_boost['y'] += health_boost['speed']
                health_boost['x'] -= health_boost['speed']
    
    
    
    
       
       
    # random_motion(goblin["x"], goblin["y"])
    # RENDER!
    # 6. Screen.fill (background_color)
    pygame_screen.blit(background_image, [0, 0])

    # draw the hero's wins on the screen'
    kill_font = pygame.font.Font(None, 40)
    kill_text = kill_font.render("Kills: %d " % (hero["kills"]), True, (241,43,36))
    pygame_screen.blit(kill_text, [40, 10])
    level_font = pygame.font.Font(None, 40)
    level_text = level_font.render('Level: %d' % (level), True, (1, 155, 225))
    pygame_screen.blit(level_text, [190, 10])

    
    health_font = pygame.font.Font(None, 40)
    health_text = health_font.render("Health: %d " % (hero["health"]), True, (44,136,145))
    pygame_screen.blit(health_text, [340, 10])
    win_font = pygame.font.Font(None, 65)
    win_font2 = pygame.font.Font(None, 40)
    restart_font = pygame.font.Font(None, 40)
    restart_text = restart_font.render("Press Spacebar to Continue...", True, (71, 144, 32))
    pause_font1 = pygame.font.Font(None, 80)
    pause_font2 = pygame.font.Font(None, 40)
    pause_text1 = pause_font1.render("Game Paused", True, (71, 144, 32))
    pause_text2 = pause_font2.render("Press Spacebar to Continue...", True, (71, 144, 32))
    lose_font = pygame.font.Font(None, 80)
    
    if game_paused:
        pygame_screen.blit(pause_text1, [60, 180])
        pygame_screen.blit(pause_text2, [60, 250])


    # draw the hero
    pygame_screen.blit(hero_image_scaled, [hero["x"], hero["y"]])
    pygame_screen.blit(goblin_image_scaled, [goblin["x"], goblin["y"]])
    pygame_screen.blit(monster_image, [monster['x'], monster['y']])
    pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])

    if hero['kills'] == 3 and not level == 10:
        hero_won = not hero_won
        # pygame.mixer.music.pause()
        # win_sound.play()
        pygame_screen.blit(background_image, [0, 0])
        win_text = win_font.render("You Win!!", True, (71, 144, 32))
        pygame_screen.blit(win_text, [120, 180])
        pygame_screen.blit(restart_text, [60, 250])
        if event.key == 32:
            hero_won = False
            hero['kills'] = 0
            level += 1
            # pygame.mixer.music.play()
            pygame_screen.blit(background_image, [0, 0])
            pygame_screen.blit(kill_text, [40, 40])
            pygame_screen.blit(health_text, [340, 40])
            pygame_screen.blit(level_text, [190, 10])
            pygame_screen.blit(hero_image_scaled, [hero["x"], hero["y"]])
            pygame_screen.blit(goblin_image_scaled, [goblin["x"], goblin["y"]])
            pygame_screen.blit(monster_image, [monster['x'], monster['y']])
            pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])
    elif hero['kills'] == 3 and level == 10:
        hero_won = not hero_won
        game_win_text = win_font.render("CONGRATULATIONS!", True, (71, 144, 32))
        game_win_text2 = win_font2.render("You have saved the Realm!", True, (71, 144, 32))
        game_win_text3 = restart_font.render("Press Spacebar to Quit...", True, (71, 144, 32))
        pygame_screen.blit(background_image, [0, 0])
        pygame_screen.blit(game_win_text, [20, 100])
        pygame_screen.blit(game_win_text2, [50, 160])
        pygame_screen.blit(game_win_text3, [30, 220])
        if event.key == 32:
            game_on = False
    if hero['health'] <= 0:
        hero_won = not hero_won
        # pygame.mixer.music.pause()
        # win_sound.play()
        pygame_screen.blit(background_image, [0, 0])
        lose_text = lose_font.render("You Lose!", True, (200, 30, 30))
        pygame_screen.blit(lose_text, [120, 180])
        pygame_screen.blit(restart_text, [60, 250])
        if event.key == 32:
            hero_won = False
            hero['kills'] = 0
            hero['health'] = 60
            # pygame.mixer.music.play()
            pygame_screen.blit(background_image, [0, 0])
            pygame_screen.blit(kill_text, [40, 40])
            pygame_screen.blit(health_text, [340, 40])
            pygame_screen.blit(hero_image_scaled, [hero["x"], hero["y"]])
            pygame_screen.blit(goblin_image_scaled, [goblin["x"], goblin["y"]])
            pygame_screen.blit(monster_image, [monster['x'], monster['y']])
            pygame_screen.blit(health_boost_image, [health_boost['x'], health_boost['y']])
    
    if level == 2:
        goblin['speed'] = 4
    if level == 3:
        monster['speed'] = 12
    if level == 4:
        goblin['speed'] = 5
    if level == 5:
        monster['damage'] = 15
    if level == 6:
        hero['speed'] = 6
        monster['damage'] = 20
    if level == 7:
        health_boost['amount'] = 45
    if level == 8:
        goblin['speed'] = 6
        health_boost['amount'] = 50
    if level == 9:
        monster['speed'] = 14
    if level == 10:
        goblin['speed'] = 8
        hero['speed'] = 7
        monster['damage'] = 25


    # 7. clear the screen for next time (flip the screen) - the image gets drawn in every loop
    pygame.display.flip()