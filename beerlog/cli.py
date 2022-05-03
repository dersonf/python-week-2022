import typer
from typing import Optional
from beerlog.core import add_beer_to_db, get_beers_from_db
from rich.table import Table
from rich.console import Console


main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add(
    # Esses precisam ser passados na ordem
    name: str,
    style: str,
    # Esses já não precisam de ordem devido o nome
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_db(name, style, flavor, image, cost):
        print("Beer successfully added!!!")
    else:
        print("Deu ruim!!!")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """List beers in database."""
    beers = get_beers_from_db()
    table = Table(title="Beerlog")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)


