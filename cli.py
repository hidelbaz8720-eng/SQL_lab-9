import click
from db import get_conn

@click.group()
def cli():
    pass

@cli.command()
@click.argument("titre")
@click.option("--credits", default=3)
def add_course(titre, credits):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO COURS (titre, credits) VALUES (%s, %s)",
        (titre, credits)
    )
    conn.commit()
    conn.close()
    print("Cours ajouté")

@cli.command()
def list_courses():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM COURS")
    for row in cur.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    cli()
