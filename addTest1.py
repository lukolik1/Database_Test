
# Импорт класса ошибок из mysql.connector
from mysql.connector import Error

# Импорт необходимых виджетов из PyQt5
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)

# Импорт шрифтов и цветов из PyQt5
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor

# Импорт класса AddTables из модуля database.Add_tables
from database.Test1.Add_tables import AddTables


class AddTest1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # Устанавливаем заголовок окна
        self.setWindowTitle('Добавление данных')

        # Устанавливаем иконку окна (необходимо скорректировать путь)
        self.setWindowIcon(QIcon('ФОТО/hacker.jpg'))

        # Создаем объект шрифта
        font = QFont("SansSerif", 14)

        # Устанавливаем светло-голубой цвет фона окна
        color_lightblue = QColor(173, 216, 230)
        self.setStyleSheet(f"background-color: {color_lightblue.name()}")

        # Создаем метки (label) для отображения текста
        self.label_title = QLabel("Добавление:", self)
        self.label_name = QLabel("Имя:", self)
        self.label_age = QLabel("Возраст:", self)
        self.label_gender = QLabel("Пол:", self)
        self.label_course = QLabel("Курс:", self)
        self.label_course_type = QLabel("Тип курса:", self)

        # Устанавливаем шрифт для всех меток
        for label in (self.label_title, self.label_name, self.label_age,
                      self.label_gender, self.label_course, self.label_course_type):
            label.setFont(font)

        # Создаем поля ввода текста (LineEdit)
        self.name_edit = QLineEdit(self)
        self.age_edit = QLineEdit(self)
        self.gender_edit = QLineEdit(self)
        self.course_edit = QLineEdit(self)
        self.course_type_edit = QLineEdit(self)

        # Создаем кнопку "Добавить"
        self.add_button = QPushButton("Добавить", self)

        # Связываем нажатие кнопки с методом add_data_to_db
        self.add_button.clicked.connect(self.add_data_to_db)

        # Устанавливаем размер кнопки по содержимому
        self.add_button.resize(self.add_button.sizeHint())

        # Размещаем кнопку
        self.add_button.move(120, 290)

        # Размещаем метки по координатам
        self.label_title.move(100, 10)
        self.label_name.move(100, 40)
        self.label_age.move(100, 80)
        self.label_gender.move(100, 125)
        self.label_course.move(100, 170)
        self.label_course_type.move(100, 220)

        # Размещаем поля ввода с небольшим отступом от меток
        self.name_edit.move(150, 60)
        self.age_edit.move(150, 105)
        self.gender_edit.move(150, 150)
        self.course_edit.move(150, 195)
        self.course_type_edit.move(150, 250)

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(300, 350)  # Задаем ширину и высоту окна

    def add_data_to_db(self):
        """
        Функция для добавления данных в базу данных.

        Считывает значения из полей ввода, создает объект класса AddTables
        и вызывает его метод add_Test1() для добавления данных. Обрабатывает возможные ошибки.
        """

        # **Получаем текст из полей ввода**
        name = self.name_edit.text()
        age = self.age_edit.text()
        gender = self.gender_edit.text()
        course = self.course_edit.text()
        course_type = self.course_type_edit.text()

        # **Добавление данных в базу данных**
        add_tables = AddTables(name, age, gender, course, course_type)
        try:
            add_tables.add_Test1()
            # **Отображение сообщения об успехе**
            message_box = QMessageBox()
            message_box.setText(f"{name} Данные успешно внесены в систему.")
            message_box.exec_()
        except Error as err:
            # **Отображение сообщения об ошибке**
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Установка иконки ошибки
            message_box.setText("Ошибка базы данных:")
            message_box.setDetailedText(str(err))
            message_box.exec_()
