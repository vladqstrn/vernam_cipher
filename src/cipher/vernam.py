import random
import string


class VernamEncrypter:
    """Класс для шифрования методом Вернама"""

    def __init__(self, message, key_len):
        self.message = message
        self.key_len = key_len

    def chr_to_binary(self, message) -> list:
        """Перевод сообщения в двоичную систему счисления"""
        binary_list = []
        for x in message:
            binary_list.append(bin(ord(x)))
        return binary_list

    def generate_key(self) -> list:
        """Создание случайного ключа"""
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(self.key_len))
        key = self.chr_to_binary(key)
        return key

    def encryption(self, message, key) -> list:
        """Сложение по модулю 2"""
        buff = []
        for i in range(len(message)):
            buff.append(int(message[i], 2) ^ int(key[i], 2))
        return buff

    def sum(self, a) -> list:
        """Вывод двоичного шифрованного сообщения"""
        sum = []
        for i in range(len(a)):
            sum.append('{0:0b}'.format(a[i]))
        return sum

    def encripted_message(self, a) -> str:
        """Вывод шифрованного сообщения в формате ascii"""
        buff = []
        for x in range(len(a)):
            buff.append(chr(a[x]))
        return ''.join(buff)


class VernamDescriptor(VernamEncrypter):
    """
    Класс для расшифрования сообщения
    """
    def __init__(self, cript_message):
        self.cript_message = cript_message

    def convert_ascii_to_binary(self) -> list:
        """"Перевод из формата ascii в двоичный код"""
        buff = []
        for i in range(len(self.cript_message)):
            buff.append(bin(ord(self.cript_message[i])))
        return buff

    def return_decrypted_message(self, binary_message) -> str:
        """Возвращает расшифрованное сообщение"""
        decrypted_buff = []
        for i in range(len(binary_message)):
            decrypted_buff.append(chr(binary_message[i]))
        return ''.join(decrypted_buff)
