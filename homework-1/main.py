"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2,csv

with open('north_data\\customers_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='Mike1984') as conn:
        with conn.cursor() as curr:
            count = 0
            for row in file_reader:
                if count != 0:
                    curr.execute("INSERT INTO customer_data VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
                count+=1
    conn.close()

with open('north_data\\employees_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='Mike1984') as conn:
        with conn.cursor() as curr:
            count = 0
            for row in file_reader:
                if count != 0:
                    curr.execute("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
                count+=1
    conn.close()

with open('north_data\\orders_data.csv', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=',')
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='Mike1984') as conn:
        with conn.cursor() as curr:
            count = 0
            for row in file_reader:
                if count != 0:
                    curr.execute("INSERT INTO order_data VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))
                count+=1
    conn.close()