from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QLabel, QTabWidget, QGridLayout, QTableWidget, QTableWidgetItem, QPushButton)
from PyQt5.QtCore import QTimer

from addTest1 import  AddTest1
from deleteTest1 import  DeleteTest1
from updateTest1 import  UpdateTest1

from database.Show_database import ShowDatabase

class Test1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Задаем заголовок окна
        self.setWindowTitle('Tast1')

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(800, 800)

        # Создаем QGridLayout
        layout = QGridLayout()

        # Создаем метку для названия таблицы
        self.label = QLabel("Таблица Test1")
        self.label.setFont(QFont("SansSerif", 14))

        # Создаем QTabWidget
        self.tab_widget = QTabWidget()

        # Добавляем элементы в layout
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.tab_widget, 1, 0)

        # Устанавливаем layout для окна
        self.setLayout(layout)

        # Создаем таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_table)
        self.timer.start(1000)  # Обновлять таблицу каждую 1 секунду


        self.update_table()  # Вызываем метод один раз при запуске

        self.bth = QPushButton('Добавление', self)
        self.bth1 = QPushButton('Удаление', self)
        self.bth2 = QPushButton('Обновление', self)

        # Изменяем размеры кнопок в соответствии с их содержимым
        self.bth.resize(self.bth.sizeHint())
        self.bth1.resize(self.bth1.sizeHint())
        self.bth2.resize(self.bth.sizeHint())

        # Располагаем кнопки в окне

        self.bth1.move(700, 20)
        self.bth.move(600, 20)
        self.bth2.move(500, 20)

        self.bth.clicked.connect(self.ShowAddTest1)
        self.bth1.clicked.connect(self.ShowDeleteTest1)
        self.bth2.clicked.connect(self.ShowUpdateTest1)

        self.show()





    def update_table(self):
        # Создаем экземпляр класса ShowDatabase
        database = 'myсourse'
        show_database = ShowDatabase(database)

        # Вызываем метод table_Test1()
        data = show_database.table_Test1()

        # Создаем экземпляр QTableWidget
        self.table = QTableWidget()

        # Устанавливаем количество строк и столбцов
        self.table.setRowCount(len(data))  # Устанавливаем количество строк равное количеству данных
        self.table.setColumnCount(4)  # Устанавливаем 5 столбцов

        # Заполняем заголовки столбцов
        self.table.setHorizontalHeaderLabels(["name", "age", "gender", "curse_type"])

        # Заполняем таблицу данными, начиная со 2-го элемента (пропускаем первые 2)
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data[1:]):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))

        # Ограничиваем ширину таблицы
        self.table.setMaximumWidth(self.width() - 200)

        # Автоматически подбираем ширину столбцов
        self.table.resizeColumnsToContents()

        # Создаем новую вкладку и добавляем в нее таблицу
        new_tab = QWidget()
        new_tab_layout = QGridLayout()
        new_tab_layout.addWidget(self.table)
        new_tab.setLayout(new_tab_layout)
        self.tab_widget.addTab(new_tab, "Таблица Test1")

        # Останавливаем таймер
        self.timer.stop()

    def ShowAddTest1(self):
        self.test1 = AddTest1()
        self.test1.show()

    def ShowDeleteTest1(self):
        self.test1 = DeleteTest1()
        self.test1.show()

    def ShowUpdateTest1(self):
        self.test1 = UpdateTest1()
        self.test1.show()