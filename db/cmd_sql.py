import sqlite3
from datetime import datetime
import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlError
from PyQt5.QtWidgets import QMessageBox

db_name = 'contacts.sqlite'


def connection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName("storage/" + db_name)

    if not con.open():
        QMessageBox.critical(
            None,
            "App Name - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        sys.exit(1)

    if con.isOpen():
        print('Connected.')
        return con


def insert_result(data):
    p1 = data['player_1']
    p2 = data['player_2']
    wi = data['winner']
    fs = data['final_score']
    dn = datetime.now()

    sql = f"""INSERT INTO games ( player_1, player_2, winner, final_score, date ) 
    VALUES ('{p1}', '{p2}', '{wi}', '{fs}', '{dn}') """

    try:
        q = QSqlQuery()
        q.exec_(sql)
        # print(sql)

        # query_all = """SELECT winner FROM games;"""
        # qa = QSqlQuery()
        # qa.exec_(query_all)
        #
        # if qa.first():
        #     print(qa.value(0))
        # else:
        #     print('Erro ao buscar o vencedor')
        # print(query_all)
    except QSqlError:
        print(QSqlError)
        return


sql1 = f"""CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        player_1 VARCHAR(46) NOT NULL,
        player_2 VARCHAR(46) NOT NULL,
        winner VARCHAR(46),
        final_score VARCHAR(10),
        date VARCHAR(46)
        )"""

