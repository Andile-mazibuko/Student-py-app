from idlelib.query import Query
from statistics import stdev

import psycopg2

from Student import Student

conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="root",port=5432)
cursor = conn.cursor()

def create_connection():

    return conn

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INT PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            cellphone VARCHAR(10)
        );
    """)
    conn.commit()
def __get_all():
    cursor.execute("""
        SELECT * FROM student;
    """)
    return cursor.fetchall()
def __create__stud(stud: Student):
    cursor.execute(stud.create_student())
    conn.commit()

def __get__stud(id:int):
    cursor.execute(f"SELECT * FROM student  WHERE id = {id};")
    conn.commit()
    return cursor.fetchone()


def __update__student(stud: Student):
            query = """
                UPDATE student
                SET first_name = %s, last_name = %s,cellphone = %s 
                WHERE id = %s
            """
            cursor.execute(query,(stud.first_name, stud.last_name ,stud.cellphone,stud.id))
            conn.commit()
def __delete_stud(stud:Student):
    cursor.execute("DELETE FROM student WHERE id = %s",(stud.id,))
    conn.commit()