import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
from tabulate import tabulate

app = typer.Typer()

@app.command()
def loadData(): 
    """Load dataset"""
    df = pd.read_csv('menu.csv')
    table = df.iloc[[0,1],:]
    print("Successfully load dataset")
    print(table)

@app.command()
def fetchlist():
    """fetch items list"""
    df = pd.read_csv('menu.csv')
    print(df)


@app.command()
def sortbycalories():
    """return sorted list by calories"""
    df = pd.read_csv('menu.csv')
    sorted = df.sort_values(by=['Calories'],ascending = False)
    print(sorted[['Item','Calories']])

@app.command()
def seemax():
    """See max value of each dataset"""
    df = pd.read_csv('menu.csv')
    max_values = df[['Calories','Total Fat','Carbohydrates','Dietary Fiber','Sugars','Protein','Vitamin A (% Daily Value)','Vitamin C (% Daily Value)','Calcium (% Daily Value)','Iron (% Daily Value)']].max()
    print(max_values)

if __name__ == "__main__":
    app()