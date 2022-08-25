import subprocess
import socket
import core.settings

def run_command(command):
    result = subprocess.run(command.split(), stdout=subprocess.PIPE)
    return result.stdout

addr = (settings.ALLOWED_HOSTS[0], custom_port)
