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

process = True
#Define the loop

while process:
#Keep looping through
    for event in pygame.event.get():
    #Loop through the events    
        if event.type == pygame.QUIT:
        #Check if user clicks close-button    
            pygame.quit()
            exit()
            #If it's true, quit the game

    x_axis -= 0.1
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
    pygame.display.update()
    #Update screen
