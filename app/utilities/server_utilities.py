import shlex
import subprocess
import re


class ServerUtilities(object):
    MC_SERVER_DIR = '/opt/server/minecraft'
    SCREEN_NAME = 'minecraft_server'
    SCREEN_LOG = 'screen_log'

    def __init__(self):
        self._is_on = False

    # todo: Update with RAM alottment
    # todo: Print error with log error
    # todo: Make screen commands a decorator
    # todo: Can also probably make a shell command decorator
    # todo: replace error regex search
    def turn_on(self):
        """
        Approach: Creating an attached terminal screen thru 'screen' functionality and issuing commands.
        Success of commands will be read through log.

        screen -S <screen_name> -L (attached screen with logging)

        Turn on server
        :return: (bool)
        """
        if not self._is_on:
            # create attached screen
            self.create_screen()

            # turning on server
            command = 'sudo java -jar {mc_server_dir}/minecraft_server.1.12.2.jar nogui'.format(
                mc_server_dir=ServerUtilities.MC_SERVER_DIR,
            )
            execute = ServerUtilities.issue_attached_screen_command(cmd=command)

            # execute returns True if nothing went wrong.  Now get tail of log and find out if screen had any errors
            if execute:
                log_tail = ServerUtilities.tail_screen_log(num_of_lines=1)
                # do some regex search for value
                is_success = (not re.match('look for error syntax', log_tail, flags=re.IGNORECASE))
                if is_success:
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
        mc_cmd = 'stop'
        pass

    def who_is_on(self):
        """
        Returns players in server
        :return: (list)
        """
        mc_cmd = 'list'
        pass

    def is_players(self):
        """
        screen -S minecraft -X stuff '<command>'`echo -ne '\015'`

        Are there players in server
        :return: (bool)
        """
        mc_cmd = 'list'
        pass

    @staticmethod
    def screen_log_cleanup():
        """
        :return:
        """
        command = 'rm -rf {mc_server_dir}/{screen_log}'.format(
            mc_server_dir=ServerUtilities.MC_SERVER_DIR,
            screen_log=ServerUtilities.SCREEN_LOG,
        )

        sh_command = shlex.split(command)
        execute = subprocess.Popen(sh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = execute.communicate()
        if stderr:
            print 'screen log cleanup error'
            return False
        return True

    @staticmethod
    def issue_attached_screen_command(cmd):
        """
        :param cmd: (str) Sh command
        :return:
        """
        screen_command = 'screen -S {screen_name} -X stuff "{cmd}"`echo -ne "\015"`'.format(
            screen_name=ServerUtilities.SCREEN_NAME,
            cmd=cmd,
        )

        sh_screen_command = shlex.split(screen_command)
        execute = subprocess.Popen(sh_screen_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = execute.communicate()
        if stderr:
            print 'Error when fetching tail of screen log'
            return False
        return True

    @staticmethod
    def tail_screen_log(num_of_lines=1):
        """
        :param num_of_lines: (int) Fetch 'n' lines from tail of log
        :return:
        """
        command = 'tail -n {num_of_lines} {mc_server_dir}/{screen_log}'.format(
            num_of_lines=num_of_lines,
            mc_server_dir=ServerUtilities.MC_SERVER_DIR,
            screen_log=ServerUtilities.SCREEN_LOG,
        )

        sh_command = shlex.split(command)
        execute = subprocess.Popen(sh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = execute.communicate()
        if stderr:
            print 'Error when fetching tail of screen log'
            return False
        return stdout

    @staticmethod
    def create_screen():
        """
        Switches to screen_log dir and then creates screen.
        Creating a screen with the log param (-L) will create a screenlog.<NUM> at the cwd
        :return: (bool)
        """
        # super janky, but I'm not finding a way around this
        command = 'cd {mc_server_dir}/{screen_log} && screen -S {screen_name} -L'.format(
            mc_server_dir=ServerUtilities.MC_SERVER_DIR,
            screen_name=ServerUtilities.SCREEN_NAME,
            screen_log=ServerUtilities.SCREEN_LOG,
        )
        sh_command = shlex.split(command)
        execute = subprocess.Popen(sh_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = execute.communicate()
        if stderr:
            print 'Error when creating screen!'
            return False
        return True
