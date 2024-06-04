import psycopg2
import psycopg2.extras
import pymysql
import pymysql.cursors
import sqlite3
import typing as t

from .functions import is_nested_iterable


class connect:
    """
    A class for establishing and managing database connections.

    Attributes:
        connection: The database connection object.
        cursor: The database cursor object.
        engine: The database engine being used ("sqlite3", "mysql", or "postgresql").
    """

    def __init__(self, connection, cursor, engine):
        self.connection = connection
        self.cursor = cursor
        self.engine = engine

    @classmethod
    def sqlite3(cls, database: str) -> "connect":
        """
        Create a connection to a SQLite database.

        Args:
            database (str): The name of the SQLite database file.

        Returns:
            connect: A connect instance with a SQLite connection.
        """
        connection = sqlite3.connect(database)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        return cls(connection, cursor, "sqlite3")

    @classmethod
    def mysql(
        cls,
        database: str,
        host: str,
        user: str,
        password: str,
        port: int
    ) -> "connect":
        """
        Create a connection to a MySQL database.

        Args:
            database (str): The name of the MySQL database.
            host (str): The hostname of the MySQL server.
            user (str): The username for the MySQL connection.
            password (str): The password for the MySQL connection.
            port (int): The port number for the MySQL connection.

        Returns:
            connect: A connect instance with a MySQL connection.
        """
        connection = pymysql.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port,
            cursorclass=pymysql.cursors.DictCursor,
        )
        cursor = connection.cursor()
        return cls(connection, cursor, "mysql")

    @classmethod
    def postgresql(
        cls,
        database: str,
        host: str,
        user: str,
        password: str,
        port: int
    ) -> "connect":
        """
        Create a connection to a PostgreSQL database.

        Args:
            database (str): The name of the PostgreSQL database.
            host (str): The hostname of the PostgreSQL server.
            user (str): The username for the PostgreSQL connection.
            password (str): The password for the PostgreSQL connection.
            port (int): The port number for the PostgreSQL connection.

        Returns:
            connect: A connect instance with a PostgreSQL connection.
        """
        connection = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port,
            cursor_factory=psycopg2.extras.RealDictCursor,
        )
        cursor = connection.cursor()
        return cls(connection, cursor, "postgresql")

    @property
    def query(self) -> str:
        """
        Get the current query string.

        Returns:
            str: The current query string.
        """
        return self._query

    @query.setter
    def query(self, query: str):
        """
        Set the query string, with placeholders replaced for MySQL and PostgreSQL.

        Args:
            query (str): The query string to be set.
        """
        if self.engine in ("mysql", "postgresql"):
            query = query.replace("?", "%s")
        self._query = query

    @property
    def value(self) -> t.Any:
        """
        Get the current value or values to be used in the query.

        Returns:
            Any: The current value or values.
        """
        return self._value

    @value.setter
    def value(self, value: t.Any):
        """
        Set the value or values to be used in the query.

        Args:
            value (Any): The value or values to be set.
        """
        self._value = value or ()
        if value and not is_nested_iterable(value):
            self._value = (value,)

    def fetch(self, size: t.Optional[int] = 1) -> t.Union[t.List[t.Dict], t.Dict, None]:
        """
        Fetch data from the database based on the current query and values.

        Args:
            size (Optional[int]): The number of rows to fetch. 0 for all rows, 1 for a single row.

        Returns:
            Union[List[Dict], Dict, None]: The fetched data as a list of dictionaries, a single dictionary, or None.
        """
        self.cursor.execute(self.query, self.value)
        if size == 0:
            if res := self.cursor.fetchall():
                return [dict(r) for r in res]
        elif size == 1:
            if res := self.cursor.fetchone():
                return dict(res)

    def execute(self):
        """
        Execute the current query with the current values.
        """
        if self.value:
            if is_nested_iterable(self.value):
                self.cursor.executemany(self.query, self.value)
            else:
                self.cursor.execute(self.query, self.value)
        else:
            self.cursor.execute(self.query)
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()
