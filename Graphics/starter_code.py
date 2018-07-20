#Read through https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
# import the pygame module, so you can use it
import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    #paint the screen white
    screen.fill(white)
    #draw a circle
    circle_x = 50
    circle_y = 50
    circle_rad = 50
    pygame.draw.circle(screen, red, (circle_x,circle_y), circle_rad)
    #update the screen
    pygame.display.update()


    # define a variable to control the main loop
    running = True

    # main loop
    while running:

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        #paint screen white


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
