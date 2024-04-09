from mysql.connector import connect, Error  # Импортируем необходимые модули для работы с БД и окнами сообщений


class DeleteTables:

    def __init__(self, groups_name):
        self.username = 'root'  # Имя пользователя базы данных
        self.password = '!123'  # Пароль пользователя базы данных
        self.database = 'myсourse' # Исправлено имя переменной
        self.groups_name = groups_name


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

        except Error as err:  # Более конкретное исключение
            print(
                None, "Ошибка подключения к базе данных", f"{str(err)}"
            )
            return False

    def delete_Test2(self):
        if self.connect_database():
            try:
                cursor = self.connection.cursor()
                delete_stmt = f"DELETE FROM test2 WHERE groups_name = '{self.groups_name}'"  # Убрана лишняя закрывающая скобка
                cursor.execute(delete_stmt)
                self.connection.commit()  # Фиксация транзакции
                print(self, "Удалены", f"{self.groups_name} Данные успешно удалены из систему.")
            except Error as err:
                print(
                    None, "Ошибка выполнения запроса", f"{str(err)}"
                )
                return False
            finally:
                cursor.close()
                self.connection.close()

            return True



