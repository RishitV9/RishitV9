from django.shortcuts import render
import 
from .computer_api import *

def computer(request):
    # start server:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(addr)
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
