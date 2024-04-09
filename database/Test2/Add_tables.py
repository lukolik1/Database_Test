from mysql.connector import connect, Error




class AddTables:

    def __init__(self, groups_name, id_test_1):
        self.username = 'root'
        self.password = '!123'
        self.database = 'myсourse' # Исправлено имя переменной
        self.groups_name = groups_name
        self.id_test_1 = id_test_1

    def connect_database(self):
        """
        Функция для подключения к базе данных.

        Пытается подключиться к базе данных с указанными параметрами.
        В случае успеха возвращает True, иначе возвращает False и выводит сообщение об ошибке.
        """

        try:
            # Подключение к базе данных
            self.connection = connect(
                user=self.username,
                password=self.password,
                database=self.database,
                host="localhost"
            )
            # Создаем курсор для работы с БД
            self.connection.cursor()
            return True

        except Error as err:  # Более конкретное исключение
            # Вывод сообщения об ошибке
            print(
                None, "Ошибка подключения к базе данных:", f"{str(err)}"
            )
            return False

    def add_Test2(self):
        """
        Функция для добавления данных в таблицу test1 базы данных.

        Сначала пытается подключиться к базе данных с помощью метода connect_database().
        Если подключение успешно, выполняет запрос INSERT для добавления данных
        из полей ввода в таблицу test1.
        В случае успеха возвращает None,
        в случае ошибки возвращает None и выводит сообщение об ошибке.
        """

        if self.connect_database():
            try:
                cursor = self.connection.cursor()

                # Формирование запроса INSERT
                test2 = f"INSERT INTO test2 (groups_name, id_test_1) VALUES ('{self.groups_name}', '{self.id_test_1}')"

                # Выполнение запроса
                cursor.execute(test2)

                # Подтверждение изменений (commit)
                self.connection.commit()

            except Error as err:
                # Вывод сообщения об ошибке выполнения запроса
                print(
                    None, "Ошибка выполнения запроса:", f"{str(err)}"
                )
                return None

            finally:
                # Закрытие курсора и соединения с базой данных
                # (необходимо выполнять вне зависимости от успешности или ошибки)
                cursor.close()
                self.connection.close()

            return None


























