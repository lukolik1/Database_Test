from mysql.connector import connect, Error  # Импортируем необходимые модули для работы с БД и окнами сообщений
from PyQt5.QtWidgets import QMessageBox

class UpdateTables:

<<<<<<< HEAD
=======
    def __init__(self, name, age, gender, course, course_type):
        self.username = 'root'
        self.password = '!123'
        self.database = 'myсourse'  # Исправлено имя переменной
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.course_type = course_type

    def connect_database(self):
        try:
            self.connection = connect(
                user=self.username,
                password=self.password,
                database=self.database,
                host="localhost"
            )
            self.connection.cursor()  # Создаем курсор для работы с БД
            return True

        except Error as err:
            QMessageBox.critical(
                None, "Ошибка подключения к базе данных", f"{str(err)}"
            )
            return False

    from mysql.connector import connect, Error  # Импортируем необходимые модули для работы с БД и окнами сообщений
    from PyQt5.QtWidgets import QMessageBox

    class UpdateTables:

>>>>>>> origin/master
        def __init__(self, name, age, gender, course, course_type):
            self.username = 'root'
            self.password = '!123'
            self.database = 'myсourse'  # Исправлено имя переменной
            self.name = name
            self.age = age
            self.gender = gender
            self.course = course
            self.course_type = course_type

        def connect_database(self):
            try:
                self.connection = connect(
                    user=self.username,
                    password=self.password,
                    database=self.database,
                    host="localhost"
                )
                self.connection.cursor()  # Создаем курсор для работы с БД
                return True

            except Error as err:
                QMessageBox.critical(
                    None, "Ошибка подключения к базе данных", f"{str(err)}"
                )
                return False



        def update_Test1(self):
            """
            Обновляет запись в таблице test1 по указанному id.

            Args:
                id (int): Идентификатор записи для обновления.
                name (str, optional): Имя (обновляется, если указано). Defaults to None.
                age (int, optional): Возраст (обновляется, если указано). Defaults to None.
                gender (str, optional): Пол (обновляется, если указано). Defaults to None.
                course (str, optional): Курс (обновляется, если указано). Defaults to None.
                course_type (str, optional): Тип курса (обновляется, если указано). Defaults to None.

            Returns:
                bool: True - если обновление успешно, False - иначе.
            """

            if self.connect_database():
                try:
                    cursor = self.connection.cursor()
                    # Динамическое построение запроса UPDATE based на аргументах
                    update_stmt = "UPDATE test1 SET "
                    setters = []
                    if self.name:
                        setters.append(f"name = '{self.name}'")
                    if self.age:
                        setters.append(f"age = {self.age}")
                    if self.gender:
                        setters.append(f"gender = '{self.gender}'")
                    if self.course:
                        setters.append(f"course = '{self.course}'")
                    if self.course_type:
                        setters.append(f"course_type = '{self.course_type}'")
                    if setters:
                        update_stmt += ", ".join(setters)
                        update_stmt += f" WHERE name = '{self.name}'"  # Условие для обновления конкретной записи
                        cursor.execute(update_stmt)
                    else:
                        # Обработка случая, когда не указаны параметры обновления
                        QMessageBox.warning(None, "Предупреждение", "Не указаны параметры для обновления")
                except Error as err:
                    QMessageBox.critical(
                        None, "Ошибка выполнения запроса", f"{str(err)}"
                    )
                    return False
                finally:
                    cursor.close()
                    self.connection.commit()  # Сохранение изменений в базе данных
                    self.connection.close()
                return True  # Успешное обновление

            else:
                return False  # Ошибка подключения