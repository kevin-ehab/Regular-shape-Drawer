# 🔷Regular-shape-Drawer

This is a simple Python desktop app that allows users to draw regular shapes (like triangles, squares, pentagons, etc.) using the `turtle` graphics library. The shape's number of sides and side length are user-defined through a Tkinter GUI.

This is one of **my earliest and most favourite projects**.

---

## 📌 Features

- GUI built using **Tkinter**
- Dynamic shape rendering with **Turtle**
- Randomly colored sides for visual variety
- User inputs:  
  - Side length  
  - Number of sides

---

## 🛠️ How It Works

1. The user enters the **length of each side** and the **number of sides** in the GUI.
2. Upon clicking **Submit**, a turtle window opens and draws the shape.
3. Each side is given a randomly selected color from a predefined list.

---

## 🧪 Example

- Enter:  
  - Length: `100`  
  - Sides: `5`  
- Output: A colorful pentagon drawn on the screen.

---

## 🧑‍💻 Technologies Used

- `tkinter` for the GUI  
- `turtle` for drawing graphics  
- `random` for selecting colors

---

## 📝 Code Structure

- `Shape(length, side)`: Draws a regular polygon using turtle.
- `click()`: Reads input from GUI and calls the `Shape()` function.
- `Tkinter` widgets:
  - Labels and entries for input
  - Submit button to trigger drawing

---

## 🚀 How to Run

1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python shape_maker.py
