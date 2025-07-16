from rembg import remove
from PIL import Image
input_path = "photo.jpeg"
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
