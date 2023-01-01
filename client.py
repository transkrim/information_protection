import math
import socket
import random
import decimal
from decimal import Decimal
from typing import List
from message import Message, Field, get_field_name


def read_from_file(path):
    with open(path) as f:
        res = f.readlines()
        return str.join("", res)


class Client:
    def __init__(self):
        self.client_socket = None
        if self.connect_to_server():
            self.auth()
        self.close()

    def close(self):
        self.client_socket.close()

    def get_private_key(self) -> List[int]:
        block_length = 8
        self.private_key = []
        for i in range(block_length):
            number = sum(self.private_key) + random.randint(1, 10)
            self.private_key.append(number)

        return self.private_key

    def get_public_key(self) -> List[int]:
        m = sum(self.private_key) + 2
        n = 1
        for i in range(10, 1000):
            if math.gcd(i, m) == 1:
                n = i
                break

        self.public_key = []
        for k in self.private_key:
            key = (k * n) % m
            self.public_key.append(key)

        return self.public_key

    def connect_to_server(self):
        host = socket.gethostname()
        port = 5000

        self.client_socket = socket.socket()
        print("Ожидание подключения к серверу...")
        try:
            self.client_socket.connect((host, port))
            print("Подключение успешно!")
            return True
        except:
            print("Подключение не удалось. Bye!")
            return False

    def auth(self):
        print("Начинаем процедуру аутентификации...")
        keys_str = read_from_file("../../Desktop/STUDY/Защита информации/3.0_lab/keys.txt").replace("\n", "")
        keys_obj = Message(keys_str)
        # e_obj = keys_obj.get_specific_field("e")
        # n_obj = keys_obj.get_specific_field("n")
        # d_obj = keys_obj.get_specific_field("d")
        e = 5 #e_obj.value
        n = 91 #n_obj.value
        d = 29 #d_obj.value
        mes_obj = Message()
        mes_obj.add_field(Field(get_field_name(e), e))
        mes_obj.add_field(Field(get_field_name(n), n))
        message_e_n = mes_obj.to_string()
        self.send_message(message_e_n)
        message_r = self.get_message()
        mes_r_obj = Message(message_r)
        r_obj = mes_r_obj.get_specific_field("r")
        k = self.get_k(r_obj.value, d, n)
        mes_k = Message()
        mes_k.add_field(Field(get_field_name(k)[0], float(k)))
        self.send_message(mes_k.to_string())
        message = self.get_message()

    def get_k(self, r, d, n):
        r = Decimal(r)
        d = Decimal(d)
        n = Decimal(n)
        k = Decimal((r ** d) % n)
        return k

    def send_message(self, message):
        message = str(message)
        print("Отправленное сообщение: " + message)
        self.client_socket.send(message.encode())

    def get_message(self):
        message = self.client_socket.recv(1024).decode()
        print("Входящее сообщение: " + str(message))
        return message


if __name__ == '__main__':
    decimal.getcontext().prec = 1000000
    client = Client()
