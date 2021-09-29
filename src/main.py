from cipher import vernam


def main():
    message = input('Введите сообщение: ')
    key = vernam.VernamEncrypter.generate_key(len(message))
    enc = vernam.VernamEncrypter(message, key)    

if __name__ == "__main__":
    main()