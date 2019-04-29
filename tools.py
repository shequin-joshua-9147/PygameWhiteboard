"""
Contains the base class for a Tool and all available tools(for now).

Contains the base Tool object which is a framework for all other tools, it should never
be truly called or created from another class as it is a base object meant for
parenthood.

This module also contains all of the other actual tools that will be used by the Page class.
    Marker - A simple marker that you would use on a whiteboard.
"""
import pygame


class Tool:

    def __init__(self):

        self.color = (0, 0, 0)

    def action(self, screen, x, y):

        pass

    def end_action(self, screen, x, y):

        pass


class Marker(Tool):

    def __init__(self):
        super().__init__()

        self.size = 3

        self.actioning = False
        self.last_location = None

    def action(self, screen, x, y):
        super().action(screen, x, y)

        if self.actioning and (x, y) != self.last_location:
            xdif = x - self.last_location[0]
            ydif = y - self.last_location[1]
            xratio = 1
            xcount = 0
            yratio = 1
            ycount = 0
            if xdif > ydif and xdif != 0:
                yratio = ydif/xdif
            elif xdif > ydif and xdif == 0:
                yratio = 1
            elif ydif > xdif and ydif != 0:
                xratio = xdif/ydif
            elif ydif > xdif and ydif == 0:
                xratio = 1

            while xcount != xdif and ycount != ydif:
                xcount += xratio
                ycount += yratio
                pygame.draw.circle(screen, self.color, (self.last_location[0]+int(xcount),
                                                        self.last_location[1]+int(ycount)), self.size)

        pygame.draw.circle(screen, self.color, (x, y), self.size)
        self.last_location = (x, y)
        self.actioning = True

    def end_action(self, screen, x, y):
        super().end_action(screen, x, y)

        self.actioning = False
        self.last_location = None
