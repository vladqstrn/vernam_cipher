def console_menu():
    print('Шифр Вернама')
    message = (input("Введите сообщение"))
    key_len = len(message)
    enc_res= vernam.VernamEncrypter(message, key_len)
