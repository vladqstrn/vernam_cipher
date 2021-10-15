import console_view


class Controller:
    def __init__(self, view, encrypter, descriptor):
        self.view = view
        self.encrypter = encrypter
        self.descriptor = descriptor

    def run(self):
        self.view.show_menu()
        self.menu_choice()

    def menu_choice(self):
        self.view._ask_choice_menu()
        choice = int(input())
        
        if choice == 1:
            self.view._ask_message()
            message = input()
            print(self.encrypter.process_enryption(message))