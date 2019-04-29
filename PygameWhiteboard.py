"""
Main file, that you run, for PygameWhiteboard.

You run this file but it really doesn't do anything special code wise.
It creates and initializes a pygame window and creates a frame object and overlays
it on top of our pygame window. It also runs the main loop for the program.

Most of the functionality lives within the frame object.
"""
import pygame
import frame

background_color = (255, 255, 255)  # white color
width, height = 1200, 800  # default size of our window
screen = pygame.display.set_mode((width, height))  # create window
pygame.display.set_caption("Pygame Whiteboard")  # Set our window title
screen.fill(background_color)  # make our background white
pygame.display.flip()  # make the background change to the window

if __name__ == '__main__':
    running = True  # running variable, if False end

    default_frame = frame.Frame(width, height, screen)

    while running:
        events = pygame.event.get()
        for event in events:
            # look the receives all Pygame events as event
            if event.type == pygame.QUIT:
                # hitting the red X
                running = False
        default_frame.step(events)
        pygame.display.update()  # how we make Pygame draw the actual window changes
