import typer
from src.cli.terminal_cli_image import image_app
from src.cli.terminal_cli_pipeline import pipeline_app

app = typer.Typer(help="Main CLI\n" \
"python main.py image --help\n" \
"python main.py pipeline --help")
app.add_typer(image_app, name="image")
app.add_typer(pipeline_app, name="pipeline")

if __name__ == "__main__":
    app()