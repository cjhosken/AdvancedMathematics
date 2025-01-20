import numpy, PIL

from PIL import Image

def main():
    image = Image.open("./image.png")
    image.show()
    image.save("./output.png")

main()