from mysql.connector import Error
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor

from database.Test1.Updates_tables import UpdateTables


class UpdateTest1(QWidget):
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
        self.label_title = QLabel("Обновление:", self)
        self.label_name = QLabel("Имя:", self)
        self.label_age = QLabel("Возраст:", self)
        self.label_gender = QLabel("Пол:", self)
        self.label_course = QLabel("Курс:", self)
        self.label_course_type = QLabel("Тип курса:", self)
        for label in (self.label_title, self.label_name, self.label_age,
                      self.label_gender, self.label_course, self.label_course_type):
            label.setFont(font)

        # Создание полей ввода
        self.name_edit = QLineEdit(self)
        self.age_edit = QLineEdit(self)
        self.gender_edit = QLineEdit(self)
        self.course_edit = QLineEdit(self)
        self.course_type_edit = QLineEdit(self)

        # Создание кнопки "Обновить"
        self.update_button = QPushButton("Обновить", self)
        self.update_button.clicked.connect(self.update_data_to_db)
        self.update_button.resize(self.update_button.sizeHint())

        # Размещение элементов
        self.update_button.move(120, 290)
        self.label_title.move(100, 10)
        self.label_name.move(100, 40)
        self.label_age.move(100, 80)
        self.label_gender.move(100, 125)
        self.label_course.move(100, 170)
        self.label_course_type.move(100, 220)
        self.name_edit.move(150, 60)
        self.age_edit.move(150, 105)
        self.gender_edit.move(150, 150)
        self.course_edit.move(150, 195)
        self.course_type_edit.move(150, 250)

        # Фиксированный размер окна
        self.setFixedSize(300, 350)

    def update_data_to_db(self):
        """
        Функция для обновления данных в базе данных.

        Считывает значения из полей ввода, создает объект класса UpdateTables
        и вызывает его метод update_Test1() для обновления данных. Обрабатывает возможные ошибки.
        """
        # Получение данных из полей ввода
        name = self.name_edit.text()
        age = self.age_edit.text()
        gender = self.gender_edit.text()
        course = self.course_edit.text()
        course_type = self.course_type_edit.text()

        # Обновление данных в базе данных
        update_tables = UpdateTables(name, age, gender, course, course_type)
        try:
            update_tables.update_Test1()
            # Отображение сообщения об успехе
            message_box = QMessageBox()
            message_box.setText(f"Данные для {name} успешно обновлены.")
            message_box.exec_()
        except Error as err:
            # **Отображение сообщения об ошибке**
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Установка иконки ошибки
            message_box.setText("Ошибка базы данных:")
            message_box.setDetailedText(str(err))
            message_box.exec_()