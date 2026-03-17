from src.image_processor import ImageProcessor
from pathlib import Path
from utils.terminal_clear import clean_terminal
from src.gui.terminal_information import terminal_information

if __name__ == "__main__":
    image_name = input("Enter the photo title: ").strip()
    clean_terminal()
    folder = Path("photos")

    found_path = None

    for ext in (".jpg", ".jpeg", ".png"):
        candidate = folder / f"{image_name}{ext}"
        if candidate.is_file():
            found_path = candidate
            break

    if found_path is not None:
        image = ImageProcessor(found_path)
        print(f"File found: {image.name}\nPhoto size: {image.show_size()}\nFormat: {ext},\nPath: {found_path}")
    else:
        clean_terminal()
        print("File not found")


