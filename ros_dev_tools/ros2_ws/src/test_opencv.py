import cv2
import numpy as np

print(f"OpenCV version: {cv2.__version__}")

# Create a black image with a white rectangle
img = cv2.imread('test_image.jpg')
if img is None:
    print("No test image found. Creating one...")
    img = 255 * np.ones((200, 200, 3), dtype='uint8')
    cv2.rectangle(img, (50, 50), (150, 150), (0, 0, 255), 3)
    cv2.imwrite('test_image.jpg', img)
else:
    print("Loaded test image from file.")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Grayscale image shape: {gray.shape}")

# Show the image in a window (works only if X11 is set up)
try:
    cv2.imshow("Test Image", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
except cv2.error as e:
    print(f"cv2.imshow() failed: {e}")
    print("No GUI display, but OpenCV works for processing!")

print("✅ OpenCV test complete.")
