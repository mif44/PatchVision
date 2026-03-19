from PIL import UnidentifiedImageError
from src.core.image_processor import ImageProcessor


def handler_pipeline(photo: str) -> bool:
    try:
        image = ImageProcessor(photo)
        width, height = image.show_size()
        if width >= 256 and height >= 256 and max(width, height) / min(width, height) <= 1.15:
            image.prepare_image_256()
            image.processing_center_crop()
            image.processing_sharpen()

            image.save_pipeline()
            return True
        
        return False
      
    except (UnidentifiedImageError, OSError):
        return False
