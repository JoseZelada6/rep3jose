import tkinter as tk
from tkinter import messagebox

def sumar_numeros():
    num1= float (entrada_num1.get())
    num2= float (entrada_num2.get())
    resultado = num1 + num2 
    messagebox.showinfo("Resultado", f"la suma es: {resultado}" )

ventana=tk.Tk()
ventana.title=("Operaciones Aritmeticas")

etiqueta_num1=tk.Label(ventana, text="número 1: ")
etiqueta_num1.grid(row=0, column=0, padx=10, pady=10)

etiqueta_num2=tk.Label(ventana, text="número 2: ")
etiqueta_num2.grid(row=1, column=0, padx=10, pady=10)

#Creación de campos de entrada

entrada_num1=tk.Entry(ventana)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)

entrada_num2=tk.Entry(ventana)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

ventana.mainloop()