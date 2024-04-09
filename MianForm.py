from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton



from  Test1 import  Test1
from  Test2 import  Test2






class MainWindow(QWidget):  # Создаем класс главного окна
    def __init__(self, parent=None):  # Конструктор класса
        super().__init__(parent)  # Вызываем конструктор базового класса
        self.initUI()  # Инициализируем пользовательский интерфейс

    def initUI(self):


        # Задаем заголовок окна
        self.setWindowTitle('Главное меню')

        # Устанавливаем иконку окна
        self.setWindowIcon(QIcon('ФОТО/hacker.jpg'))

        # Устанавливаем шрифт для всплывающих подсказок
        QToolTip.setFont(QFont('SansSerif', 10))

        # Создаем кнопки
        bth = QPushButton('Таблица Test1', self)
        bth1 = QPushButton('Таблица Test2', self)

        # Изменяем размеры кнопок в соответствии с их содержимым
        bth.resize(bth.sizeHint())
        bth1.resize(bth1.sizeHint())

        # Располагаем кнопки в окне
        bth.move(50, 50)  # Кнопка Test1
        bth1.move(50, 20)  # Кнопка Test2


        bth.clicked.connect(self.ShowTest1)
        bth1.clicked.connect(self.ShowTest2)

        # Устанавливаем фиксированный размер окна
        self.setFixedSize(200, 200)  # Увеличиваем высоту окна




        # Создаем кнопку 'Выход'
        quit_button = QPushButton('Выход', self)

        # Привязываем кнопку выхода к завершению приложения
        quit_button.clicked.connect(QCoreApplication.instance().quit)

        # Располагаем кнопку выхода в окне
        quit_button.move(50, 100)

        self.show()  # Отображаем окно


    def ShowTest1(self):
        self.test1 = Test1()
        self.test1.show()

    def ShowTest2(self):
        self.test2 = Test2()
        self.test2.show()



















