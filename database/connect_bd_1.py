from mysql.connector import connect
from PyQt5.QtWidgets import QMessageBox


class Connect_bd:
   

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect_database(self):
        try:
            self.connection = connect(
                user=self.username,
                password=self.password,
                host="localhost"
            )
            return True
        except Exception as err:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при подключении к базе данных: {str(err)}")
            return False



