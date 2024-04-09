from mysql.connector import Error

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor

from database.Test1.Delete_tables import DeleteTables


class DeleteTest1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Удаление данных')
        self.setWindowIcon(QIcon('ФОТО/hacker.jpg'))
        font = QFont("SansSerif", 14)

        # Создаем свои переменные цвета
        color_lightblue = QColor(173, 216, 230)  # Цвет lightblue

        self.setStyleSheet("background-color: " + color_lightblue.name() + ";")  # Устанавливаем цвет фона окна


        lable = QLabel("Удаление:", self)
        lable_name = QLabel("Имя:", self)


        lable.setFont(font)
        lable_name.setFont(font)



        # Создаем поле для ввода пароля, логина и базы данных
        self.textbox_name = QLineEdit(self)





        self.btn1 = QPushButton("Удалить", self)
        self.btn1.resize(self.btn1.sizeHint())
        self.btn1.clicked.connect(self.deleteTest1_bd)




        self.btn1.move(120, 290)  # Увеличиваем координату Y для кнопки "Войти"

        lable.move(100, 10)

        lable_name.move(100, 40)


        self.textbox_name.move(100, 60)


        # Устанавливаем фиксированный размер окна
        self.setFixedSize(300, 350)  # Увеличиваем высоту окна

    def deleteTest1_bd(self):
        name = self.textbox_name.text()

        try:
            delete_tables = DeleteTables(name)
            delete_tables.delete_Test1()

            # Отображение сообщения об успехе
            message_box = QMessageBox()
            message_box.setText(f"Данные для {name} успешно удалены.")
            message_box.exec_()
        except Error as err:
            # Отображение сообщения об ошибке
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Установка иконки ошибки
            message_box.setText("Ошибка базы данных:")
            message_box.setDetailedText(str(err))
            message_box.exec_()




