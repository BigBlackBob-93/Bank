from config import CENTRAL, UNIVERSE


def create_table() -> str:
    query = """
                    CREATE TABLE bank(
                    id serial PRIMARY KEY,
                    class varchar(10) NOT NULL,
                    name varchar(50) NOT NULL,
                    date varchar(50) NOT NULL,
                    location varchar(50),
                    rate real,
                    type varchar(10),
                    license int,
                    equity int,
                    specialization varchar(100));
            """
    return query


def insert_query(index: int = UNIVERSE) -> str:
    if index == CENTRAL:
        return "INSERT INTO bank (class, name, date, location, rate) VALUES (%s, %s, %s, %s, %s)"
    return "INSERT INTO bank (class, name, date, location, type, license, equity) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
