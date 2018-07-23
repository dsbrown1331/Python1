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
    screen.fill(white)
    circle_x = 100
    circle_y = 200
    circle_rad = 50
    step_x = 2
    step_y = 2
    pygame.draw.circle(screen, red, (circle_x,circle_y), circle_rad)
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        msElapsed = clock.tick(30)
        screen.fill(white)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        #To check if we've bumped into a wall
        #check if the y-coordinate is too large
        if circle_y + circle_rad >= screen_height:
            step_y = -step_y
        #check if the y-coordinate is too small
        elif circle_y - circle_rad <= 0:
            step_y = -step_y
        #check if the x_coordinate is too large
        if circle_x + circle_rad >= screen_width:
            step_x = -step_x
        #check if the x-coordinate is too small
        elif circle_x - circle_rad <= 0:
            step_x = -step_x


        #update position of circle each time
        circle_x += step_x
        circle_y += step_y
        pygame.draw.circle(screen, red, (circle_x, circle_y), circle_rad)

        pygame.display.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
