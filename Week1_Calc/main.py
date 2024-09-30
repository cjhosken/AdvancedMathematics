from PIL import Image, ImageDraw
import numpy as np
import cv2

# Step 1: Create a black image using Pillow
width, height = 500, 500  # You can specify any size
img = Image.new('RGB', (width, height), (0, 0, 0))

# Draw a rectangle and a point
draw = ImageDraw.Draw(img)
draw.rectangle([(10, 10), (50, 50)], fill="#ffff33")  # Draw yellow rectangle
draw.point(xy=(70, 70), fill="white")  # Draw white point

def show_and_save(name, img):
    # Convert the Pillow image to a NumPy array
    im = np.array(img)
    
    # Convert the image from RGB (Pillow) to BGR (OpenCV)
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    
    # Show the image with OpenCV
    cv2.imshow(name, im)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_and_save("yolo", img)