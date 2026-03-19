import typer


from src.core.batch_processor import Batch_Processor


pipeline_app = typer.Typer(help="Processing images from the `photos` folder.",
    no_args_is_help=True,
    rich_markup_mode="markdown",
    epilog="""
Examples:
python main.py pipeline pipeline
""",
)

@pipeline_app.command("pipeline")
def get_pipeline():
    processor = Batch_Processor()
    processor.process_folder()