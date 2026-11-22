import cv2

image_path = "myphoto.jpg"

img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blur
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)

    cv2.imwrite("sketch.png", sketch)
    print("Sketch created successfully!")
