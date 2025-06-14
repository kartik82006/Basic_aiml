# Cartoonify Your Image

This project is a Python GUI application that allows you to cartoonify your images using OpenCV, Pillow, Tkinter, and Matplotlib. The app provides a simple interface to select an image, process it through several image processing steps, and display the cartoonified result.

---

## Features

- **Graphical User Interface (GUI):** Built with Tkinter for easy image selection and interaction.
- **Image Processing:** Uses OpenCV for cartoonification (grayscale conversion, blurring, edge detection, bilateral filtering).
- **Visualization:** Displays each processing step and the final cartoon image using Matplotlib in a 3x2 grid.
- **File Dialogs:** Uses EasyGUI for simple file selection dialogs.

---

## Requirements

- Python 3.x

Install the required libraries with:

```bash
pip install opencv-python pillow matplotlib numpy easygui imageio
```

---

## Libraries Used

| Library     | Use Case                                   | Install Command           | Official Link                                      |
|-------------|--------------------------------------------|---------------------------|----------------------------------------------------|
| Tkinter     | GUI creation                               | Included with Python      | [Tkinter Docs](https://docs.python.org/3/library/tkinter.html) |
| Pillow      | Image processing and Tkinter compatibility | `pip install pillow`      | [Pillow](https://python-pillow.org/)               |
| OpenCV      | Image processing and cartoonification      | `pip install opencv-python` | [OpenCV](https://opencv.org/)                      |
| Matplotlib  | Displaying images and processing steps     | `pip install matplotlib`  | [Matplotlib](https://matplotlib.org/)              |
| NumPy       | Numerical operations                       | `pip install numpy`       | [NumPy](https://numpy.org/)                        |
| EasyGUI     | Simple file dialogs                        | `pip install easygui`     | [EasyGUI](https://easygui.readthedocs.io/en/master/)|
| imageio     | Image reading and writing                  | `pip install imageio`     | [imageio](https://imageio.readthedocs.io/en/stable/)|

---
Author - Kartik Gupta