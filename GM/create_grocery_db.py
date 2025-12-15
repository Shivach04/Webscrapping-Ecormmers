"""
Create and populate an SQLite grocery DB from CSV files in the same folder.

Usage (PowerShell):
  python .\GM\create_grocery_db.py

This script:
 - Creates `grocery.db` in the `GM` folder
 - Executes the schema in `schema.sql`
 - Loads CSV files: Categories, Suppliers, Products, Customers, Store_Employees, Orders, OrderDetails
 - Prints row counts after import

This implementation uses only Python stdlib (sqlite3, csv, os).
"""
import sqlite3
import csv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "grocery.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def read_schema(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def convert_value(col: str, val: str):
    if val is None:
        return None
    s = val.strip()
    if s == "":
        return None
    # integer-like columns
    col_low = col.lower()
    try:
        if col_low.endswith("id") or col_low in ("quantity",):
            return int(float(s))
        if "price" in col_low or col_low in ("priceeach", "totalprice"):
            return float(s)
    except Exception:
        # fallback to string if conversion fails
        return s
    return s


def load_csv_into_table(conn: sqlite3.Connection, csv_path: Path, table_name: str):
    with open(csv_path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames
        if not cols:
            print(f"Skipping empty CSV: {csv_path}")
            return 0
        placeholders = ",".join(["?" for _ in cols])
        col_list = ",".join([f'"{c}"' for c in cols])
        insert_sql = f"INSERT INTO {table_name} ({col_list}) VALUES ({placeholders})"
        to_insert = []
        for row in reader:
            values = [convert_value(c, row.get(c)) for c in cols]
            to_insert.append(values)
        cur = conn.cursor()
        cur.executemany(insert_sql, to_insert)
        conn.commit()
        return len(to_insert)


def main():
    print("Creating SQLite DB at:", DB_PATH)
    if DB_PATH.exists():
        print("Note: existing DB will be overwritten. Removing old DB.")
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")

    # Create schema
    schema = read_schema(SCHEMA_PATH)
    conn.executescript(schema)
    print("Schema created.")

    # Mapping CSV file names to table names (folder contains these CSVs)
    csv_table_map = [
        (BASE_DIR / "Categories.csv", "Categories"),
        (BASE_DIR / "Suppliers.csv", "Suppliers"),
        (BASE_DIR / "Products.csv", "Products"),
        (BASE_DIR / "Customers.csv", "Customers"),
        (BASE_DIR / "Store_Employees.csv", "Store_Employees"),
        (BASE_DIR / "Orders.csv", "Orders"),
        (BASE_DIR / "OrderDetails.csv", "OrderDetails"),
    ]

    for path, table in csv_table_map:
        if path.exists():
            print(f"Loading {path.name} -> {table}")
            cnt = load_csv_into_table(conn, path, table)
            print(f"Inserted {cnt} rows into {table}")
        else:
            print(f"CSV not found, skipping: {path}")

    # Print table counts
    cur = conn.cursor()
    print('\nTable row counts:')
    for _, table in csv_table_map:
        try:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            c = cur.fetchone()[0]
            print(f" - {table}: {c}")
        except Exception as e:
            print(f" - {table}: error ({e})")

    conn.close()
    print('\nDB creation complete. File:', DB_PATH)


if __name__ == '__main__':
    main()
