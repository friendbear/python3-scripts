from rembg import remove
from PIL import Image
input = input("Please input image path: ")
inp = Image.open(input)
output = remove(inp)
output.save("removed.png")