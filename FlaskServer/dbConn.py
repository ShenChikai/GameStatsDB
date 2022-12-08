import mariadb
import sys

# https://mariadb-corporation.github.io/mariadb-connector-python/cursor.html#cursor-methods

def connectToDB(dbconfig):
    # Connect
    try:
        conn = mariadb.connect(
            host=dbconfig['dbhost'],
            user=dbconfig['dbuser'],
            password=dbconfig['dbpass'],
            database=dbconfig['dbname'],
            port=3306
        )
    except mariadb.Error as e:
        print(f'Database Connection Error: {e}')
        sys.exit(1)

    print('***********************************************************************')
    print(f"| Connection Established with Database as User \"{dbconfig['dbuser']}\" ")
    print('***********************************************************************')
    # Get Cursor
    cursor = conn.cursor()

    return cursor