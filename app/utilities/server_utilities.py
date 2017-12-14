import shlex
import subprocess


class ServerUtilities(object):
    def __init__(self):
        self._is_on = False

    # todo: Update with RAM alottment
    # todo: Print error with log error
    def turn_on(self):
        """
        Turn on server
        :return: (bool)
        """
        if not self._is_on:
            command = 'java -jar minecraft_server.jar nogui'
            sh_command = shlex.split(command)
            execute = subprocess.Popen(sh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = execute.communicate()
            if not stderr:
                self._is_on = True
                return True
            else:
                print 'Error, cannot turn on server.'
        return False

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
