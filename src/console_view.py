class ConsoleView:
    def __init__(self):
        self.menu_items = [
            "Зашифровать сообщение",
            "Расшифровать сообщение",
            "Выход"
        ]

    def _generate_menu(self):
        """
        Создаёт меню из элементов menu_items
        """
        return "\n" + "".join([str(index + 1) + ". " + item + "\n" for index, item in enumerate(self.menu_items)])

    def _ask_choice_menu(self):
        print('Выберите вариант: ')
    
    def _ask_message(self):
        print('Введите сообщение: ')
        

    def show_menu(self):
        menu = self._generate_menu()
        print(menu)
    
    def _ask_log(self):
        print('Показать лог?\n1 - Да\n0 - Нет')
    
    def _print_log(self,  binary_message, xor, binary_key, binary_encripted_message):
        print(binary_message, 'Двоичное сообщение\n',\
            binary_key, 'Двоичный ключ\n',\
            binary_encripted_message, 'Зашифрованное двоичное сообщение\n',
            xor, 'XOR'
            )
    
    def _encription_log(self, key, ascii_message):
        print(
            key, ' - Ключ\n',\
            ascii_message, 'Зашифрованное сообщение\n'
            )
    
    def _start_description_menu(self):
        print('Введите сообщение\nВведите ключ')

    def _return_descripted_message(self, message):
        print(message, '- сообщение')
