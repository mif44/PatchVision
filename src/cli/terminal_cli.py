import typer
from pathlib import Path

from src.image_processor import ImageProcessor
from utils.terminal_clear import clean_terminal

image_app = typer.Typer(help="Processing images from the `photos` folder.",
    no_args_is_help=True,
    rich_markup_mode="markdown",
    epilog="""
Examples:

python main.py image info "file name"\n
python main.py image show_size "file name"\n
python main.py image grayscale "file name"\n
python main.py image blur "file name"\n 
python main.py image invert "file name"\n
python main.py image sharpen "file name"\n
python main.py image sepia "file name"\n
python main.py image upscale "file name"\n
python main.py image resize "file name" 300 300 (width, height)\n
python main.py image resize-keep-aspect "file name" 300 300 (width, height)\n
python main.py image center-crop "file name" 300 300 (width,height)\n
""",
)

def find_image(image_name: str) -> Path | None:
    folder = Path("photos")

    for ext in (".jpg", ".jpeg", ".png"):
        candidate = folder / f"{image_name}{ext}"
        if candidate.is_file():
            return candidate
        else:
            candidate = folder / image_name
            if candidate.is_file():
                return candidate

    return None


def get_processor(image_name: str) -> ImageProcessor | None:
    found_path = find_image(image_name)

    if found_path is None:
        clean_terminal()
        print("File not found")
        return None

    return ImageProcessor(str(found_path))


@image_app.command()
def info(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    found_path = find_image(image_name)
    print(
        f"File found: {processor.name}\n"
        f"Photo size: {processor.show_size()}\n"
        f"Format: {found_path.suffix}\n"
        f"Path: {found_path}"
    )


@image_app.command("show-size")
def show_size(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    print(processor.show_size())


@image_app.command()
def grayscale(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_grayscale()


@image_app.command()
def blur(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_blur()


@image_app.command()
def invert(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_invert()


@image_app.command()
def sharpen(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_sharpen()


@image_app.command()
def sepia(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_sepia()


@image_app.command()
def upscale(image_name: str) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_upscale()


@image_app.command()
def resize(image_name: str, width: int, height: int) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_resize(width, height)


@image_app.command("resize-keep-aspect")
def resize_keep_aspect(image_name: str, width: int, height: int) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_resize_keep_aspect(width, height)


@image_app.command("center-crop")
def center_crop(image_name: str, width: int, height: int) -> None:
    processor = get_processor(image_name)
    if processor is None:
        return

    processor.save_center_crop(width, height)