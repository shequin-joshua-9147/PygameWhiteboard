"""
This module contains everything that a Bundle needs to function.

First it contains Bundle, which hold a variable amount of pages.
Second it contains the class for a Page, which is where we do all of our actual whiteboard
work. Something to note is that this module does not contain tools that the Page will
use, instead those will be in the Tool module.
"""
import tools
import pygame


class Bundle:

    def __init__(self, screen, save_location=None, name="New Bundle"):

        self.name = ""
        self.pages = []
        self.current_page = 0
        self.screen = screen

        if save_location is None:
            self.new_bundle(name)

    def new_bundle(self, name):

        self.name = "New Bundle"
        self.pages = [Page(name="New Page")]

    def step(self, events, mouse_info):
        self.pages[self.current_page].step(events, mouse_info, self.screen)


class Page:

    def __init__(self, name=None):

        self.name = name
        self.tool = tools.Marker()

        self.mouse_one_down = False

    def step(self, events, mouse_info, screen):

        if mouse_info[1][0] == 1:
            self.mouse_one_down = True
            self.tool.action(screen, mouse_info[0][0], mouse_info[0][1])
        else:
            if self.mouse_one_down:
                self.tool.end_action(screen, mouse_info[0][0], mouse_info[0][1])
            self.mouse_one_down = False

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DELETE:
                    screen.fill((255, 255, 255))
