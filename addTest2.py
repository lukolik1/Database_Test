
# Импорт класса ошибок из mysql.connector
from mysql.connector import Error

# Импорт необходимых виджетов из PyQt5
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QMessageBox)

# Импорт шрифтов и цветов из PyQt5
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QColor

# Импорт класса AddTables из модуля database.Add_tables
from database.Test2.Add_tables import AddTables


class AddTest2(QWidget):
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
        self.label_groups_name = QLabel("Имя группы:", self)
        self.label_id_test_1 = QLabel("ID_Студента:", self)


        # Устанавливаем шрифт для всех меток
        for label in (self.label_title, self.label_groups_name, self.label_id_test_1):
            label.setFont(font)

        # Создаем поля ввода текста (LineEdit)
        self.groups_name_edit = QLineEdit(self)
        self.id_test_1_edit = QLineEdit(self)

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
        self.label_groups_name.move(100, 40)
        self.label_id_test_1.move(100, 80)


        # Размещаем поля ввода с небольшим отступом от меток
        self.groups_name_edit.move(150, 60)
        self.id_test_1_edit.move(150, 105)


        # Устанавливаем фиксированный размер окна
        self.setFixedSize(300, 350)  # Задаем ширину и высоту окна

    def add_data_to_db(self):
        """
        Функция для добавления данных в базу данных.

        Считывает значения из полей ввода, создает объект класса AddTables
        и вызывает его метод add_Test1() для добавления данных. Обрабатывает возможные ошибки.
        """

        # **Получаем текст из полей ввода**
        groups_name = self.groups_name_edit.text()
        id_test_1 = self.id_test_1_edit.text()


        # **Добавление данных в базу данных**
        add_tables = AddTables(groups_name, id_test_1)
        try:
            add_tables.add_Test2()
            # **Отображение сообщения об успехе**
            message_box = QMessageBox()
            message_box.setText(f"{groups_name} Данные успешно внесены в систему.")
            message_box.exec_()
        except Error as err:
            # **Отображение сообщения об ошибке**
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Critical)  # Установка иконки ошибки
            message_box.setText("Ошибка базы данных:")
            message_box.setDetailedText(str(err))
            message_box.exec_()
