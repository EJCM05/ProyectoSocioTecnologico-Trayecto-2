import customtkinter as ctk

class GradosVentana:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()

        # Crear un nuevo Label dentro del área de contenido
        self.label = ctk.CTkLabel(master=self.master,
                                  text="Sección de Grados",
                                  fg_color="white")
        self.label.place(relx=0.5, rely=0.5, anchor="center")
