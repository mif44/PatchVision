from pathlib import Path
from src.core.pipeline import handler_pipeline


class Batch_Processor:
    def __init__(self):
        self.count = 0
        self.missed = 0


    def process_folder(self) -> None:
        folder = Path("photos")

        pattern = {".jpg", ".jpeg", ".png"}

        for photo in folder.iterdir():
            self.count += 1

            if photo.suffix.lower() not in pattern:
                self.missed += 1
                continue
        
            ok = handler_pipeline(str(photo))

            if not ok:
                self.missed += 1

        processed = self.count - self.missed
        print(f"Processed: {self.count}, Missed: {self.missed}, Processed: {processed}")
