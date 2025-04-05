from statistics import stdev

import psycopg2

from Student import Student

conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="root",port=5432)
curor = conn.cursor()
def create_connection():

    return conn

def create_table():
    curor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INT PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            cellphone VARCHAR(10)
        );
    """)
    conn.commit()

def __create__stud(stud: Student):
    curor.execute(stud.create_student())
    conn.commit()

def __get__Stud(id:int):
    curor.execute(f"SELECT FROM student * WHERE id = {id}")
    conn.commit()
    return curor.fetchone()

