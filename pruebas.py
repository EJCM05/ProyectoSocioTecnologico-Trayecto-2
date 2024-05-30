import tkinter as tk

def create_frame_with_border(root):
    # Crear un canvas
    canvas = tk.Canvas(root, width=200, height=200)
    canvas.pack()

    # Crear un frame
    frame = tk.Frame(canvas, bg="white")
    frame.place(relwidth=1, relheight=1)

    # Dibujar una línea en el borde izquierdo del frame
    canvas.create_line(0, 0, 0, 200, fill="red", width=5)

root = tk.Tk()
create_frame_with_border(root)
root.mainloop()
