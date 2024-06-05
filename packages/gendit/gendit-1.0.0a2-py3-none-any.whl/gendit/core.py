class Format:
    CSV = 'CSV'
    JSON = 'JSON'
    JSONL = 'JSONL'
    YAML = 'YAML'
    PARQUET = 'PARQUET'
    DUCKDB = 'DUCKDB'
    SQLITE = 'SQLITE'
    AUTO = 'AUTO'

def detect_db_format(db: str) -> str | None:
    """
    Detects the format to use from the db connection string.

    >>> detect_db_format('duckdb://file.db') # DUCKDB
    """
    if db.startswith('duckdb://'):
        return Format.DUCKDB

    return None

def detect_file_format(file: str) -> str | None:
    """
    Detects the format to use from the file name.

    >>> detect_file_format('output.csv') # CSV
    >>> detect_file_format('output.json') # JSON
    """
    if file.endswith('.csv'):
        return Format.CSV

    if file.endswith('.json'):
        return Format.JSON

    if file.endswith('.parquet'):
        return Format.PARQUET

    return None
