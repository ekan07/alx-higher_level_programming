#!/usr/bin/python3
"""display all values that matches the given argument"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s
                ORDER BY states.id ASC""", (sys.argv[4],))
    rows_data = cur.fetchall()
    for row in rows_data:
        print(row)
    cur.close()
    db.close()
