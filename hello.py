import tkinter as tk

def create_linear_gradient(canvas, x1, y1, x2, y2, colors):
    num_colors = len(colors)
    dx = (x2 - x1) / num_colors
    dy = (y2 - y1) / num_colors

    for i in range(num_colors):
        color = colors[i]
        canvas.create_rectangle(x1 + i * dx, y1 + i * dy, x1 + (i + 1) * dx, y2, fill=color, outline="")

def main():
    root = tk.Tk()
    root.title("Linear Gradient in Tkinter")

    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()

    # Define colors for the gradient
    gradient_colors = ["#FF0000", "#FFFF00", "#00FF00", "#0000FF"]

    # Draw linear gradient on the canvas
    create_linear_gradient(canvas, 0, 0, 300, 200, gradient_colors)

    root.mainloop()

if __name__ == "__main__":
    main()


    
