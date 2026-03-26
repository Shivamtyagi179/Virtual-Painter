import cv2
import numpy as np

# Define image size
width = 1280
height = 125

# Each button is 125px wide
buttons = [
    ("red.png", (170, 295), (0, 0, 255)),      # Red
    ("blue.png", (436, 561), (255, 0, 0)),     # Blue
    ("green.png", (700, 825), (0, 255, 0)),    # Green
    ("eraser.png", (980, 1105), (0, 0, 0))     # Eraser
]

for filename, (x1, x2), color in buttons:
    img = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background
    cv2.rectangle(img, (x1, 0), (x2, height), color, -1)
    cv2.putText(img, filename.split('.')[0].capitalize(), (x1 + 5, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
    cv2.imwrite(filename, img)
    print(f"[✅ Created] {filename}")

print("\nAll header images generated successfully.")
