import classes
import queries
import psycopg2
from config import host, user, password, db_name, CENTRAL, UNIVERSE

if __name__ == "__main__":
    try:
        # BD connection
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        # Banks creation
        central = classes.Central(name='The Central Bank of Russian Federation', rate=15.3)
        sber = classes.Universal(name='Sberbank', license=1481, equity=5810000)
        vtb = classes.Universal(name='VTB', license=1000, equity=1700000)
        pochta = classes.Universal(name='Pochta Bank', license=650, equity=21600)

        # Queries to DB
        with connection.cursor() as cursor:
            cursor.execute(queries.insert_query(CENTRAL), central.getter())
            cursor.execute(queries.insert_query(UNIVERSE), sber.getter())
            cursor.execute(queries.insert_query(UNIVERSE), vtb.getter())
            cursor.execute(queries.insert_query(UNIVERSE), pochta.getter())

    except Exception as _ex:
        print("[INFO] Error PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
