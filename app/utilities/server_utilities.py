import os
import shlex
import subprocess


class ServerUtilities(object):
    def __init__(self):
        self._is_on = False

    def turn_on(self):
        """
        Turn on server
        :return: (bool)
        """
        pass

    def turn_off(self):
        """
        Turn off server
        :return: (bool)
        """
        pass

    def who_is_on(self):
        """
        Returns players in server
        :return: (list)
        """
        pass

    def is_players(self):
        """
        Are there players in server
        :return: (bool)
        """
        pass
