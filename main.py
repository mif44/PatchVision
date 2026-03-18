import typer
from src.cli.terminal_cli import image_app

app = typer.Typer(help="Main CLI\n" \
"python main.py image --help")
app.add_typer(image_app, name="image")

if __name__ == "__main__":
    app()