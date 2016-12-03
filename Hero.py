#Hero alpha version 1.0
#01.12.2016

import math
#Import math functions
import pygame
#Import Pygame
from pygame.locals import *
#Import common functions and values
from sys import exit
#Import function "exit" from sys

pygame.init()
#Initialize Pygame

screen = pygame.display.set_mode((800, 480), 0, 32)
#Create a 800*480 window
pygame.display.set_caption("Hero alpha v1.0")
#Set up the title of the window

keys = [False, False, False, False]
player_position = [370, 400]

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
#Load buttons' images

player_up = pygame.image.load("Images/Charactor/player_static_up.png")
#player_down = pygame.image.load("Images/Charactor/player_static_down.png")
#player_left = pygame.image.load("Images/Charactor/player_static_left.png")
#player_right = pygame.image.load("Images/Charactor/player_static_right.png")
#Load player's images

player = player_up
#Define default direction

start_selected = True
option_selected = False
quit_selected = False
back_selected = False
#Define buttons' values

process = True
menu = True
game = False
option = False
#Define the loop

while process:
#Keep looping through
    screen.fill((255, 255, 255))
    while menu:
        screen.fill((255, 255, 255))
        x_axis -= 0.4
        #Define the speed of looping background
        if x_axis <= -800:
        #If the background is completely out of the window
            background_array = background_array[1:] + background_array[:1]
            #Loop the array
            background_image_filename, background_image_loop = background_array
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
                        menu = False
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
        screen.fill((255, 255, 255))
        x_axis -= 0.1
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
        screen.fill((255, 255, 255))

        mouse_position = pygame.mouse.get_pos()

        angle = math.atan2(mouse_position[1] - (player_position[1] + 32), mouse_position[0] - (player_position[0] + 26))

        rotation = pygame.transform.rotate(player, 270 - angle * (360 / (math.pi * 2)))

        player_new_position = (player_position[0] - rotation.get_rect().width / 2, player_position[1] - rotation.get_rect().height / 2)

        screen.blit(rotation, player_new_position)

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
                menu = True
                game = False
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
        #When user releases any key
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        if keys[0] and keys[1] == False and keys[2] == False and keys[3] == False:
            player_position[1] -= 0.1
            #player = player_up
        if keys[2] and keys[0] == False and keys[1] == False and keys[3] == False:
            player_position[1] += 0.1
            #player = player_down
        if keys[1] and keys[0] == False and keys[2] == False and keys[3] == False:
            player_position[0] -= 0.1
            #player = player_left
        if keys[3] and keys[0] == False and keys[1] == False and keys[2] == False:
            player_position[0] += 0.1
            #player = player_right
        
        pygame.display.update()

pygame.quit()
#Quit the game
