from PIL import Image, ImageDraw

class AM_Canvas:
    width = 512
    height = 512
    canvas = None
    image = None

    def __init__(self, w, h, color=(0, 0, 0)):
        self.width = w
        self.height = h
        self.image=Image.new("RGB",(w, h), color)
        self.canvas=ImageDraw.Draw(self.image)

    def draw(self):
        pass

    def show(self):
        self.image.show()
    
    def save(self, name="image.png"):
        self.image.save(name)