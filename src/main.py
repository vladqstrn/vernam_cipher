from app import viewConsole
from cipher import vernam


def main():
    message = input('Введите сообщение: ')
    encription = vernam.VernamEncrypter(message)
    enc, key, key_binary, log_enc, log_enc_ascii = encription.process_enryption()
    print(enc, key, key_binary, log_enc, log_enc_ascii)

if __name__ == "__main__":
    main()