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

#define circles by a list of [x,y] coordinates

#TODO: create a variable num_circles and start the
#simulation with that many bubbles at random positions
#TODO: make the bubbles smaller and blue to look like raindrops
#TODO: play with the framerate using clock.tick and step_y to make the
#rain drops fall at a speed that looks natural.
circle_centers = [[100,300],[200,100],[300,400],[400,50]]
circle_rad = 50
screen_width = 500
screen_height = 500
step_y = 2

def update_circle_positions(screen):
    for center in circle_centers:
        #get y-coordinate
        center[1] += step_y
        #check to see if circle has fallen off the screen
        if center[1] - circle_rad > screen_height:
            #TODO: randomly set the x-coordanate each type we reset a bubble
            center[1] = -circle_rad
        pygame.draw.circle(screen, red, center, circle_rad)


# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(white)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        msElapsed = clock.tick(50)
        screen.fill(white)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        #update position of circles each time
        update_circle_positions(screen)

        pygame.display.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
