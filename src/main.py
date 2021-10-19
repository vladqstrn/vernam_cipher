import vernam
import controller
import console_view

if __name__ == '__main__':
    cv = console_view.ConsoleView()
    encrypter = vernam.VernamEncrypter()
    descriptor = vernam.VernamDescriptor()
    app = controller.Controller(cv, encrypter, descriptor)

    app.run()