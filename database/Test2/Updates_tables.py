
from mysql.connector import connect, Error  # Импортируем необходимые модули для работы с БД и окнами сообщений
from PyQt5.QtWidgets import QMessageBox


class UpdateTables:

    def __init__(self, groups_name, id_test_1):
        self.username = 'root'
        self.password = '!123'
        self.database = 'myсourse'  # Исправлено имя переменной
        self.groups_name = groups_name
        self.id_test_1 = id_test_1

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

    def update_Test2(self):
        """
        Обновляет запись в таблице test2 по указанному id.

        Args:
            id (int): Идентификатор записи для обновления.
            groups_name (str, optional): Имя (обновляется, если указано). Defaults to None.
            id_test_1 (int, optional): Возраст (обновляется, если указано). Defaults to None.

        Returns:
            bool: True - если обновление успешно, False - иначе.
        """

        if self.connect_database():
            try:
                cursor = self.connection.cursor()
                # Динамическое построение запроса UPDATE based на аргументах
                update_stmt = "UPDATE test2 SET "
                setters = []
                if self.groups_name:
                    setters.append(f"groups_name = '{self.groups_name}'")
                if self.id_test_1:
                    setters.append(f"id_test_1 = {self.id_test_1}")
                if setters:
                    update_stmt += ", ".join(setters)
                    update_stmt += f" WHERE groups_name = '{self.groups_name}'"  # Условие для обновления конкретной записи
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