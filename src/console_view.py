class ConsoleView:
    def __init__(self):
        self.menu_items = [
            "Зашифровать сообщение",
            "Расшифровать сообщение"
            "Выход"
        ]

    def _generate_menu(self):
        """
        Создаёт меню из элементов menu_item
        """
        return "\n" + "".join([str(index + 1) + ". " + item + "\n" for index, item in enumerate(self.menu_items)])
    
    def menu_choice(self):
        choice = int(input("Выберите вариант: "))
        return choice
    
    def show_menu(self):
        menu = self._generate_menu()
        print(menu)
