#!/usr/bin/python3
"""Lists all states matching a given name from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    """ Establishing a connection to MySQL and accessing the database """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    """ Executing a query to select states matching the given name """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
