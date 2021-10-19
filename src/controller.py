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
            self._start_encription()   
        if choice == 2:
            self._start_description()
    
    def _start_encription(self):
        self.view._ask_message()
        message = input()
        binary_message, xor, key, binary_key, binary_encripted_message, ascii_message = self.encrypter.process_encryption(message)
        self.view._encription_log(key, ascii_message)
        self.view._ask_log()
        log = int(input())
        if log == 1:
            self.view._print_log(binary_message,xor,binary_key, binary_encripted_message)
        else:
            exit(0)

    def _start_description(self):
        self.view._start_description_menu()
        message = input()
        key = input()
        descripted_message = self.descriptor.process_description(message, key)
        self.view._return_descripted_message(descripted_message)