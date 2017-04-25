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
    "down": 274,
    "s": K_s,
    "enter": K_RETURN,
    "space": K_SPACE
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
win_sound = pygame.mixer.Sound('./sounds/extralife.wav')
death_sound = pygame.mixer.Sound('./sounds/0477.ogg')
# ///////////////////// MAIN GAME LOOP ///////////////////

# 4. create game loop
loop_count = 0
game_on = True
game_paused = False
hero_won = False
level = 1

intro()

def play():
    while game_on:
        event_keys()


def event_keys():
    for event in pygame.event.get():
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
            elif event.key == keys['s']:
                keys_down['s'] = True
            elif event.key == keys['enter']:
                keys_down['enter'] = True
            elif event.key == keys['space']:
                keys_down['space'] = True
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

def change_dir(creature):
    dir_index = randint(0, len(directions)-1)
    creature['direction'] = directions[dir_index]

def move(creature):
    if (creature['direction'] == 'N'):
        if creature['y'] > 20:
                creature['y'] -= creature['speed']
    elif (creature['direction'] == 'S'):
        if creature['y'] < screen["height"] - 200:
                creature['y'] += creature['speed']
    elif (creature['direction'] == 'E'):
        if creature['x'] < screen['width'] - 200:
                creature['x'] += creature['speed']
    elif (creature['direction'] == 'W'):
        if creature['x'] > 20:
                creature['x'] -= creature['speed']
    elif (creature['direction'] == 'NE'):
        if creature['y'] > 20 and creature['x'] < screen['width'] - 200:
                creature['y'] -= creature['speed']
                creature['x'] += creature['speed']
    elif (creature['direction'] == 'NW'):
        if creature['y'] > 20 and creature['x'] > 20:
                creature['y'] -= creature['speed']
                creature['x'] -= creature['speed']
    elif (creature['direction'] == 'SE'):
        if creature['y'] < screen["height"] - 200 and creature['x'] < screen['width'] - 200:
                creature['y'] += creature['speed']
                creature['x'] += creature['speed']
    elif (creature['direction'] == 'SW'):
        if creature['y'] < screen["height"] - 200 and creature['x'] > 20:
                creature['y'] += creature['speed']
                creature['x'] -= creature['speed']

def collide(creature):
    rand_x = randint(0, screen["width"]-50)
    rand_y = randint(0, screen["height"]-200)
    creature["x"] = rand_x
    creature["y"] = rand_y

def intro():
    intro_font = pygame.font.Font(None, 30)
    intro_text1 = intro_font.render("Welcome to the realm of Pythonia.", True, (255, 245, 66))
    intro_text2 = intro_font.render("You have been hired to eradicate", True, (255, 245, 66))
    intro_text3 = intro_font.render("the goblin that has invaded.", True, (255, 245, 66))
    intro_text4 = intro_font.render("Kill the goblin and avoid the moster", True, (255, 245, 66))
    intro_text5 = intro_font.render("to prevail and become a hero of the realm.", True, (255, 245, 66))
    intro_text6 = intro_font.render("Press 's' to start your quest!", True, (255, 245, 66))
    pygame_screen.blit(intro_text1, [40, 40])
    pygame_screen.blit(intro_text2, [40, 70])
    pygame_screen.blit(intro_text3, [40, 100])
    pygame_screen.blit(intro_text4, [40, 130])
    pygame_screen.blit(intro_text5, [40, 160])
    pygame_screen.blit(intro_text6, [40, 190])
    if event.key == keys['s']:
        start()
