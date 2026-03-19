import os


from PIL import Image, ImageOps, ImageFilter


class ImageProcessor:
    def __init__(self, path: str):
        with Image.open(path) as image:
            self.name = os.path.basename(path)
            self.file_name = os.path.splitext(self.name)[0] 
            self.image = image.copy()
            self.format = os.path.splitext(self.name)[1]
        

    def show_size(self) -> tuple:
        return self.image.size

    
    def save_grayscale(self) -> None:
        image = self.image.convert("L")
        image.save(f"assets/grayscale/{self.file_name}_gray.jpg")
        print("The photo has been saved.")

    
    def save_blur(self) -> None:
        image = self.image.filter(filter=ImageFilter.BLUR)
        image.save(f"assets/blur/{self.file_name}_blur.jpg")
        print("The photo has been saved.")

    
    def save_invert(self) -> None:
        mode = self.image.mode
        if mode in ["RGB", "L"]:
            image = ImageOps.invert(self.image)
            image.save(f"assets/invert/{self.file_name}_invert.jpg")
            print("The photo has been saved.")
        else:
            raise ValueError("Incorrect photo mode")

    
    def save_sharpen(self) -> None:
        image = self.image.filter(filter=ImageFilter.SHARPEN)
        image.save(f"assets/sharpen/{self.file_name}_sharpen.jpg")
        print("The photo has been saved.")

    
    def save_sepia(self) -> None:
        image = self.image.convert("RGB")

        sepia_matrix = (
            0.393, 0.769, 0.189, 0,
            0.349, 0.686, 0.168, 0,
            0.272, 0.534, 0.131, 0,
        )

        sepia = image.convert("RGB", sepia_matrix)
        sepia.save(f"assets/sepia/{self.file_name}_sepia.jpg")
        print("The photo has been saved.")

    
    def save_upscale(self) -> None:
        image = self.image.resize((self.image.width * 2, self.image.height * 2), Image.Resampling.LANCZOS)
        image.save(f"assets/upscale/{self.file_name}_upscale.jpg")
        print("The photo has been saved.")

    
    def data_entry_verification(self, width: int, height: int) -> bool:
        if not isinstance(width, int) or not isinstance(height, int):
            print("Incorrect data provided")
            return False
        elif isinstance(width, bool) or isinstance(height, bool):
            print("Incorrect data provided")
            return False
        elif width <= 0 or height <=0:
            print("Width and height must be greater than 0")
            return False
        else:
            return True

   
    def save_resize(self, width: int, height: int) -> None:
        if not self.data_entry_verification(width, height):
            return
        
        image = self.image.resize((width, height), Image.Resampling.LANCZOS)
        image.save(f"assets/resize/{self.file_name}_{width}x{height}.jpg")
        print("The photo has been saved.")

    
    def save_resize_keep_aspect(self, width: int, height: int) -> None:
        if not self.data_entry_verification(width, height):
            return 
        
        image = ImageOps.contain(self.image, (width, height))
        wid, hei = image.size
        image.save(f"assets/resize_keep_aspect/{self.file_name}_{wid}x{hei}.jpg")
        print("The photo has been saved.")

    
    def save_center_crop(self, width: int, height: int) -> None:
        if not self.data_entry_verification(width, height):
            return
        
        if width > self.image.width or height > self.image.height:
            return
        
        wid, hei = self.image.size
        x = wid / 2
        y = hei / 2
        left = x - (width/2)
        right = x + (width/2)
        top = y - (height/2)
        bottom = y + (height/2)
        image = self.image.crop((int(left), int(top), int(right), int(bottom)))
        image.save(f"assets/center_crop/{self.file_name}_{width}x{height}.jpg")
        print("The photo has been saved.")
    

    def prepare_image_256(self, width: int = 256 ,height: int = 256) -> None:
        self.image = ImageOps.contain(self.image, (width, height))
        return self.image


    def processing_center_crop(self, width: int = 224 ,height: int = 224) -> None:
        wid, hei = self.image.size
        x = wid / 2
        y = hei / 2
        left = x - (width/2)
        right = x + (width/2)
        top = y - (height/2)
        bottom = y + (height/2)
        self.image = self.image.crop((int(left), int(top), int(right), int(bottom)))
        return self.image
    
    def processing_sharpen(self) -> None:
        self.image = self.image.filter(filter=ImageFilter.SHARPEN)
        return self.image
    

    def save_pipeline(self) -> None:
        self.image.save(f"assets/output/{self.file_name}{self.format}")