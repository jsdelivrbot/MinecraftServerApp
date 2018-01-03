import shlex
import subprocess
import io
import random
import string
from interruptingcow import timeout
import time
import socket


class ServerUtilities(object):
    MC_SERVER_DIR = '/opt/minecraft/server'
    SCREEN_NAME = 'minecraft_server_screen'
    SCREEN_LOG = 'screen_log'
    LOG_NAME = 'screenlog.0'
    MAX_RUNTIME = 30  # 30 seconds

    def __init__(self):
        self._is_on = ServerUtilities.is_on()
        self._unique_id = ''

    # todo: Update with RAM alottment
    # todo: Print error with log error
    # todo: Make screen commands a decorator
    # todo: Can also probably make a shell command decorator
    def turn_on(self):
        """
        Approach: Creating an attached terminal screen thru 'screen' functionality and issuing commands.
        Success of commands will be read through log.

        screen -S <screen_name> -L (attached screen with logging)

        Turn on server
        :return: (bool)
        """
        if not self._is_on:
            # turning on server
            # comment: Super janky, but want to search only applicable log entries so we use
            # comment: a special process id to show when the output of a command started
            self._unique_id = ServerUtilities.generate_unique_id(length=32)

            command = 'sudo java -jar {mc_server_dir}/minecraft_server.1.12.2.jar nogui'.format(
                mc_server_dir=ServerUtilities.MC_SERVER_DIR,
            )
            execute = ServerUtilities.issue_attached_screen_command(
                cmd=command,
                unique_id=self._unique_id,
            )

            # execute returns True if nothing went wrong.  Now get tail of log and find out if screen had any errors
            if execute:
                is_execute_success = ServerUtilities.is_execute_success(
                    success='Done',
                    error='error',
                    unique_id=self._unique_id,
                )
                self._is_on = is_execute_success
                return is_execute_success
            else:
                print 'Error, cannot turn on server.'
        return False

    def turn_off(self):
        """
        Turn off server
        :return: (bool)
        """
        if self._is_on:
            mc_cmd = 'stop'
            self._unique_id = ServerUtilities.generate_unique_id(length=32)
            execute = ServerUtilities.issue_attached_screen_command(mc_cmd, self._unique_id)
            if execute:
                is_execute_success = ServerUtilities.is_execute_success(
                    success='Stopping the server',
                    error='Error',
                    unique_id=self._unique_id,
                )
                self._is_on = (not is_execute_success)
                return is_execute_success
            else:
                print 'Error, cannot turn off server'
        return False

    @staticmethod
    def is_on():
        """
        Returns bools indicating if server is on or off
        :return: (bool)
        """
        response = False
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", 25565))

        except socket.error as error:
            if error.errno == 98:
                print 'error is {}'.format(error)
                response = True
            else:
                print('Error when checking socket, error: {}'.format(error))

        s.close()
        return response

    def who_is_on(self):
        """
        Returns players in server
        :return: (list)
        """
        mc_cmd = 'list'
        self._unique_id = ServerUtilities.generate_unique_id(length=32)
        pass

    def is_players(self):
        """
        screen -S minecraft -X stuff '<command>'`echo -ne '\015'`

        Are there players in server
        :return: (bool)
        """
        mc_cmd = 'list'
        self._unique_id = ServerUtilities.generate_unique_id(length=32)
        pass

    @staticmethod
    def screen_log_cleanup():
        """
        :return:
        """
        command = 'sudo rm -rf {mc_server_dir}/{screen_log}/screenlog.0'.format(
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
    # screen -r "minecraft_server_screen" -X stuff "echo hello"`echo -ne "\015"`
    @staticmethod
    def issue_attached_screen_command(cmd, unique_id='noID'):
        """
        :param cmd: (str) Sh command
        :param unique_id: (str) unique id for remote screen command
        :return:
        """
        time.sleep(0.25)
        screen_id= "screen -r '{screen_name}' -X stuff '{id}'".format(
            screen_name=ServerUtilities.SCREEN_NAME,
            id=unique_id
        )
        execute = subprocess.Popen(
            shlex.split(screen_id),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )
        execute.communicate()

        time.sleep(0.25)
        enter_command = 'screen -r "{screen_name}" -X stuff "{enter}"'.format(
            screen_name=ServerUtilities.SCREEN_NAME,
            enter='\015',
        )
        execute = subprocess.Popen(
            shlex.split(enter_command),
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        execute.communicate()

        time.sleep(0.25)
        screen_command = "screen -r '{screen_name}' -X stuff '{cmd}'".format(
            screen_name=ServerUtilities.SCREEN_NAME,
            cmd=cmd,
        )
        execute = subprocess.Popen(
            shlex.split(screen_command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )
        execute.communicate()

        enter_command = 'screen -r "{screen_name}" -X stuff "{enter}"'.format(
            screen_name=ServerUtilities.SCREEN_NAME,
            enter='\015',
        )
        execute = subprocess.Popen(
            shlex.split(enter_command),
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = execute.communicate()

        if stderr:
            print 'Error when fetching tail of screen log'
            return False
        return True

    @staticmethod
    def is_execute_success(success, error, unique_id):
        """
        Probably need something like this inconjunction to stream_screen_log_by_id()
        :return:
        """
        for log_line in ServerUtilities.stream_screen_log_by_id(success, error, unique_id):
            if error in log_line:
                return False
            elif success in log_line:
                return True
        return False

    @staticmethod
    def stream_screen_log_by_id(success, error, unique_id='noID'):
        """
        Streams tail of log file for a set period of time before timing out.
        :return: Returns
        """
        try:
            with io.open(file='{mc_server_dir}/{screen_log}/screenlog.0'.format(
                mc_server_dir=ServerUtilities.MC_SERVER_DIR,
                screen_log=ServerUtilities.SCREEN_LOG
            ),
                mode='rt',
            ) as log, timeout(ServerUtilities.MAX_RUNTIME, exception=RuntimeError):

                start_sending = False
                while True:
                    line = log.readline()
                    if start_sending and line:
                        yield line
                    elif unique_id in line:
                        start_sending = True

        except RuntimeError:
            print('Run time was exceeded.')
            yield False

        except Exception as error:
            print('Other error in stream tail screen log', error)
            yield False

    @staticmethod
    def generate_unique_id(length=32):
        """
        :return: Returns super crazy unique process id
        """
        _id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])
        return _id
