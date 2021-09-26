import random
import string


class VernamEncrypter:
    ''''Класс для шифрования методом Вернама'''

    def __init__(self, message, key_len):
        self.message = message
        self.key_len = key_len
        pass

    def chr_to_binary(self,message) -> list:
        "Перевод сообщения в двоичную систему счисления"
        binary_list =[]
        for x in message:
            binary_list.append(bin(ord(x)))
        return binary_list

    def generate_key(self) -> list:
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(self.key_len))
        key = self.chr_to_binary(key)
        return key

    def encryption(self, message, key):
        buff = []
        for i in range(len(message)):
            buff.append(int(message[i],2) ^ int(key[i],2))
        return buff
        
        
    def sum(self, a):
        sum = []
        for i in range(len(a)):
            sum.append('{0:0b}'.format(a[i]))
        return sum
    
    def encripted_message(self, a):
        buff = []
        for x in range(len(a)):
            buff.append(chr(a[x]))
        return ''.join(buff)

test = VernamEncrypter('he', 11)
binary_message = test.chr_to_binary('hello world')
binary_key = test.generate_key()
print('message - ',binary_message)
print('key - ', binary_key)
a = test.encryption(binary_message, binary_key)
print('this is a-----------',a)
b = (test.sum(a))
print('this is b---------', b)
cript = (test.encripted_message(a))
print(cript)



#print(bin(ord(bytearray(a))))

#print(a)
#a = (bin(ord('a')))
#b = (bin(ord('b')))
# res = int(a, 2) ^ int(b, 2)
# print(a, b)
#print('{0:0{1}b}'.format(int(a), len(a)))
# res = int(res)
# print(chr(res))

class VernamDescriptor():
    def __init__(self, cript_message):
        self.cript_message = cript_message
    def cript(self):
        print(len(self.cript_message))#for i in range(len(self.cript_message)):

f = VernamDescriptor(cript)
f.cript()