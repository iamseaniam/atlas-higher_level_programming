#!/usr/bin/python3
"""
List all cities of a specified state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def filter_cities(username, password, database_name, state_name):
    
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database_name)
        
        cursor = db.cursor()
        cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
        cities = cursor.fetchall()
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))n
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

