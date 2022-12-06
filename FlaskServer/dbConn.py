import mariadb
import sys

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
        print('Database Connected.')
    except mariadb.Error as e:
        print(f'Database Connection Error: {e}')
        sys.exit(1)
    # Get Cursor
    cursor = conn.cursor()

    return cursor