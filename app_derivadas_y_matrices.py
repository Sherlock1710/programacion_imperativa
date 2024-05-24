import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import sympy as sp

# Clase principal de la aplicación
class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Matrices y Derivadas")

        # Establecer tamaño de la ventana y centrarla en la pantalla
        self.root.geometry("700x700")
        self.center_window()

        # Crear pestañas
        self.tabControl = ttk.Notebook(root)
        
        self.matrix_tab = ttk.Frame(self.tabControl)
        self.derivative_tab = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.matrix_tab, text='Matrices 3x3')
        self.tabControl.add(self.derivative_tab, text='Derivadas')
        
        self.tabControl.pack(expand=1, fill="both")

        # Configurar pestaña de matrices
        self.create_matrix_tab()
        
        # Configurar pestaña de derivadas
        self.create_derivative_tab()

    # Método para centrar la ventana en la pantalla
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    # Método para configurar la pestaña de matrices
    def create_matrix_tab(self):
        font = ("Helvetica", 11)  # Reducir el tamaño de la fuente en ~20%
        tk.Label(self.matrix_tab, text="Ingrese los valores de la matriz 3x3:", font=("Helvetica", 22)).grid(row=0, column=0, columnspan=3, pady=16, sticky="ew")
        
        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(self.matrix_tab, width=4, font=("Helvetica", 14))  # Ajustar el tamaño de la fuente según sea necesario
                entry.grid(row=i+1, column=j, padx=30, pady=8, sticky="ew")
                row_entries.append(entry)
            self.entries.append(row_entries)
        
        self.solve_matrix_button = tk.Button(self.matrix_tab, text="Resolver", command=self.solve_matrix, font=("Helvetica", 22))
        self.solve_matrix_button.grid(row=4, column=0, columnspan=3, pady=16, padx=50 ,sticky="ew")

        self.matrix_result = tk.Label(self.matrix_tab, text="", font=("Helvetica", 22))
        self.matrix_result.grid(row=5, column=0, columnspan=3, pady=16, sticky="ew")

        # Configurar el grid para expandirse
        for i in range(6):
            self.matrix_tab.rowconfigure(i, weight=1)
        for j in range(3):
            self.matrix_tab.columnconfigure(j, weight=1)

    # Método para configurar la pestaña de derivadas
    def create_derivative_tab(self):
        font = ("Helvetica", 11)  # Reducir el tamaño de la fuente en ~20%
        tk.Label(self.derivative_tab, text="Ingrese la función:", font=("Helvetica", 22)).grid(row=0, column=0, columnspan=2, pady=16, sticky="ew")
        
        self.function_entry = tk.Entry(self.derivative_tab, width=40, font=("Helvetica", 22))  # Ajustar el ancho según sea necesario
        self.function_entry.grid(row=1, column=0, columnspan=2, pady=16, padx=50, sticky="ew")
        
        tk.Label(self.derivative_tab, text="Ingrese la variable:", font=("Helvetica", 22)).grid(row=2, column=0, pady=16, sticky="ew")
        
        self.variable_entry = tk.Entry(self.derivative_tab, width=8, font=("Helvetica", 22))  # Ajustar el ancho según sea necesario
        self.variable_entry.grid(row=2, column=1, pady=16, padx=110, sticky="ew")

        self.derivative_button = tk.Button(self.derivative_tab, text="Calcular Derivada", command=self.calculate_derivative, font=("Helvetica", 22))
        self.derivative_button.grid(row=3, column=0, columnspan=2, pady=16, padx=50, sticky="ew")
        
        self.derivative_result = tk.Label(self.derivative_tab, text="", font=("Helvetica", 22))
        self.derivative_result.grid(row=4, column=0, columnspan=2, pady=16, sticky="ew")

        # Configurar el grid para expandirse
        for i in range(5):
            self.derivative_tab.rowconfigure(i, weight=1)
        for j in range(2):
            self.derivative_tab.columnconfigure(j, weight=1)

    # Método para resolver la matriz
    def solve_matrix(self):
        try:
            matrix_values = []
            for row_entries in self.entries:
                row = [float(entry.get()) for entry in row_entries]
                matrix_values.append(row)

            matrix = np.array(matrix_values)
            determinant = np.linalg.det(matrix)
            inverse = np.linalg.inv(matrix)

            result_text = f"Determinante: {determinant:.2f}\nMatriz Inversa:\n{inverse}"
            self.matrix_result.config(text=result_text)
        except Exception as e:
            messagebox.showerror("Error", f"Error al resolver la matriz: {e}")

    # Método para calcular la derivada
    def calculate_derivative(self):
        try:
            function_text = self.function_entry.get()
            variable_text = self.variable_entry.get()

            x = sp.symbols(variable_text)
            function = sp.sympify(function_text)
            derivative = sp.diff(function, x)

            self.derivative_result.config(text=f"Derivada: {derivative}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la derivada: {e}")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
