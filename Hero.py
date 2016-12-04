#Hero alpha version 3.0
#03.12.2016

import pygame
#Import Pygame
import random
from pygame.locals import *
#Import common functions and values
from sys import exit
#Import function "exit" from sys


class Asteroid_Large(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_large_image
        self.rect = self.image.get_rect()


class Asteroid_Medium(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_medium_image
        self.rect = self.image.get_rect()


class Asteroid_Small(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asteroid_small_image
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()


class Missile_vertical(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_vertical
        self.rect = self.image.get_rect()


class Missile_horizontal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_horizontal
        self.rect = self.image.get_rect()




pygame.init()
#Initialize Pygame

screen_width = 800
screen_height = 480

white = (255, 255, 255)
GREY = (70, 80, 90)
screen = pygame.display.set_mode([screen_width, screen_height])
#Create a 800*480 window
pygame.display.set_caption("Hero alpha v1.0")
#Set up the title of the window

keys = [False, False, False, False]
directions = [True, False, False, False]

shoot = pygame.mixer.Sound("audio/shoot.wav")
pygame.mixer.music.load("audio/track1.wav")
#set up voice
asteroid_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
missile_up_list = pygame.sprite.Group()
missile_down_list = pygame.sprite.Group()
missile_left_list = pygame.sprite.Group()
missile_right_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#player_position = [370, 400]

background_image_filename = 'Images/Menu/Main menu/main_menu.png'
#Set main menu background
background_image_loop = 'Images/Menu/Main menu/main_menu.png'
#Define another one for the loop
background = pygame.image.load(background_image_filename).convert()
background_loop = pygame.image.load(background_image_loop).convert()
#Load and convert the background
background_array = [background_image_filename, background_image_loop]
#Create an array for background
x_axis, y_axis = 0, 0
#Position of looping

start_button = pygame.image.load("Images/Menu/Main menu/start_button.png")
start_button_selected = pygame.image.load("Images/Menu/Main menu/start_button_selected.png")
option_button = pygame.image.load("Images/Menu/Main menu/option_button.png")
option_button_selected = pygame.image.load("Images/Menu/Main menu/option_button_selected.png")
quit_button = pygame.image.load("Images/Menu/Main menu/quit_button.png")
quit_button_selected = pygame.image.load("Images/Menu/Main menu/quit_button_selected.png")
back_button = pygame.image.load("Images/Menu/Option/back_button.png")
back_button_selected = pygame.image.load("Images/Menu/Option/back_button_selected.png")
voice_button_on=pygame.image.load("Images/Menu/Option/voice_button_on.png")
voice_button_off=pygame.image.load("Images/Menu/Option/voice_button_off.png")
#Load buttons' images

asteroid_large_image = pygame.image.load("Images/Enemy/object_large.png")
asteroid_medium_image = pygame.image.load("Images/Enemy/object_medium.png")
asteroid_small_image = pygame.image.load("Images/Enemy/object_small.png")
                                         

player_up = pygame.image.load("Images/Charactor/player_static_up.png")
player_down = pygame.image.load("Images/Charactor/player_static_down.png")
player_left = pygame.image.load("Images/Charactor/player_static_left.png")
player_right = pygame.image.load("Images/Charactor/player_static_right.png")
#Load player's images

player_image = player_up

missile_vertical = pygame.image.load("Images/Object/missile_vertical.png")
missile_horizontal = pygame.image.load("Images/Object/missile_horizontal.png")

#player_image = player_up
#Define default direction
game_over = pygame.image.load("Images/gameover.png")
#gameover image
player = Player()
player.rect.x = 370
player.rect.y = 400

player_list.add(player)
all_sprites_list.add(player)

start_selected = True
option_selected = False
quit_selected = False
back_selected = False
voice=0.25
#Define buttons' values
score=0
my_font = pygame.font.SysFont("", 30)
#secore and secore font
process = True
menu = True
game = False
option = False
draw = True
#Define the loop

pygame.mixer.init()
#Define the mixer

pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(voice)
shoot.set_volume(voice)


clock = pygame.time.Clock()

while process:
#Keep looping through
    screen.fill(white)
    while menu:
        screen.fill(white)
        x_axis -= 0.4
        #Define the speed of looping background
        if x_axis <= -800:
        #If the background is completely out of the window
            background_array = background_array[1:] + background_array[:1]
            #Loop the array
            #background_image_filename, background_image_loop = background_array
            #?
            x_axis = 800
            #Define where to start looping
        screen.blit(background, (x_axis, y_axis))
        #Start looping
        
        for event in pygame.event.get():
        #Loop through the events
            if event.type == pygame.QUIT:
            #if user clicks close button
                menu = False
                process = False
                #End of loop

            if event.type == pygame.KEYDOWN:
            #Check if user presses any key
                if start_selected == True and option_selected == False and quit_selected == False:
                #When start button is selected
                    if event.key == pygame.K_RETURN:
                        game = True
                        draw = True
                        menu = False
                        gameover=False
                    elif event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to quit button
                        start_selected = False
                        option_selected = False
                        quit_selected = True
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to option button
                        start_selected = False
                        option_selected = True
                        quit_selected = False
                elif start_selected == False and option_selected == True and quit_selected == False:
                #When option button is selected
                    if event.key == pygame.K_RETURN:
                    #If user presses enter key, move to option menu
                        option = True
                        menu = False
                        gameover=False
                    if event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to start button
                        start_selected = True
                        option_selected = False
                        quit_selected = False
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to quit button
                        start_selected = False
                        option_selected = False
                        quit_selected = True
                elif start_selected == False and option_selected == False and quit_selected == True:
                #When quit button is selected
                    if event.key == pygame.K_RETURN:
                        menu = False
                        process = False
                    elif event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to option button
                        start_selected = False
                        option_selected = True
                        quit_selected = False
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to start button
                        start_selected = True
                        option_selected = False
                        quit_selected = False

        if start_selected == True and option_selected == False and quit_selected == False:
        #If start button is selected, highlight it, by drawing every button again
            screen.blit(start_button_selected, (592, 272))
            screen.blit(option_button, (592, 328))
            screen.blit(quit_button, (592, 384))
        elif start_selected == False and option_selected == True and quit_selected == False:
        #If option button is selected, highlight it, by drawing every button again
            screen.blit(start_button, (592, 272))
            screen.blit(option_button_selected, (592, 328))
            screen.blit(quit_button, (592, 384))
        elif start_selected == False and option_selected == False and quit_selected == True:
        #If quit button is selected, highlight it, by drawing every button again
            screen.blit(start_button, (592, 272))
            screen.blit(option_button, (592, 328))
            screen.blit(quit_button_selected, (592, 384))
        
        pygame.display.update()
        #Update screen

    while option:
        screen.fill(white)
        x_axis -= 0.1

        #Define the speed of looping background
        if x_axis <= -800:
        #If the background is completely out of the window
            background_array = background_array[1:] + background_array[:1]
            #Loop the array
            x_axis = 800
            #Define where to start looping
        screen.blit(background, (x_axis, y_axis))

        voice_triggle = True
        #Start looping
        for event in pygame.event.get():
        #Loop through the events
            if event.type == pygame.QUIT:
            #if user clicks close button
                option = False
                process = False

                #End of loop
            
            if event.type == pygame.KEYDOWN:
            #Check if user presses any key
                if event.key == pygame.K_RETURN:
                #When user presses enter key
                    if back_selected == True:
                        back_selected = False
                        menu = True
                        option = False
                elif event.key == pygame.K_ESCAPE:
                #When user presses escape key
                    back_selected = False
                    menu = True
                    option = False
                
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    back_selected = True
                    
        if back_selected == True:
            screen.blit(back_button_selected, (592, 384))
        else:
            screen.blit(back_button, (592, 384))
        
        pygame.display.update()
    while gameover:
        screen.fill(white)
        screen.blit(game_over, (240, 200))
        label = my_font.render('your score :'+str(score), 1, GREY)
        screen.blit(label, ((screen_width/2)-53, 153))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    score=0
                    menu=True
                    gameover=False
        pygame.display.update()
    #gameover
    while game:
        screen.fill(white)

        for event in pygame.event.get():
        #Loop through the events
            if event.type == pygame.QUIT:
            #if user clicks close button
                game = False
                process = False
                #End of loop
            if event.type == pygame.KEYDOWN:
            #Check if user presses any key
                if event.key == pygame.K_ESCAPE:
                #When user presses escape key
                    player_image = player_up
                    player = Player()
                    all_sprites_list.empty()
                    screen.fill(white)
                    player = Player()
                    player.rect.x = 370
                    player.rect.y = 400
                    all_sprites_list.add(player)
                    gameover=True
                    game = False

                if event.key == pygame.K_SPACE:
                    shoot.play()
                    if directions[0]:
                        shot = Missile_vertical()
                        shot.rect.x = player.rect.x + 19
                        shot.rect.y = player.rect.y + 27
                        missile_up_list.add(shot)
                        missile_list.add(shot)
                        all_sprites_list.add(shot)
                        
                    elif directions[1]:
                        shot = Missile_vertical()
                        shot.rect.x = player.rect.x + 19
                        shot.rect.y = player.rect.y + 33
                        missile_down_list.add(shot)
                        missile_list.add(shot)
                        all_sprites_list.add(shot)

                    elif directions[2]:
                        shot = Missile_horizontal()
                        shot.rect.x = player.rect.x + 21
                        shot.rect.y = player.rect.y + 19
                        missile_left_list.add(shot)
                        missile_list.add(shot)
                        all_sprites_list.add(shot)

                    elif directions[3]:
                        shot = Missile_horizontal()
                        shot.rect.x = player.rect.x + 33
                        shot.rect.y = player.rect.y + 19
                        missile_right_list.add(shot)
                        missile_list.add(shot)
                        all_sprites_list.add(shot)
                    
                    
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    #player = player_up
                    keys[0] = True
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    #player = player_down
                    keys[1] = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    #player = player_left
                    keys[2] = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    #player = player_down
                    keys[3] = True

            elif event.type == pygame.KEYUP:
            #When user releases any key
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    keys[0] = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    keys[1] = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    keys[2] = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    keys[3] = False

        if keys[0]:
            if player.rect.y > 40:
                player.rect.y -= 4
            player_image = player_up
            x_axis = player.rect.x
            y_axis = player.rect.y
            all_sprites_list.remove(player)
            player = Player()
            player.rect.x, player.rect.y = x_axis, y_axis
            all_sprites_list.add(player)
            directions = [True, False, False, False]
        elif keys[1]:
            if player.rect.y < 400:
                player.rect.y += 4
            player_image = player_down
            x_axis = player.rect.x
            y_axis = player.rect.y
            all_sprites_list.remove(player)
            player = Player()
            player.rect.x, player.rect.y = x_axis, y_axis
            all_sprites_list.add(player)
            directions = [False, True, False, False]
        elif keys[2]:
            if player.rect.x < -30:
                player.rect.x = 770
            player.rect.x -= 4
            player_image = player_left
            x_axis = player.rect.x
            y_axis = player.rect.y
            all_sprites_list.remove(player)
            player = Player()
            player.rect.x, player.rect.y = x_axis, y_axis
            all_sprites_list.add(player)
            directions = [False, False, True, False]
        elif keys[3]:
            if player.rect.x > 770:
                player.rect.x = -30
            player.rect.x += 4
            player_image = player_right
            x_axis = player.rect.x
            y_axis = player.rect.y
            all_sprites_list.remove(player)
            player = Player()
            player.rect.x, player.rect.y = x_axis, y_axis
            all_sprites_list.add(player)
            directions = [False, False, False, True]

        if draw:
            for i in range(3):
                asteroid = Asteroid_Large()
                asteroid.rect.x = random.randrange(screen_width - 0)
                asteroid.rect.y = -random.randrange(100, 1000)
                asteroid_list.add(asteroid)
                all_sprites_list.add(asteroid)

            for i in range(4):
                asteroid = Asteroid_Medium()
                asteroid.rect.x = random.randrange(screen_width - 60)
                asteroid.rect.y = -random.randrange(60, 1000)
                asteroid_list.add(asteroid)
                all_sprites_list.add(asteroid)

            for i in range(5):
                asteroid = Asteroid_Small()
                asteroid.rect.x = random.randrange(screen_width - 40)
                asteroid.rect.y = -random.randrange(40, 1000)
                asteroid_list.add(asteroid)
                all_sprites_list.add(asteroid)
            draw = False
        
        if pygame.sprite.groupcollide(missile_list, asteroid_list, True, True):
            score += 1
        if pygame.sprite.groupcollide(player_list, asteroid_list, True, True):
            gameover = True
            game = False



        
        for shot in missile_up_list:
            shot.rect.y -= 7
            if shot.rect.y < 10 or shot.rect.y > 470 or shot.rect.x < -15 or shot.rect.x > 815:
                missile_list.remove(shot)
                all_sprites_list.remove(shot)

        for shot in missile_down_list:
            shot.rect.y += 7
            if shot.rect.y < 10 or shot.rect.y > 470 or shot.rect.x < -15 or shot.rect.x > 815:
                missile_list.remove(shot)
                all_sprites_list.remove(shot)

        for shot in missile_left_list:
            shot.rect.x -= 7
            if shot.rect.y < 10 or shot.rect.y > 470 or shot.rect.x < -15 or shot.rect.x > 815:
                missile_list.remove(shot)
                all_sprites_list.remove(shot)

        for shot in missile_right_list:
            shot.rect.x += 7
            if shot.rect.y < 10 or shot.rect.y > 470 or shot.rect.x < -15 or shot.rect.x > 815:
                missile_list.remove(shot)
                all_sprites_list.remove(shot)

        for block in asteroid_list:
            block.rect.y += 3

        all_sprites_list.draw(screen)
        pygame.draw.rect(screen, GREY, pygame.Rect(30, 30, 120, 60))
        label = my_font.render(str(score), 1, white)
        screen.blit(label, (53, 53))
        #score borad
        clock.tick(70)

        pygame.display.flip()

pygame.quit()
#Quit the game
#                for u in asteroid.rect:
#                    if asteroid.rect.y-player.rect.y < 5 or asteroid.rect.y-player.rect.y < -5:
#                        game=False
#                        menu=True
   
