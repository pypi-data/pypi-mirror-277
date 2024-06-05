import csv
import json
from typing import Callable, Any
from urllib.parse import urlparse

from tqdm import tqdm

from gendit import core, _duckdb

AUTO=core.Format.AUTO
CSV=core.Format.CSV
JSON=core.Format.JSON
PARQUET=core.Format.PARQUET
DUCKDB=core.Format.DUCKDB


def generate_file(
    data_generator: Callable[[], dict],
    output: str, row: int,
    sorting: Callable[[dict], Any] | None = None,
    options: dict | None = None,
    format: str = AUTO
):
    """
    Generates a file from a data generator
    """
    if options is None:
        options = {}

    if format == core.Format.AUTO:
        format_attempt = core.detect_file_format(output)
        if format_attempt is None:
            raise ValueError(f"Output format detection failed for `{output}`, use format argument to specify the output format")
        format = format_attempt

    if sorting is not None:
        generator = iter(sorted([data_generator() for _ in range(row)], key=sorting))
    else:
        generator = (data_generator() for _ in range(row))

    if format == core.Format.CSV:
        with open(output, 'w') as filep:
            firstrow = next(generator)
            writer = csv.DictWriter(filep, fieldnames=firstrow.keys(), delimiter=options.get('delimiter', ','))
            if options.get('header', False):
                writer.writeheader()

            writer.writerow(firstrow)
            for i in tqdm(range(row - 1)):
                writer.writerow(next(generator))

    if format == core.Format.JSON:
        indent = options.get('indent', None)
        with open(output, 'w') as filep:
            json.dump([
                next(generator) for _ in tqdm(range(row))
            ], filep, indent=indent)

    if format == core.Format.PARQUET:
        import pyarrow as pa
        import pyarrow.parquet as pq

        records = [next(generator) for _ in tqdm(range(row))]
        pa_arrays = []
        for k in records[0].keys():
            pa_arrays.append(pa.array([r[k] for r in records]))

        table = pa.Table.from_arrays(pa_arrays, names=list(records[0].keys()))  # type: ignore
        pq.write_table(table, output)


def populate_db(
    data_generator: Callable[[], dict],
    db: str,
    table: str,
    row: int,
    sorting: Callable[[dict], Any] | None = None,
    options: dict | None = None,
    format: str = AUTO
) -> None:
    """
    Generates a file from a data generator
    """
    if options is None:
        options = {}

    if format == core.Format.AUTO:
        format_attempt = core.detect_db_format(db)
        if format_attempt is None:
            raise ValueError(f"Db format detection failed for `{db}`, use format argument to specify the output format")

        format = format_attempt

    if sorting is not None:
        generator = iter(sorted([data_generator() for _ in range(row)], key=sorting))
    else:
        generator = (data_generator() for _ in range(row))

    if format == core.Format.DUCKDB:
        import duckdb
        db_parts = urlparse(db)
        conn = duckdb.connect(db_parts.netloc)
        try:

            if not _duckdb.table_exists(conn, table):
                raise ValueError(f"Table `{table}` does not exist in the database {db}")

            records = []
            bulk_size = options.get('bulk_size', 1000)
            for i in tqdm(range(row)):
                next_record = next(generator)
                records.append(next_record)

                if len(records) == bulk_size:
                    _duckdb.insert_bulk_records(conn, table, records)
                    records = []

            _duckdb.insert_bulk_records(conn, table, records)
        finally:
            if conn is not None:
                conn.close()



