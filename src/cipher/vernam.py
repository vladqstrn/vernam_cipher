import random
import string


class VernamEncrypter:
    """Класс для шифрования методом Вернама"""

    def __init__(self, message):
        self.message = message

    def _chr_to_binary(self, data) -> list:
        """Перевод сообщения в двоичную систему счисления"""
        binary_list = []
        for x in data:
            binary_list.append(bin(ord(x)))
        return binary_list

    def _generate_key(self) -> list:
        """Создание случайного ключа"""
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(len(self.message)))
        key_binary = self._chr_to_binary(key)
        return key, key_binary

    def _encryption(self, message, key) -> list:
        """Сложение по модулю 2"""
        buff = []
        for i in range(len(message)):
            buff.append(int(message[i], 2) ^ int(key[i], 2))
        return buff

    def _sum(self, data) -> list:
        """Вывод двоичного шифрованного сообщения"""
        sum = []
        for i in range(len(data)):
            sum.append('{0:0b}'.format(data[i]))
        return sum

    def _encripted_message(self, data) -> str:
        """Вывод шифрованного сообщения в формате ascii"""
        buff = []
        for x in range(len(data)):
            buff.append(chr(data[x]))
        return ''.join(buff)
    
    def process_enryption(self) -> list:
        binary_message = self._chr_to_binary(self.message)
        key, key_binary = self._generate_key()
        enc = self._encryption(binary_message ,key_binary)
        log_enc = self._sum(enc)
        log_enc_ascii = self._encripted_message(enc)
        return enc, key, key_binary, log_enc, log_enc_ascii
        


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

test = VernamEncrypter('hello')
#print(test.process_enryption())
# test = VernamEncrypter('he', 11)
# binary_message = test.chr_to_binary('hello world')
# binary_key = test.generate_key()
# print('message - ',binary_message)
# print('key - ', binary_key)
# a = test.encryption(binary_message, binary_key)
# print('this is xor-----------',a)
# b = (test.sum(a))
# print('this is byte xor---------', b)
# cript = (test.encripted_message(a))
# print('this is cripr', cript)

# f = VernamDescriptor(cript)
# d = f.convert_ascii_to_binary()
# print('this is binary',d)
# ff = test.encryption(d,binary_key)
# print(f.return_decrypted_message(ff))
