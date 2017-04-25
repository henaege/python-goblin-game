# 1. Include pygame
# Include pygame which we got from pip
import pygame

# bring in the math module so we can use absolute value
from math import fabs

# Get the random module
from random import randint

# in order to use pygame, we have to run the init method
# 2. Init pygame
pygame.init()


# 3. Create a screen with a size
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

keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False,
}

hero = {
	"x": 100,
	"y": 100,
	"speed": 10,
	"wins": 0,
	"is_alive": True
}

goblin = {
	"x": 200,
	"y": 200,
	"speed_x": 5,
	"speed_y": 5,
	"direction": "N"
}

powerup = {
	'active': True,
	'tick_gotten': 0	
}

game_paused = False


directions = ['N','S','E','W','NE','NW','SE','SW']

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('./images/background.png')
hero_image = pygame.image.load('./images/hero.png')
hero_image_scaled = pygame.transform.scale(hero_image, (32,32))
goblin_image = pygame.image.load('images/goblin.png')
# powerup_image = pygame.image.load('./images/Mushroom.png')
# powerup_image_scaled = pygame.transform.scale(powerup_image, (32,32))

# Add music files
# pygame.mixer.music.load('./sounds/faf.wav')
# pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound('./sounds/win.wav')
lose_sound = pygame.mixer.Sound('./sounds/lose.wav')

tick = 0
timer = 0


# /////////////////////////////////////////////
# //////////////MAIN GAME LOOP/////////////////
# /////////////////////////////////////////////	x
game_on = True
# Create the game loop (while 1)
while game_on:
	# update our ticker each time through the loop ~30/sec
	tick += 1

	# we are inside teh main game loop. It will run as long as game_on is true
	# ---EVENTS!!----
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		# 4. Add a quit event (requires sys)
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean, so pygame can escape the loop
		elif event.type == pygame.KEYDOWN:
			if event.key == keys['up']:
				keys_down['up'] = True
			elif event.key == keys['down']:
				keys_down['down'] = True
			elif event.key == keys['left']:
				# print "User pressed left!"
				keys_down['left'] = True
			elif event.key == keys['right']:
				# print "User pressed right!"
				keys_down['right'] = True
			elif event.key == 121:
				# userpushed "y"
				hero['x'] = 100
				hero['y'] = 100
			elif event.key == 32:
				# user pushed space!
				game_paused = not game_paused
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == keys['up']:
				# the user let go of a key... and that key was the up arrow
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['left']:
				keys_down['left'] = False
			if event.key == keys['right']:
				keys_down['right'] = False

	if(not game_paused):
		# Update Hero position
		if keys_down['up']:
			hero['y'] -= hero['speed']
		elif keys_down['down']:
			hero['y'] += hero['speed']
		if keys_down['left']:
			hero['x'] -= hero['speed']
		elif keys_down['right']:
			hero['x'] += hero['speed']

		# update goblin position
		# get random direction (up down left or right)
		# move goblin in that direction
		# if (goblin['direction'] == 'N'):
		# 	goblin['y'] -= goblin['speed']
		# elif (goblin['direction'] == 'S'):
		# 	goblin['y'] += goblin['speed']
		# elif (goblin['direction'] == 'E'):
		# 	goblin['x'] += goblin['speed']
		# elif (goblin['direction'] == 'W'):
		# 	goblin['x'] -= goblin['speed']
		# elif (goblin['direction'] == 'NE'):
		# 	goblin['y'] -= goblin['speed']
		# 	goblin['x'] += goblin['speed']
		# elif (goblin['direction'] == 'NW'):
		# 	goblin['y'] -= goblin['speed']
		# 	goblin['x'] -= goblin['speed']
		# elif (goblin['direction'] == 'SE'):
		# 	goblin['y'] += goblin['speed']
		# 	goblin['x'] += goblin['speed']
		# elif (goblin['direction'] == 'SW'):
		# 	goblin['y'] += goblin['speed']
		# 	goblin['x'] -= goblin['speed']

	goblin['x'] += goblin['speed_x']
	goblin['y'] += goblin['speed_y']

	if (goblin['x'] > screen['width']) or (goblin['x'] < 0):
		goblin['speed_x'] = -goblin['speed_x']
	if (goblin['y'] > screen['height']) or (goblin['y'] < 0):
		goblin['speed_y'] = -goblin['speed_y']


	if (tick % 20 == 0):
		# new_dir_index = randint(0, len(directions)-1)
		# goblin['direction'] = directions[new_dir_index]
		goblin['speed_x'] += randint(-2,3)
		goblin['speed_y'] += randint(-2,3)

	# if (goblin['x'] > screen['width']):
	# 	goblin['x'] = 0
	# elif (goblin['x'] < 0):
	# 	goblin['x'] = screen['width']
	# if (goblin['y'] > screen['height']):
	# 	goblin['y'] = 0
	# elif (goblin['y'] < 0):
	# 	goblin['y'] = screen['height']



	# COLLISION DETECTION!!

	# For goblin and hero
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if (distance_between < 32):
		# the hero and goblin are touching!
		# print ("Collision!!")
		# Generate a random X > 0, X < screen['width']
		# Generate a random Y > 0, Y < screen['height']
		rand_x = randint(0,screen['width'])
		rand_y = randint(0,screen['height'])
		goblin['x'] = rand_x
		goblin['y'] = rand_y
		# Update the hero's wins
		if(not game_paused):
			hero['wins'] += 1
			goblin['speed'] += 5
			win_sound.play()

	# For powerup and hero
	distance_between = fabs(hero['x'] - 100) + fabs(hero['y'] - 200)
	if (distance_between < 32):
		print 'hero ran into musroom!'



	# ---RENDER!---
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	# Screen.fill (pass bg_color)
	pygame_screen.blit(background_image, [0,0])

	# Draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	if (tick % 30 == 0):
		timer += 1
	timer_text = font.render("Seconds Alive: %d" % (timer), True, (0,0,0))
	pygame_screen.blit(timer_text, [40,100])

	if(game_paused):
		timer_text = font.render("Game Paused. Hit space to unpause", True, (0,0,0))
		pygame_screen.blit(timer_text, [200,300])


	# draw the hero
	pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])
	pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])
	# pygame_screen.blit(powerup_image_scaled, [100,200])

	# clear the screen for next time
	pygame.display.flip()

