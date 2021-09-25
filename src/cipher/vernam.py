import random
import string
class Encrypt:
    def __init__(self, message, key_len):
        self.message = message
        self.key_len = key_len

    def chr_to_binary(self,message) -> list:
        "Перевод сообщения в двоичную систему счисления"
        binary_list =[]
        for x in bytearray(message, 'utf-8'):
            binary_list.append(format(x,'b'))
        return binary_list

    def generate_key(self) -> list:
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        key = ''.join(random.choice(alphabet) for _ in range(self.key_len))
        key = self.chr_to_binary(key)
        return key

    
    def encryption(self, massage, key):
        for i,j in enumerate(range(len(massage))):
            print(massage[i][j])            
        
        

test = Encrypt('hello', 5)
binary_massage = test.chr_to_binary('hello')
binary_key = test.generate_key()
print('massage - ',binary_massage)
print('key - ', binary_key)
print(test.encryption(binary_massage, binary_key))