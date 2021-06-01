
# Import a library of functions called 'pygame'
import pygame
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
 
# Set the height and width of the screen
size   = [400, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)
 
pygame.display.set_caption("Game Title")
  
#Loop until the user clicks the close button.
done  = False
flag  = None
clock = pygame.time.Clock()
 
# print text function
def printText(msg, color='BLACK', pos=(50, 50)):
    textSurface      = font.render(msg, True, pygame.Color(color), None)
    textRect         = textSurface.get_rect()
    textRect.topleft = pos
 
    screen.blit(textSurface, textRect)
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    # Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.MOUSEBUTTONDOWN: # If user release what he pressed.
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP: # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:  # If user clicked close.
            done = True                  
 
     
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Print red text if user pressed any key.
    if flag == True:
        printText('you just mouse down!!', 'RED')
        printText('--> you pressed your', 'RED', (50, 70))
        printText('    left mouse button.', 'RED', (50, 90))
 
    # Print blue text if user released any key.
    elif flag == False:
        printText('you just mouse up!!', 'BLUE')
        printText('--> released what you pressed.', 'BLUE', (50, 70))
 
    # Print default text if user do nothing.
    else:
        printText('Please press any key.')
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
