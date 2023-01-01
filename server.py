import socket
import decimal
from decimal import Decimal
from message import Message, Field, get_field_name


class Server:
    def __init__(self):
        self.server_socket = None
        self.client = self.listen_for_client()
        self.auth()
        self.close()

    def close(self):
        self.client.close()
        self.server_socket.close()

    def auth(self):
        message = self.get_message()
        mes = Message(message)
        e = mes.get_specific_field("e")
        n = mes.get_specific_field("n")
        r, k = self.get_r_k(e.value, n.value)
        print("Начальный k = " + str(k))
        mes1 = Message()
        mes1.add_field(Field(get_field_name(r)[0], float(r)))
        self.send_message(mes1.to_string())
        message = self.get_message()
        mes_k = Message(message)
        received_k = mes_k.get_specific_field("k").value
        if k == received_k:
            message = "Аутентификация успешно пройдена!"
        else:
            message = "Ошибка! Аутентификация не пройдена!"
        self.send_message(message)

    def get_r_k(self, e, n):
        k = 23 # random.randint(1, n - 1)
        e = Decimal(e)
        n = Decimal(n)
        k = Decimal(k)
        r = Decimal((k ** e) % Decimal(n))
        return r, k

    def listen_for_client(self):
        host = socket.gethostname()
        port = 5000

        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))

        self.server_socket.listen(10)
        print("Слушаем входящие подключения...")
        conn, address = self.server_socket.accept()
        print("Новое подключение от: " + str(address))
        return conn

    def send_message(self, message):
        message = str(message)
        self.client.send(message.encode())

    def get_message(self):
        message = self.client.recv(1024).decode()
        print("Входящее сообщение: " + str(message))
        return message


if __name__ == '__main__':
    decimal.getcontext().prec = 1000000
    server = Server()