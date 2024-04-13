#!/usr/bin/python3
"""Lists all cities of a specified state from the database hbtn_0e_4_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to MySQL and access the database"""
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    """Retrieve all cities of the specified state"""
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    """Extract city names from the query result"""
    cities = [row[0] for row in rows]
    """Print the list of city names"""
    print(*cities, sep=", ")
    cur.close()
    db.close()
