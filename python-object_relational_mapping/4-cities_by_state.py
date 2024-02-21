#!/usr/bin/python3
"""
List all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def list_cities(username, password, database_name):
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)

        cursor = db.cursor()
        query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """
        cursor.execute(query)
        cities = cursor.fetchall()

        for city in cities:
            print(city)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) !=   4:
        print("Usage: ./4-cities_by_state.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    list_cities(username, password, database_name)
