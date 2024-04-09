from mysql.connector import connect, Error
from PyQt5.QtWidgets import QMessageBox



class ShowDatabase:

    def __init__(self, database):
        self.username = 'root'
        self.password = '!123'
        self.database = database # Исправлено имя переменной

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
            QMessageBox.critical(
                None, "Ошибка подключения к базе данных", f"{str(err)}"
            )
            return False

    def table_Test1(self):
        if self.connect_database():
            try:
                cursor = self.connection.cursor()
                test1 = f'SELECT *  FROM test1'
                cursor.execute(test1)
                data = cursor.fetchall()
            except Error as err:
                QMessageBox.critical(
                    None, "Ошибка выполнения запроса", f"{str(err)}"
                )
                return None
            finally:
                cursor.close()


            return data

        else:
            print("Ошибка подключения к базе данных")

    def table_Test2(self):
            if self.connect_database():
                try:
                    cursor = self.connection.cursor()
                    test2 = f'SELECT *  FROM test2'
                    cursor.execute(test2)
                    data = cursor.fetchall()
                except Error as err:
                    QMessageBox.critical(
                        None, "Ошибка выполнения запроса", f"{str(err)}"
                    )
                    return None
                finally:
                    cursor.close()

                return data

            else:
                print("Ошибка подключения к базе данных")















