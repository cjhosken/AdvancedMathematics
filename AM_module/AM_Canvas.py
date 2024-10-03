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
        self.draw_grid()
        pass

    def draw_grid(self, spacing=50, color=(50, 50, 50), axis_color=(100, 100, 100)):
        self.canvas.line([(0,self.height/2),(self.width,self.height/2)],axis_color)
        self.canvas.line([(self.width/2,0),(self.width/2,self.height)],axis_color)

    def show(self):
        self.image.show()
    
    def save(self, name="image.png"):
        out_image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        out_image.save(name)