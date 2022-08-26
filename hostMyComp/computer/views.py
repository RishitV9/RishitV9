from django.shortcuts import render
from .computer_api import *

def computer(request):
    # start server:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(addr)
        s.listen()
        conn, addr = s.accept()
        with conn:
            thr = threading.Thread(target=connection, args=[conn, addr])
            thr.start()
