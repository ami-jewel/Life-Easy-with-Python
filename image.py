# Remove image backgrounds in Python

from rembg import remove
from PIL import Image

input_path = "input.jpg"
output_path = "output.jpg"


img = Image.open(input_path)
output = remove(img)
output.save(output_path)

print("Background removed successfully.")