# 🎨 Virtual Painter

A computer vision–based application that enables users to draw on a virtual canvas using hand gestures captured through a webcam. The system detects and tracks hand movements in real time and converts them into digital strokes, providing a touch-free interactive drawing experience.

---

## 📸 Project Preview

![WhatsApp Image 2026-03-31 at 10 36 40 PM](https://github.com/user-attachments/assets/efd0e83b-330a-48c2-9cc7-ba4926607960)



---

## 🚀 Features

* ✋ Hand gesture recognition for drawing
* 🎥 Real-time webcam input processing
* 🎨 Multiple color selection
* 🧽 Eraser functionality
* ⚡ Smooth and responsive drawing experience
* 🖥️ Simple and intuitive UI

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * OpenCV
  * NumPy
  * MediaPipe (for hand tracking)

---

## 📂 Project Structure

```
Virtual-Painter/
│
├── assets/               # Images, GIFs, demo files
├── main.py               # Main application file
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-shivamtyagi179/virtual-painter.git
cd virtual-painter
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

### Controls:

* **Index Finger Up:** Draw
* **Index + Middle Finger Up:** Selection mode
* **Move Hand:** Draw on canvas

---

## 📌 How It Works

1. Captures live video using webcam
2. Detects hand landmarks using MediaPipe
3. Tracks fingertip positions
4. Maps movements onto a virtual canvas
5. Renders drawing in real time

---

## 📦 Requirements

Example `requirements.txt`:

```
opencv-python
mediapipe
numpy
```

---

## 🔧 Future Improvements

* Add shape recognition (circle, rectangle, etc.)
* Save drawings as image files
* Add gesture-based undo/redo
* Improve UI with toolbar and brush sizes

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author
 Name- Shivam tyagi
 
GitHub: [https://github.com/shivamtyagi179]

---

⭐ If you like this project, consider giving it a star!
