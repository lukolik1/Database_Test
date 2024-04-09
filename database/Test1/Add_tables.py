from mysql.connector import connect, Error




class AddTables:

    def __init__(self, name, age, gender, course, course_type):
        self.username = 'root'
        self.password = '!123'
        self.database = 'myсourse' # Исправлено имя переменной
        self.name = name
        self.age = age
        self.gender = gender
        self.course = course
        self.course_type = course_type

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

    def add_Test1(self):
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
                test1 = f"INSERT INTO test1 (name, age, gender, course, course_type) VALUES ('{self.name}', {self.age}, '{self.gender}', '{self.course}', '{self.course_type}')"

                # Выполнение запроса
                cursor.execute(test1)

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


























