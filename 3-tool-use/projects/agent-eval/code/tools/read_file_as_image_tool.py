import os
from PIL import Image
import io
import base64

class ReadFileAsImageTool:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def execute(self, file_name):
        try:
            file_path = os.path.join(self.folder_path, file_name)
            if not os.path.exists(file_path):
                return f"File {file_name} does not exist."
            with open(file_path, 'rb') as file:
                content = file.read()

            # Convert bytes to a PIL Image
            pil_image = Image.open(io.BytesIO(content))

            # Convert the image to PNG and base64 encode it
            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            image_base64 = base64.b64encode(buffer.getvalue())

            return image_base64

        except Exception as e:
            return str(e)