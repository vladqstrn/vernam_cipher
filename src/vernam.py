import random
import string


class VernamEncrypter:
    """Класс для шифрования методом Вернама"""

    def __init__(self):
        self.alphabet_eng = string.ascii_lowercase + string.ascii_uppercase
        self.alphabet_rus = ''.join([chr(i) for i in range(1040,1040+64)])
        self.alphabet = self.alphabet_eng + self.alphabet_rus + string.punctuation + string.digits
        self.alphabet_dict = {key : char for key, char in enumerate(self.alphabet)}

    def _chr_to_binary(self, data) -> list:
        """Перевод сообщения в двоичную систему счисления"""
        binary_list = []
        for x in data:
            binary_list.append(bin(ord(x)))
        return binary_list

    def _generate_key(self, message) -> list:
        """Создание случайного ключа"""
        alphabet = string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(len(message)))
        key_binary = self._chr_to_binary(key)
        return key, key_binary

    def _encryption(self, message, key) -> list:
        """Сложение по модулю 2"""
        buff = []
        for i in range(len(message)):
            buff.append(int(message[i], 2) ^ int(key[i], 2))
        return buff

    def _int_to_binary(self, data) -> list:
        """Вывод двоичного шифрованного сообщения"""
        sum = []
        for i in range(len(data)):
            sum.append(bin(data[i]))
        return sum

    def _encripted_message(self, data) -> str:
        """Вывод шифрованного сообщения в формате ascii"""
        message_buff = []
        for i in data:
            if i in self.alphabet_dict.keys():
                message_buff.append(self.alphabet_dict[i])
        return ''.join(message_buff)

    def process_encryption(self, message) -> list:
        binary_message = self._chr_to_binary(message)
        key, key_binary = self._generate_key(message)
        xor = self._encryption(binary_message ,key_binary)
        binary_xor = self._int_to_binary(xor)
        binary_xor_to_ascii = self._encripted_message(xor)
        return binary_message, xor, key, key_binary, binary_xor, binary_xor_to_ascii
        


class VernamDescriptor(VernamEncrypter):
    """
    Класс для расшифрования сообщения
    """

    def __init__(self):
        super().__init__()

    def convert_char_to_int(self, data) -> list:
        buff = []
        for i in data:
            for key, char in self.alphabet_dict.items():
                if i == char:
                    buff.append(bin(key))
        return buff

    def int_to_ascii(self, data) -> str:
        """Возвращает расшифрованное сообщение"""
        buff = []
        for i in range(len(data)):
            buff.append(chr(data[i]))
        return ''.join(buff)
    
    def process_description(self, data, key):
        message_bin = self.convert_char_to_int(data)
        key_bin = self._chr_to_binary(key)
        xor = self._encryption(message_bin, key_bin)
        descripted_message = self.int_to_ascii(xor)
        return descripted_message