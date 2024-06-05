from duckdb import DuckDBPyConnection


def table_exists(conn: DuckDBPyConnection, table: str) -> bool:
    """
    Checks if a table exists in a duckdb database

    >>> if not table_exists(conn, 'table1'):
    >>>     # raise error
    """
    query = f"""SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{table}'"""
    result = conn.execute(query).fetchone()
    if result is None:
        return False

    return result[0] > 0

def insert_record(conn: DuckDBPyConnection, table: str, record: dict) -> None:
    """
    Inserts a record into a table

    >>> insert_record(conn, 'table1', {'name': 'yolo', 'age': 32, 'city': 'yolo'})
    """
    values = record.values()
    insert_record = f"INSERT INTO {table} VALUES ("
    for r in values:
        insert_record += f"'{r}',"
    insert_record = insert_record[:-1] + ")"
    conn.execute(insert_record)

def insert_bulk_records(conn: DuckDBPyConnection, table: str, records: list[dict]) -> None:
    """
    Inserts multiple records into a table

    >>> insert_bulk_records(conn, 'table1', [{'name': 'yolo', 'age': 32, 'city': 'yolo'}, {'name': 'yolo', 'age': 32, 'city': 'yolo'}])
    """
    if len(records) == 0:
        return

    insert_query = f"INSERT INTO {table} VALUES (" + ", ".join(["?" for r in records[0].values()]) + ")"

    raw_records = [list(r.values()) for r in records]
    conn.executemany(insert_query, raw_records)
