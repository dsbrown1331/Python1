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

colors = [red, green, blue, darkBlue, white, black, pink]

#define circles by a list of [x,y] coordinates




# define a main function
def main():

    x_pos = 250
    y_pos = 250
    radius = 50
    screen_width = 500
    screen_height = 500
    speed = 5

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
            # if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            #check if a key was pressed
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_pos -= speed
            #     if event.key == pygame.K_RIGHT:
            #         x_pos += speed
            #     if event.key == pygame.K_UP:
            #         y_pos -= speed
            #     if event.key == pygame.K_DOWN:
            #         y_pos += speed
        #update position of circles each time
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x_pos -= speed
            if x_pos < 0:
                x_pos = screen_width
        if keys[pygame.K_RIGHT]:
            x_pos += speed
            if x_pos > screen_width:
                x_pos = 0
        if keys[pygame.K_UP]:
            y_pos -= speed
            if y_pos < 0:
                y_pos = screen_height
        if keys[pygame.K_DOWN]:
            y_pos += speed
            if y_pos > screen_height:
                y_pos = 0
        pygame.draw.circle(screen, blue, (x_pos, y_pos), radius)

        pygame.display.update()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
