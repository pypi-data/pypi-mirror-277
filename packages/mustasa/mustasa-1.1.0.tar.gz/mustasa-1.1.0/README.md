# Mustasa: SQL Database Wrapper

Mustasa is a software package that offers a unified interface for connecting to and interacting with various database engines, including SQLite, MySQL, and PostgreSQL. This package simplifies database management by abstracting the underlying complexities of each database engine, providing a consistent and user-friendly API for developers. Whether you are working with lightweight, embedded databases like SQLite, or more robust, server-based databases like MySQL and PostgreSQL, Mustasa ensures seamless integration and operation, allowing developers to focus on building applications rather than managing database connections and queries.

## Installation

```
Dependencies:

- Python 3.11 or greater

Installation:

$ pip install mustasa
```

## Synchronous Connections

For synchronous connections, use the following code:

```python
from mustasa import connect

# SQLite
db = connect.sqlite3("database.db")

# MySQL
db = connect.mysql(database="mydatabase", host="localhost", user="myuser", password="mypassword", port=3306)

# PostgreSQL
db = connect.postgresql(database="mydatabase", host="localhost", user="myuser", password="mypassword", port=5432)
```

## Asynchronous Connections (with asyncio)

For asynchronous connections using asyncio, use the following code:

```python
from mustasa.asyncio import connect

# SQLite
db = await connect.sqlite3("database.db")

# PostgreSQL
db = await connect.postgresql(database="mydatabase", host="localhost", user="myuser", password="mypassword", port=5432)
```

> **_NOTE:_** Asynchronous connections are currently not supported for MySQL in this package.

## Executing Queries

After establishing a connection, you can execute queries using the query and value properties, and then call the fetch or execute methods.

```python
# Set the query and values
db.query = "SELECT * FROM users WHERE name = ? AND email = ?;"
db.value = ("John Doe", "john@example.com")

# Fetch a single row
result = db.fetch(size=1)

# Fetch all rows
results = db.fetch(size=0)

# Execute an INSERT or UPDATE query at once
db.query = "INSERT INTO users (name, email) VALUES (?, ?);"
db.value = ("John Doe", "john@example.com")
db.execute()

# Execute an INSERT or UPDATE query at many
db.query = "INSERT INTO users (name, email) VALUES (?, ?);"
db.value = [("Sam Smith", "sam@example.com"), ("Adam Page", "adam@example.com")]
db.execute()
```

After you are done with the connection, do not forget to close it:

```python
db.close() # or await db.close()
```
