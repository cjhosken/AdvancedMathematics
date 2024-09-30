import cv2
import numpy as np

def main():
    image = np.zeros((512, 512, 3), dtype=np.uint8)
    
    cv2.rectangle(image, (50, 50), (250, 150), (0, 255, 0), -1) # (img, tl, br, color, thickness)

    image[35, 100] = (0, 0, 255)

    # Step 5: Display the image
    cv2.imshow('Image', image)
    cv2.imwrite('image.png', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()