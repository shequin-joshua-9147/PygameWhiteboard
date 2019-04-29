"""
Contains the base class for a Tool and all available tools(for now).

Contains the base Tool object which is a framework for all other tools, it should never
be truly called or created from another class as it is a base object meant for
parenthood.

This module also contains all of the other actual tools that will be used by the Page class.
    Marker - A simple marker that you would use on a whiteboard.
"""


class Tool:

    pass


class Marker(Tool):

    pass
