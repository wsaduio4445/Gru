import pygame
#Import Pygame
from pygame.locals import *
#Import common functions and values
from sys import exit
#Import function "exit" from sys

pygame.init()
#Initialize Pygame, make hardwares ready to use by pygame

screen = pygame.display.set_mode((800, 480), 0, 32)
#Create a 800*480 window
pygame.display.set_caption("Hero alpha v1.0")
#Set up the title of the window

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
#Load buttons' images

start_selected = True
option_selected = False
quit_selected = False
#Define buttons' values



process = True
#Define the loop

while process:
#Keep looping through

    x_axis -= 0.2
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
        #Check if user clicks close-button
            process = False
            pygame.quit()
            exit()
            #If it's true, quit the game

        if event.type == pygame.KEYDOWN:
            if start_selected == True and option_selected == False and quit_selected == False:
                if event.key == pygame.K_UP:
                    start_selected = False
                    option_selected = False
                    quit_selected = True
                elif event.key == pygame.K_DOWN:
                    start_selected = False
                    option_selected = True
                    quit_selected = False
            elif start_selected == False and option_selected == True and quit_selected == False:
                if event.key == pygame.K_UP:
                    start_selected = True
                    option_selected = False
                    quit_selected = False
                elif event.key == pygame.K_DOWN:
                    start_selected = False
                    option_selected = False
                    quit_selected = True
            elif start_selected == False and option_selected == False and quit_selected == True:
                if event.key == pygame.K_UP:
                    start_selected = False
                    option_selected = True
                    quit_selected = False
                elif event.key == pygame.K_DOWN:
                    start_selected = True
                    option_selected = False
                    quit_selected = False

    if start_selected == True and option_selected == False and quit_selected == False:
        screen.blit(start_button_selected, (592, 272))
        screen.blit(option_button, (592, 328))
        screen.blit(quit_button, (592, 384))
        pygame.display.update()
    elif start_selected == False and option_selected == True and quit_selected == False:
        screen.blit(start_button, (592, 272))
        screen.blit(option_button_selected, (592, 328))
        screen.blit(quit_button, (592, 384))
        pygame.display.update()
    elif start_selected == False and option_selected == False and quit_selected == True:
        screen.blit(start_button, (592, 272))
        screen.blit(option_button, (592, 328))
        screen.blit(quit_button_selected, (592, 384))
        pygame.display.update()
    
    pygame.display.update()
    #Update screen
