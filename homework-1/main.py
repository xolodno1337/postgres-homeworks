"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def open_csv(filename):
    """ Функция для получения данных из файла CSV. """
    with open(filename, 'r', encoding='utf=8') as file:
        reader = csv.reader(file)
        data = [tuple(row) for row in reader]
        return data[1:]


with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='7856'
) as conn:
    with conn.cursor()as cur:
        cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', (open_csv('./north_data/customers_data.csv')))
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (open_csv('./north_data'
                                                                                           '/employees_data.csv')))
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (open_csv('./north_data/orders_data.csv')))

conn.close()
# open_csv('./north_data/customers_data.csv')
# open_csv('./north_data/employees_data.csv')
# open_csv('./north_data/orders_data.csv')
