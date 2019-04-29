"""
The main frame for our program.

This is closer to an Abstract class as there will only be one, but we won't actually treat
it as an abstract in Python. This module will contain all of the main functionality of our
program, mainly by including and sending inputs to, and receiving directions from, the
other connected parts.
"""


class Frame:
    """
    Our main frame!

    Has the functionality of:
        new_bundle(name) - Creates a new bundle and changes our current page.
        save_bundle(save_as) - Saves our current bundle as the save_as.
        load_bundle(location) - Loads a new bundle from the location.
        bundle_not_found(location) - Called if a file was not found or was not a bundle file etc.
        step() - calls our frame to do its step(what it does every time the while loop goes round.
    """
    def __init__(self, width, height, screen):
        """Construct our Frame Class."""
        self.width = width
        self.height = height
        self.screen = screen

        self.currentBundle = None

    def new_bundle(self, name):
        """
        Produce a new bundle and change our current Frame bundle.
        :param name: String. Name of the new bundle you desire.
        :return: None
        """
        pass

    def save_bundle(self, save_as):
        """
        Save our current bundle with the name of save_as.
        :param save_as: String. What you want to save your bundle as.
        :return: None
        """
        pass

    def load_bundle(self, location):
        """
        Load a new bundle based on the location given.
        :param location: String. The file path for the file you want to load.
        :return: None
        """
        pass

    def bundle_not_found(self, location):
        """
        Call when this program fails to open a bundle at a given location.
        :param location: String. Location that was not found or was not a bundle type save.
        :return: None
        """
        pass

    def step(self):
        """
        Our step function for the frame class. This is called for every update our
        windows checks for.
        :return: None
        """
        pass