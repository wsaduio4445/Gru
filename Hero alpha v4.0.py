#Hero alpha version 4.0
#05.12.2016

import pygame
#Import Pygame
import random
from pygame.locals import *
#Import common functions and values


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


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shield_image
        self.rect = self.image.get_rect()


pygame.init()
pygame.mixer.init()
#Initialize Pygame

screen_width = 800
screen_height = 480

white = (255, 255, 255)

screen = pygame.display.set_mode([screen_width, screen_height])
#Create a 800*480 window
pygame.display.set_caption("Hero alpha v3.0")
#Set up the title of the window

keys = [False, False, False, False]
directions = [True, False, False, False]

asteroid_large_list = pygame.sprite.Group()
asteroid_medium_list = pygame.sprite.Group()
asteroid_small_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
missile_up_list = pygame.sprite.Group()
missile_down_list = pygame.sprite.Group()
missile_left_list = pygame.sprite.Group()
missile_right_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
shield_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#player_position = [370, 400]

background_image_filename = "Image/Menu/Main menu/main_menu.png"
#Set main menu background
background_image_loop = "Image/Menu/Main menu/main_menu.png"
#Define another one for the loop
background = pygame.image.load(background_image_filename).convert()
background_loop = pygame.image.load(background_image_loop).convert()
#Load and convert the background
background_array = [background_image_filename, background_image_loop]
#Create an array for background
x_axis, y_axis = 0, 0
#Position of looping

background_game_over = pygame.image.load("Image/Menu/Game over/game_over.png")

press_enter = pygame.mixer.Sound("Audio/press_enter.wav")
explode = pygame.mixer.Sound("Audio/explode.wav")
shoot = pygame.mixer.Sound("Audio/shoot.wav")

press_enter.set_volume(0.05)
explode.set_volume(0.1)
shoot.set_volume(0.05)

pygame.mixer.music.load("Audio/05 Come and Find Me.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.2)

new_game_button = pygame.image.load("Image/Menu/Main menu/new_game_button.png")
new_game_button_selected = pygame.image.load("Image/Menu/Main menu/new_game_button_selected.png")
continue_button = pygame.image.load("Image/Menu/Main menu/continue_button.png")
continue_button_selected = pygame.image.load("Image/Menu/Main menu/continue_button_selected.png")
restart_button = pygame.image.load("Image/Menu/Game over/restart_button.png")
restart_button_selected = pygame.image.load("Image/Menu/Game over/restart_button_selected.png")
option_button = pygame.image.load("Image/Menu/Main menu/option_button.png")
option_button_selected = pygame.image.load("Image/Menu/Main menu/option_button_selected.png")
quit_button = pygame.image.load("Image/Menu/Main menu/quit_button.png")
quit_button_selected = pygame.image.load("Image/Menu/Main menu/quit_button_selected.png")
back_button = pygame.image.load("Image/Menu/Option/back_button.png")
back_button_selected = pygame.image.load("Image/Menu/Option/back_button_selected.png")
#Load buttons' images

asteroid_large_image = pygame.image.load("Image/Enemy/object_large.png")
asteroid_medium_image = pygame.image.load("Image/Enemy/object_medium.png")
asteroid_small_image = pygame.image.load("Image/Enemy/object_small.png")
                                         

player_up = pygame.image.load("Image/Charactor/player_static_up.png")
player_down = pygame.image.load("Image/Charactor/player_static_down.png")
player_left = pygame.image.load("Image/Charactor/player_static_left.png")
player_right = pygame.image.load("Image/Charactor/player_static_right.png")
shield_image = pygame.image.load("Image/Charactor/shield.png")
#Load player's images

player_image = player_up

missile_vertical = pygame.image.load("Image/Object/missile_vertical.png")
missile_horizontal = pygame.image.load("Image/Object/missile_horizontal.png")

#player_image = player_up
#Define default direction

player = Player()
player.rect.x = 370
player.rect.y = 400
shield = Shield()
shield.rect.x = player.rect.x - 5
shield.rect.y = player.rect.y - 5

player_list.add(player)
all_sprites_list.add(player)

new_game_selected = True
continue_selected = False
continue_disable = True
restart_selected = True
option_selected = False
quit_selected = False
back_selected = False
#Define buttons' values

process = True
menu = True
game = False
option = False
draw = True
alive = True
#Define the loop

score = 0
shield_active = False

draw_large = True
draw_medium = True
draw_small =True

additional_speed = 0

clock = pygame.time.Clock()

while process:
#Keep looping through
    screen.fill(white)
    while menu:
        screen.fill(white)

        x_axis -= 0.1
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
                press_enter.play()
                if new_game_selected == True and option_selected == False and quit_selected == False:
                #When start button is selected
                    if event.key == pygame.K_RETURN:
                        game = True
                        alive =True
                        
                        number_large = 20
                        number_medium = 30
                        number_small = 40
                        
                        menu = False
                    elif event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to quit button
                        new_game_selected = False
                        option_selected = False
                        quit_selected = True
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to option button
                        new_game_selected = False
                        option_selected = True
                        quit_selected = False
                elif new_game_selected == False and option_selected == True and quit_selected == False:
                #When option button is selected
                    if event.key == pygame.K_RETURN:
                    #If user presses enter key, move to option menu
                        option = True
                        menu = False
                    if event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to start button
                        new_game_selected = True
                        option_selected = False
                        quit_selected = False
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to quit button
                        new_game_selected = False
                        option_selected = False
                        quit_selected = True
                elif new_game_selected == False and option_selected == False and quit_selected == True:
                #When quit button is selected
                    if event.key == pygame.K_RETURN:
                        menu = False
                        process = False
                    elif event.key == pygame.K_UP:
                    #If user presses up arrow key, the selection will move to option button
                        new_game_selected = False
                        option_selected = True
                        quit_selected = False
                    elif event.key == pygame.K_DOWN:
                    #If user presses down arrow key, the selection will move to start button
                        new_game_selected = True
                        option_selected = False
                        quit_selected = False

        if new_game_selected == True and option_selected == False and quit_selected == False:
        #If start button is selected, highlight it, by drawing every button again
            screen.blit(new_game_button_selected, (592, 272))
            screen.blit(option_button, (592, 328))
            screen.blit(quit_button, (592, 384))
        #elif new_game_selected == False and option_selected == False and quit_selected == False:
            
        elif new_game_selected == False and option_selected == True and quit_selected == False:
        #If option button is selected, highlight it, by drawing every button again
            screen.blit(new_game_button, (592, 272))
            screen.blit(option_button_selected, (592, 328))
            screen.blit(quit_button, (592, 384))
        elif new_game_selected == False and option_selected == False and quit_selected == True:
        #If quit button is selected, highlight it, by drawing every button again
            screen.blit(new_game_button, (592, 272))
            screen.blit(option_button, (592, 328))
            screen.blit(quit_button_selected, (592, 384))
        
        pygame.display.update()
        #Update screen

    while option:
        screen.fill(white)
        x_axis -= 0.05
        #Define the speed of looping background
        if x_axis <= -800:
        #If the background is completely out of the window
            background_array = background_array[1:] + background_array[:1]
            #Loop the array
            x_axis = 800
            #Define where to start looping
        screen.blit(background, (x_axis, y_axis))
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
                press_enter.play()
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

    while game:
        screen.fill(white)

        font = pygame.font.Font("Font/Pixel LCD-7.fon", 24)
        score_header = font.render("Score:", True, (0,0,0))
        score_text = font.render(str(score).zfill(4), True, (0,0,0))
        
        score_rect = score_text.get_rect()
        header_rect = score_header.get_rect()
        score_rect.topright=[790,10]
        screen.blit(score_header, [650, 10])
        screen.blit(score_text, score_rect)
        
        explode.set_volume(0.1)
        pygame.mixer.music.set_volume(0.05)

        all_sprites_list.add(player)
        
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
                    draw = False
                    alive = True
                    player_image = player_up
                    player = Player()
                    asteroid_large_list.empty()
                    asteroid_medium_list.empty()
                    asteroid_small_list.empty()
                    asteroid_list.empty()
                    all_sprites_list.empty()
                    player = Player()
                    player.rect.x = 370
                    player.rect.y = 400
                    all_sprites_list.add(player)
                    x_axis, y_axis = 0, 0
                    menu = True
                    game = False

                if event.key == pygame.K_SPACE or event.key == pygame.K_z:
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

                if event.key == pygame.K_x:
                    shield_active = True
                    
                    
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
                if event.key == pygame.K_x:
                    shield_active = False
                    all_sprites_list.remove(shield)
                
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    keys[0] = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    keys[1] = False
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    keys[2] = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    keys[3] = False

        if alive:

            if keys[0]:
                if player.rect.y > 40:
                    player.rect.y -= 4
                player_image = player_up
                x_axis = player.rect.x
                y_axis = player.rect.y
                all_sprites_list.remove(player)
                if shield_active:
                    all_sprites_list.remove(shield)
                    shield = Shield()
                    shield.rect.x = x_axis - 5
                    shield.rect.y = y_axis - 5
                    all_sprites_list.add(shield)
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
                if shield_active:
                    all_sprites_list.remove(shield)
                    shield = Shield()
                    shield.rect.x = x_axis - 5
                    shield.rect.y = y_axis - 5
                    all_sprites_list.add(shield)
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
                if shield_active:
                    all_sprites_list.remove(shield)
                    shield = Shield()
                    shield.rect.x = x_axis - 5
                    shield.rect.y = y_axis - 5
                    all_sprites_list.add(shield)
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
                if shield_active:
                    all_sprites_list.remove(shield)
                    shield = Shield()
                    shield.rect.x = x_axis - 5
                    shield.rect.y = y_axis - 5
                    all_sprites_list.add(shield)
                player = Player()
                player.rect.x, player.rect.y = x_axis, y_axis
                all_sprites_list.add(player)
                directions = [False, False, False, True]

            if shield_active:
                all_sprites_list.remove(shield)
                shield = Shield()
                shield.rect.x = player.rect.x - 5
                shield.rect.y = player.rect.y - 5
                all_sprites_list.add(shield)

        #if draw:
        #    for i in range(4):
        #        asteroid = Asteroid_Large()
        #        asteroid.rect.x = random.randrange(100)#screen_width - 100)
        #        asteroid.rect.y = -random.randrange(100, 1000)
        #        asteroid_large_list.add(asteroid)
        #        asteroid_list.add(asteroid)
        #        all_sprites_list.add(asteroid)

        #    for i in range(1):
        #        asteroid = Asteroid_Medium()
        #        asteroid.rect.x = random.randrange(screen_width - 60)
        #        asteroid.rect.y = -random.randrange(60, 20000)
        #        asteroid_medium_list.add(asteroid)
        #        asteroid_list.add(asteroid)
        #        all_sprites_list.add(asteroid)

        #    for i in range(1):
        #        asteroid = Asteroid_Small()
        #        asteroid.rect.x = random.randrange(screen_width - 40)
        #        asteroid.rect.y = -random.randrange(40, 20000)
        #        asteroid_small_list.add(asteroid)
        #        asteroid_list.add(asteroid)
        #        all_sprites_list.add(asteroid)

         #   draw = False
        
        if draw_large:
            asteroid = Asteroid_Large()
            asteroid.rect.x = random.randrange(screen_width - 100)
            asteroid.rect.y = -random.randrange(100, 10000)
            asteroid_large_list.add(asteroid)
            asteroid_list.add(asteroid)
            all_sprites_list.add(asteroid)
            number_large -= 1

        if draw_large:
            asteroid = Asteroid_Medium()
            asteroid.rect.x = random.randrange(screen_width - 60)
            asteroid.rect.y = -random.randrange(100, 10000)
            asteroid_medium_list.add(asteroid)
            asteroid_list.add(asteroid)
            all_sprites_list.add(asteroid)
            number_medium -= 1

        if draw_small:
            asteroid = Asteroid_Small()
            asteroid.rect.x = random.randrange(screen_width - 40)
            asteroid.rect.y = -random.randrange(100, 10000)
            asteroid_small_list.add(asteroid)
            asteroid_list.add(asteroid)
            all_sprites_list.add(asteroid)
            number_small -= 1

        if number_large <= 0:
            draw_large = False
        elif number_large >= 0:
            draw_large = True

        if number_medium <= 0:
            draw_medium = False
        elif number_medium >= 0:
            draw_mediun = True

        if number_small <= 0:
            draw_small = False
        elif number_small >= 0:
            draw_small = True

                

        if pygame.sprite.groupcollide(missile_list, asteroid_large_list, True, True):
            explode.play()
            score += 60

        if pygame.sprite.groupcollide(missile_list, asteroid_medium_list, True, True):
            explode.play()
            score += 40

        if pygame.sprite.groupcollide(missile_list, asteroid_small_list, True, True):
            explode.play()
            score += 10
            
        if shield_active:
            if pygame.sprite.spritecollide(shield, asteroid_list, True):
                explode.set_volume(0.1)
                explode.play()
        else:
            if pygame.sprite.spritecollide(player, asteroid_list, True):
                explode.set_volume(0.4)
                explode.play()
                keys = [False, False, False, False]
                alive = False
                x_axis, y_axis = 0, 0
                player_image = player_up
                player = Player()
                asteroid_large_list.empty()
                asteroid_medium_list.empty()
                asteroid_small_list.empty()
                asteroid_list.empty()
                player_list.empty()
                all_sprites_list.empty()
                player = Player()
                player.rect.x = 370
                player.rect.y = 400
                
                additional_speed = 0
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

        #for block in asteroid_large_list:
            #if 
            #block.rect.y += 1#(random.randrange(10, 20) / 10) + large_additional_speed

        additional_speed = 0
        for block in asteroid_large_list:
            block.rect.y += (1 + additional_speed)
            if block.rect.y > 480:
                #block.rect.x = random.randrange(100)#screen_width - 100)
                #block.rect.y = -random.randrange(100, 200)
                asteroid_large_list.remove(block)
                asteroid_list.remove(block)
                all_sprites_list.remove(block)
                number_large += 1
                if additional_speed < 4:
                    additional_speed += 0.4
                    
        additional_speed = 0
        for block in asteroid_medium_list:
            block.rect.y += (1.1 + additional_speed)
            if block.rect.y > 480:
                asteroid_medium_list.remove(block)
                asteroid_list.remove(block)
                all_sprites_list.remove(block)
                number_medium += 1
                if additional_speed < 4:
                    additional_speed += 0.2

        additional_speed = 0
        for block in asteroid_small_list:
            block.rect.y += (1.2 + additional_speed)
            if block.rect.y > 480:
                asteroid_small_list.remove(block)
                asteroid_list.remove(block)
                all_sprites_list.remove(block)
                number_small += 1
                if additional_speed < 4:
                    additional_speed += 0.1
        
        all_sprites_list.draw(screen)

        clock.tick(70)

        pygame.display.flip()

    while not alive:
        screen.fill(white)
        screen.blit(background_game_over, [0, 0])

        for event in pygame.event.get():
        #Loop through the events
            screen.blit(background_game_over, [0, 0])
            if event.type == pygame.QUIT:
            #if user clicks close button
                process = False
                alive = True
                #End of loop

            if event.type == pygame.KEYDOWN:
            #Check if user presses any key
                press_enter.play()
                if restart_selected == True and back_selected == False:
                #When start button is selected
                    if event.key == pygame.K_RETURN:
                        game = True
                        alive =True
                        
                        number_large = 20
                        number_medium = 30
                        number_small = 40
                        
                    elif event.key == pygame.K_UP:
                        restart_selected == False
                        back_selected == True
                    elif event.key == pygame.K_DOWN:
                        restart_selected == False
                        back_selected == True
                elif restart_selected == False and back_selected == True:
                    if event.key == pygame.K_RETURN:
                        menu = True
                        alive = True
                        
                    if event.key == pygame.K_UP:
                        restart_selected == True
                        back_selected == False
                    elif event.key == pygame.K_DOWN:
                        restart_selected == True
                        back_selected == False
        
        if restart_selected == True and back_selected == False:
            screen.blit(restart_button_selected, (592, 328))
            screen.blit(back_button, (592, 384))
        else:
            screen.blit(restart_button, (592, 328))
            screen.blit(back_button_selected, (592, 384))
                  
    pygame.mixer.music.set_volume(0.2)

pygame.quit()
#Quit the game
