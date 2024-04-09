from mysql.connector import Error
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor

from database.Test2.Updates_tables import UpdateTables


class UpdateTest2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Настройка окна
        self.setWindowTitle("Обновление данных")
        self.setWindowIcon(QIcon("ФОТО/hacker.jpg"))
        font = QFont("SansSerif", 14)
        color_lightblue = QColor(173, 216, 230)
        self.setStyleSheet(f"background-color: {color_lightblue.name()}")

        # Создание меток
        # Создаем метки (label) для отображения текста
        self.label_title = QLabel("Обновление:", self)
        self.label_groups_name = QLabel("Имя группы:", self)
        self.label_id_test_1 = QLabel("ID_Студента:", self)

        # Устанавливаем шрифт для всех меток
        for label in (self.label_title, self.label_groups_name, self.label_id_test_1):
            label.setFont(font)

        # Создаем поля ввода текста (LineEdit)
        self.groups_name_edit = QLineEdit(self)
        self.id_test_1_edit = QLineEdit(self)

        # Создание кнопки "Обновить"
        self.update_button = QPushButton("Обновить", self)

        self.update_button.clicked.connect(self.update_data_to_db)
        self.update_button.resize(self.update_button.sizeHint())

        # Размещение элементов
        self.update_button.move(120, 290)

        # Размещаем метки по координатам
        self.label_title.move(100, 10)
        self.label_groups_name.move(100, 40)
        self.label_id_test_1.move(100, 80)

        # Размещаем поля ввода с небольшим отступом от меток
        self.groups_name_edit.move(150, 60)
        self.id_test_1_edit.move(150, 105)

        # Фиксированный размер окна
        self.setFixedSize(300, 350)

    def update_data_to_db(self):
        """
        Функция для обновления данных в базе данных.

        Считывает значения из полей ввода, создает объект класса UpdateTables
        и вызывает его метод update_Test1() для обновления данных. Обрабатывает возможные ошибки.
        """
        # **Получаем текст из полей ввода**
        groups_name = self.groups_name_edit.text()
        id_test_1 = self.id_test_1_edit.text()

        # Обновление данных в базе данных
        update_tables = UpdateTables(groups_name, id_test_1)
        try:
            update_tables.update_Test2()
            # Отображение сообщения об успехе
            message_box = QMessageBox()
            message_box.setText(f"Данные для {groups_name} успешно обновлены.")
            message_box.exec_()
        except Error as err:
            # **Отображение сообщения об ошибке**
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Установка иконки ошибки
            message_box.setText("Ошибка базы данных:")
            message_box.setDetailedText(str(err))
            message_box.exec_()