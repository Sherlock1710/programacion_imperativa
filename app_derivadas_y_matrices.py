import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import sympy as sp

class MathApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Solucionador de Matrices y Derivadas")

        # Creación de pestañas
        self.tabControl = ttk.Notebook(root)
        
        self.matrix_tab = ttk.Frame(self.tabControl)
        self.derivative_tab = ttk.Frame(self.tabControl)
        
        self.tabControl.add(self.matrix_tab, text='Matrices 3x3')
        self.tabControl.add(self.derivative_tab, text='Derivadas')
        
        self.tabControl.pack(expand=1, fill="both")

        # Configuración de la pestaña de matrices
        self.create_matrix_tab()
        
        # Configuración de la pestaña de derivadas
        self.create_derivative_tab()

    def create_matrix_tab(self):
        tk.Label(self.matrix_tab, text="Ingrese los valores de la matriz 3x3:").grid(row=0, columnspan=3, pady=10)
        
        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(self.matrix_tab, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)
        
        self.solve_matrix_button = tk.Button(self.matrix_tab, text="Resolver", command=self.solve_matrix)
        self.solve_matrix_button.grid(row=4, column=1, pady=10)

        self.matrix_result = tk.Label(self.matrix_tab, text="")
        self.matrix_result.grid(row=5, columnspan=3, pady=10)

    def create_derivative_tab(self):
        tk.Label(self.derivative_tab, text="Ingrese la función:").grid(row=0, column=0, columnspan=2, pady=10)
        
        self.function_entry = tk.Entry(self.derivative_tab, width=50)
        self.function_entry.grid(row=1, column=0, columnspan=2, pady=10)
        
        tk.Label(self.derivative_tab, text="Ingrese la variable:").grid(row=2, column=0, pady=10)
        
        self.variable_entry = tk.Entry(self.derivative_tab, width=5)
        self.variable_entry.grid(row=2, column=1, pady=10)

        self.derivative_button = tk.Button(self.derivative_tab, text="Calcular Derivada", command=self.calculate_derivative)
        self.derivative_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.derivative_result = tk.Label(self.derivative_tab, text="")
        self.derivative_result.grid(row=4, column=0, columnspan=2, pady=10)

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

if _name_ == "_main_":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
