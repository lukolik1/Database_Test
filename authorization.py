from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor
import sys


from database.connect_bd_1 import Connect_bd
from  MianForm import  MainWindow


class Aauthorization(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Аутентификация')
        self.setWindowIcon(QIcon('ФОТО/hacker.jpg'))
        font = QFont("SansSerif", 14)

        # Создаем свои переменные цвета
        color_lightblue = QColor(173, 216, 230)  # Цвет lightblue

        self.setStyleSheet("background-color: " + color_lightblue.name() + ";")  # Устанавливаем цвет фона окна

        lable_login = QLabel("Логин:", self)
        lable = QLabel("Аутентификация", self)
        lable_password = QLabel("Пароль:", self)

        lable_login.setFont(font)
        lable.setFont(font)
        lable_password.setFont(font)


        # Создаем поле для ввода пароля, логина и базы данных
        self.textbox_login = QLineEdit(self)
        self.password_field = QLineEdit(self)


        # Устанавливаем режим отображения пароля
        self.password_field.setEchoMode(QLineEdit.Password)

        self.btn1 = QPushButton("Войти", self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.clicked.connect(self.Connect_bd)

        quit_button = QPushButton("Выход", self)
        quit_button.resize(self.btn1.sizeHint())
        quit_button.clicked.connect(QCoreApplication.instance().quit)

        # расположение элементов
        quit_button.move(220, 200)  # Увеличиваем координату Y для новой кнопки
        self.btn1.move(0, 200)  # Увеличиваем координату Y для кнопки "Войти"

        lable.move(100, 20)

        lable_login.move(100, 50)

        lable_password.move(100, 90)


        self.textbox_login.move(100, 70)

        self.password_field.move(100, 110)

       

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(300, 250)  # Увеличиваем высоту окна

    def ShowMainForm(self):
        self.mainForm = MainWindow()
        self.mainForm.show()

    def Connect_bd(self):
        """
        Метод для подключения к базе данных.
        """
        username = self.textbox_login.text()
        password = self.password_field.text()

        self.connect = Connect_bd(username,  password)







        # Проверка корректности логина и пароля
        if username == 'root' and password == '!123':
            self.connect.connect_database()
            self.ShowMainForm()



        else:
            QMessageBox.critical(None, "Ошибка подключения", "Неверный логин или пароль.")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Aauthorization()
    main_window.show()
    sys.exit(app.exec_())






