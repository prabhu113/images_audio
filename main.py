"""
Assignment 2
# Josh Williamson, William Fleck, and Brandon Anderson

# This program draws a cat that blinks, moves with the arrow keys, falls down if the up arrow key isn't working, and can't leave the 
#screem, a sun that changes color and moves with mouse x and y coordinates, and a block of 4 houses.

Original documentation: (Leave this intact)
Pygame base template for opening a window, done with functions
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

Source: http://programarcadegames.com/python_examples/show_file.php?file=pygame_base_template_proper.py
Modified slightly by OttoBorchert 1/18/2018
 
"""

import random 
import pygame
import cat
 
# Define some colors as global constants (can add colors, if you'd like)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
GREY = (192, 192, 192)
BROWN = (153, 102, 51)
DARK_RED = (153, 0, 0)
GLASS = (204, 255, 229)
GOLD = (210, 178, 47)

sun_color = YELLOW
sun_ray_color = ORANGE

# Width and height of the screen (width,height)
size = (1100, 750)

def main():
    """ Main function for the game. """
    pygame.init()

    #boolean variable that determine whether or not the up arrow key is pressed.
    #Used later in game logic to assist in gravity
    upPressed = False
    downPressed = False

    # Speed in pixels per frame
    keyboard_x_speed = 0
    keyboard_y_speed = 0
     
    # Current position
    keyboard_x_coord = 100
    keyboard_y_coord = 300
 
    # Set the width and height of the screen [width,height]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #list with coordinates to draw satellites.  Used in following for loop
    satellite_coordinates = [ [300, 300], [570, 300], [300, 600], [570, 600] ]

    #fills list with sublists containing coordinates to draw houses
    house_coordinates = [ [300, 300], [570, 300], [300, 600], [570, 600] ]    
    
    #function to draw house object
    def draw_house(screen, x, y):
        pygame.draw.rect(screen, GREY, [x, y, 250, 15], 0)
        pygame.draw.rect(screen, BROWN, [x + 5, y - 150, 240, 150], 0)
        pygame.draw.polygon(screen, DARK_RED, [[x + 125, y - 250], [x, y - 150], [x + 250, y - 150]], 0)
        pygame.draw.rect(screen, BLACK, [x + 100, y - 100, 50, 100], 0)
        pygame.draw.rect(screen, GLASS, [x + 105, y - 95, 40, 90], 0)
        pygame.draw.rect(screen, GOLD, [x + 130, y - 50, 15, 5], 0)

    #function to draw sun object
    def draw_sun(screen, x, y, size, tick):
        side = size/3
        half_side = size/6
        half_size = size/2
        quarter_size = size/4
        indent = size/10
        global sun_color
        global sun_ray_color

        #function that changes variable sun_color
        if(tick%10 == 0):
            if(sun_color == ORANGE):
                sun_color = YELLOW
                sun_ray_color = ORANGE
            else:
                sun_color = ORANGE
                sun_ray_color = YELLOW
        
        #Triangle on upper part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + half_size - half_side, y + indent],
                                             [x + half_size + half_side, y + indent],
                                             [x + half_size, y + indent - side]], 0)

        #Triangle on upper right part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + half_size + quarter_size - half_side, y + quarter_size - indent],
                                             [x + half_size + quarter_size + half_side, y + quarter_size + indent],
                                             [x + half_size + quarter_size + half_side + indent, y + quarter_size - half_side - indent]], 0)

        #Triangle on bottom right part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + half_size + quarter_size + half_side, y + quarter_size*3 - indent],
                                             [x + half_size + quarter_size - half_side, y + quarter_size*3 + indent],
                                             [x + half_size + quarter_size + half_side + indent, y + quarter_size*3 + half_side + indent]], 0)
        
        #Triangle on bottom part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + half_size - half_side, y + size - indent],
                                             [x + half_size + half_side, y + size - indent],
                                             [x + half_size, y - indent + side + size]], 0)

        #Triangle on right side of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + size - indent, y + half_size - half_side],
                                             [x + size - indent, y + half_size + half_side],
                                             [x + size - indent + side, y + half_size]], 0)

        #Triangle on left side of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + indent, y + half_size - half_side],
                                             [x + indent, y + half_size + half_side],
                                             [x + indent - side, y + half_size]], 0)

        #Triangle on bottom left part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + quarter_size - half_side, y + quarter_size*3 - indent],
                                             [x + quarter_size + half_side, y + quarter_size*3 + indent],
                                             [x + quarter_size - half_side - indent, y + quarter_size*3 + half_side + indent]], 0)

        #Triangle on upper left part of sun
        pygame.draw.polygon(screen, sun_ray_color, [[x + quarter_size + half_side, y + quarter_size - indent],
                                             [x + quarter_size - half_side, y + quarter_size + indent],
                                             [x + quarter_size - half_side - indent, y + quarter_size - half_side - indent]], 0)

        #Circle representing the sun
        pygame.draw.ellipse(screen, sun_color, [x, y, size, size], 0)

    # Background image from https://opengameart.org/content/space-background-2
    background_image = pygame.image.load("background.bmp").convert()

    # Player object from Kenney/www.kenney.nl at the specific URL of http://kenney.nl/assets/space-shooter-extension
    player_image = pygame.image.load("spaceRocket.bmp")
    player_image.set_colorkey(BLACK)

    # Space object from Kenney/www.kenney.nl at the specific URL of http://kenney.nl/assets/space-shooter-extension
    satellite = pygame.image.load("satellite.bmp")
    satellite.set_colorkey(BLACK)

    #IMAGE OBJECT BIRD
    bird = pygame.image.load("bird.png")
    bird.set_colorkey(BLACK)

    #laser sound that will be played in the main program loop if the player presses the "s" key
    click_sound = pygame.mixer.Sound("laser5.ogg")
    #click_sound = pygame.mixer.Sound("254315__jagadamba__clock-tick.wav")

    #Background music by Christovix Games from https://opengameart.org/content/where-to-now
    pygame.mixer.music.load('Where to now.ogg')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

    tick = 1
 
    # -------- Main Program Loop -----------
    while not done:

        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # GAME LOGIC BEGIN

        #for loop that changes keyboard_x_speed and keyboard_y_speed by pressing keys
        #also checks if the "s" key is pressed down to make a laser sound

            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_LEFT:
                    keyboard_x_speed = -3
                elif event.key == pygame.K_RIGHT:
                    keyboard_x_speed = 3
                elif event.key == pygame.K_UP:
                    keyboard_y_speed = -3
                    upPressed = True
                elif event.key == pygame.K_DOWN:
                    keyboard_y_speed = 3
                    downPressed = True
                #plays laser sounds if user presses s key
                elif event.key == pygame.K_s:
                    if(len(satellite_coordinates) != 0):
                        pygame.mixer.music.pause()
                        satellite_coordinates.pop(random.randrange(len(satellite_coordinates)))                    
                        click_sound.play()
                        pygame.mixer.music.unpause()
         
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    keyboard_x_speed = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    keyboard_y_speed = 0
                    upPressed = False
                    downPressed = False
        #bottom bound
        if(keyboard_y_coord >= (size[1]-player_image.get_height()) and keyboard_y_speed > 0):
            keyboard_y_speed = 0
        #Top bound   
        if(keyboard_y_coord <= 0 and keyboard_y_speed < 0):
            keyboard_y_speed = 0
        #left bound
        if(keyboard_x_coord <= 0 and keyboard_x_speed < 0):
            keyboard_x_speed = 0
        #right bound
        if(keyboard_x_coord >= (size[0]-player_image.get_width()) and keyboard_x_speed > 0):
            keyboard_x_speed = 0

        if((not upPressed) and keyboard_y_coord < (size[1]-player_image.get_height()) and not downPressed):
            keyboard_y_speed = 3

            
        # Move the object according to the speed vector.
        keyboard_x_coord += keyboard_x_speed
        keyboard_y_coord += keyboard_y_speed
        
        #Get position of the mouse
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]
         
        # GAME LOGIC END
 
        # DRAW CODE BEGIN
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        #draws background
        screen.blit(background_image, [0, 0])

        #iterates through house_coordinates list to retrieve x and y coordinates then draws the houses
        for item in house_coordinates:
            house_x = item[0]
            house_y = item[1]
            draw_house(screen, house_x, house_y)
            
        #iterates through house_coordinates list to retrieve x and y coordinates then draws the houses
        for item in satellite_coordinates:
            house_x = item[0]
            house_y = item[1]
            screen.blit(satellite, [house_x, house_y])

        #draw bird
        screen.blit(bird, [25, 25])

        #draws sun object
        draw_sun(screen, mouse_x, mouse_y, 100, tick)        

        #draws cat object
        cat.draw_cat(screen, 100, 200, 2, tick)

        #Draw player object
        screen.blit(player_image, [keyboard_x_coord, keyboard_y_coord])

        #draws text with instructions and selects font
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Use the arrow keys to move the cat and press the s key to make a laser noise!" + " " + str(keyboard_x_coord) + "X" + str(keyboard_y_coord), True, WHITE)
        screen.blit(text, [300, 20])
        
        # DRAW CODE END
 
        # Update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)

        #calculate current tick
        tick+=1
        if tick == 61:tick-=60
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

 
if __name__ == "__main__":
    main()
