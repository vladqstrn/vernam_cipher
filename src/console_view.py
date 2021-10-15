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

