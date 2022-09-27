import pandas as pd
import psycopg2
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

conn = psycopg2.connect(
    dbname="nfp_boilerplate_dev",
    user="nfp_boilerplate_user"
)

cur = conn.cursor(cursor_factory=NamedTupleCursor)

@app.command()
def example1():
    """fetch notes"""
    cur.execute("SELECT * FROM notes")
    records = cur.fetchall()
    print(tabulate(records, headers="keys", tablefmt="psql"))

@app.command()
def example2():
    """fetch notes and load into pandas"""
    cur.execute("SELECT * FROM notes")
    records = cur.fetchall()
    df = pd.DataFrame(records)
    print(tabulate(df, headers="keys", tablefmt="psql"))

@app.command()
def example3(id: int):
    """fetch note by id"""
    cur.execute("SELECT * FROM notes WHERE id=%s", (id,))
    records = cur.fetchall()
    df = pd.DataFrame(records)
    df = df.transpose()
    print(tabulate(df, headers="keys", tablefmt="psql"))

if __name__ == "__main__":
    app()