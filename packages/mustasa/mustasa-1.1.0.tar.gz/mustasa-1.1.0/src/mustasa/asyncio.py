import aiosqlite
import asyncpg
import re
import typing as t

from .functions import is_nested_iterable


class connect:
    """
    A class for establishing and managing database connections.

    Attributes:
        connection: The database connection object.
        cursor: The database cursor object (for SQLite only).
        engine: The database engine being used ("sqlite3" or "postgresql").
    """

    def __init__(self, connection, cursor, engine):
        self.connection = connection
        self.cursor = cursor
        self.engine = engine

    @classmethod
    async def sqlite3(cls, filename: str) -> "connect":
        """
        Create a connection to a SQLite database.

        Args:
            filename (str): The name of the SQLite database file.

        Returns:
            connect: A connect instance with a SQLite connection.
        """
        connection = await aiosqlite.connect(filename)
        connection.row_factory = aiosqlite.Row
        cursor = await connection.cursor()
        return cls(connection, cursor, "sqlite3")

    @classmethod
    async def postgresql(
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
        connection = await asyncpg.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port,
        )
        return cls(connection, None, "postgresql")

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
        Set the query string, with placeholders replaced for PostgreSQL.

        Args:
            query (str): The query string to be set.
        """
        if self.engine == "postgresql":
            placeholder = ",".join(["${}".format(i+1) for i in range(query.count("?"))])
            query = re.sub(r"\?", "{}", query).format(*placeholder.split(","))
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

    async def fetch(self, size: t.Optional[int] = 1) -> t.Union[t.List[t.Dict], t.Dict, None]:
        """
        Fetch data from the database based on the current query and values.

        Args:
            size (Optional[int]): The number of rows to fetch. 0 for all rows, 1 for a single row.

        Returns:
            Union[List[Dict], Dict, None]: The fetched data as a list of dictionaries, a single dictionary, or None.

        Raises:
            ValueError: If the `size` argument is not 0 or 1.
        """
        if self.engine == "sqlite3":
            await self.cursor.execute(self.query, self.value)
            if size == 0:
                if res := await self.cursor.fetchall():
                    return [dict(r) for r in res]
            elif size == 1:
                if res := await self.cursor.fetchone():
                    return dict(res)
            else:
                raise ValueError
        elif self.engine == "postgresql":
            if size == 0:
                if self.value:
                    res = await self.connection.fetch(self.query, *self.value)
                else:
                    res = await self.connection.fetch(self.query)
                return [dict(r) for r in res]
            elif size == 1:
                if self.value:
                    res = await self.connection.fetchrow(self.query, *self.value)
                else:
                    res = await self.connection.fetchrow(self.query)
                return dict(res)
            else:
                raise ValueError

    async def execute(self):
        """
        Execute the current query with the current values.
        """
        if self.engine == "sqlite3":
            if self.value:
                if is_nested_iterable(self.value):
                    await self.cursor.executemany(self.query, self.value)
                else:
                    await self.cursor.execute(self.query, self.value)
            else:
                await self.cursor.execute(self.query)
            await self.connection.commit()
        elif self.engine == "postgresql":
            if self.value:
                if is_nested_iterable(self.value):
                    await self.connection.executemany(self.query, self.value)
                else:
                    await self.connection.execute(self.query, *self.value)
            else:
                await self.connection.execute(self.query)

    async def close(self):
        """
        Close the database connection.
        """
        await self.connection.close()
