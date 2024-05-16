import mysql.connector

class DatabaseConnection:
    def __init__(self, database_name='api_gateway', host='localhost', user='root', password=''):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
        self.connection = None
    
    def cursor(self):
        if self.connection is None:
            self.connect()
        return self.connection.cursor()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            print("Connected to MySQL database")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
