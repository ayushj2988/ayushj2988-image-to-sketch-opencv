import cv2
import os

# Absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Image path (SAFE: same folder only)
img_path = os.path.join(BASE_DIR, "Img.jpg")

print("Looking for image at:", img_path)

img = cv2.imread(img_path)

if img is None:
    print("❌ Image not found.")
    print("Files in this folder:", os.listdir(BASE_DIR))
    exit()

# Convert to sketch
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (31, 31), 0)
sketch = cv2.divide(gray, blur, scale=256)

# Output path
out_path = os.path.join(BASE_DIR, "sketch.png")
cv2.imwrite(out_path, sketch)

print("✅ Done. Sketch saved at:", out_path)
