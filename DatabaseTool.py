import sqlite3
from sqlite3 import Error


class DatabaseTool():

    def insert_data(conn, table_name, *args):
        """
        insert data to the table
        :param conn: Connection object
        :param table_name: name of the table
        :return:
        """

        sql = ''' INSERT INTO {}(email,username,isimsoyisim,emailuserlk,usernamelk,dogumyil,dogumay,dogumgun,ulke,ap)
                VALUES(?,?,?,?,?,?,?,?,?,?) '''.format(table_name)
        cur = conn.cursor()
        cur.execute(sql, args)
        conn.commit()

        return cur.lastrowid

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn


    def create_table(conn,table_name):
        """ create a table from the sql_create_data_table statement
        :param conn: Connection object
        :return:
        """
        sql_create_data_table = """CREATE TABLE IF NOT EXISTS {} (
                                        id integer PRIMARY KEY,
                                        email text NOT NULL,
                                        username text NOT NULL,
                                        isimsoyisim text NOT NULL,
                                        emailuserlk integer NOT NULL,
                                        usernamelk integer NOT NULL,
                                        dogumyil integer NOT NULL,
                                        dogumay integer NOT NULL,
                                        dogumgun text NOT NULL,
                                        ulke text NOT NULL,
                                        ap integer NOT NULL
                                    );""".format(table_name)

        try:
            c = conn.cursor()
            c.execute(sql_create_data_table)
        except Error as e:
            print(e)








