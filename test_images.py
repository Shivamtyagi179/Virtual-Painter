import cv2

# List of image files to check
image_files = ['red.png', 'blue.png', 'green.png', 'eraser.png']

# Loop through and try to load each
for file in image_files:
    img = cv2.imread(file)
    if img is None:
        print(f"[❌ FAILED] Could NOT read: {file}")
    else:
        print(f"[✅ OK] Loaded: {file} — Size: {img.shape}")
