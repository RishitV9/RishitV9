import subprocess
import socket
import core.settings


def run_command(command):
    result = subprocess.run(command.split(), stdout=subprocess.PIPE)
    return result.stdout


def detect_next_press():
    while True:
        key = keyboard.read_key()
        if key:
            return key


MAX_CMD_LENGHT = run_command("getconf ARG_MAX")
addr = (settings.ALLOWED_HOSTS[0], custom_port)
