from abc import ABC, abstractmethod
import sqlite3
#pip install psycopg2
import psycopg2
class Data_client(ABC):

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
'n'

class Sqlite(Data_client):

    __CONNECTION = sqlite3.connect('db_sqlite.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS client(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT);'''


    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute(''' SELECT * FROM client;''')
            for data in self.cursor.fetchall():
                print(*data)


    def insert(self, login, password):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO client(login, password) VALUES(?, ?)''', (login, password))

    def update(self, id, login, password):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE client SET login = ?, password = ?  WHERE id = ?''', (login, password, id))


    def delete(self, id):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM client WHERE id = ?''', (id,))


class Postgres(Data_client):


    __CONNECTION = psycopg2.connect(host="localhost", database="db_postgres", user="postgres",password="5432",port="5432")
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS client(
    id serial PRIMARY KEY,
    login TEXT,
    password TEXT);'''


    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute(''' SELECT * FROM client;''')
            for data in self.cursor.fetchall():
                print(*data)


    def insert(self, login, password):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO client(login, password) VALUES(%s, %s)''', (login, password))

    def update(self, id, login, password):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE client SET login = %s, password = %s  WHERE id = %s''', (login, password, id))


    def delete(self, id):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM client WHERE id = %s''', (id,))