import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Peso e altura devem ser valores positivos!")
            return
        
        imc = peso / (altura ** 2)
        if imc < 18.5:
            resultado = f"IMC: {imc:.2f} - Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado = f"IMC: {imc:.2f} - Peso normal"
        elif 25 <= imc < 29.9:
            resultado = f"IMC: {imc:.2f} - Sobrepeso"
        else:
            resultado = f"IMC: {imc:.2f} - Obesidade"
        
        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")


def mostrar_sobre():
    messagebox.showinfo("Sobre", "Calculadora de IMC desenvolvida por Mavi Abreu")


root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x450")  
root.config(bg="#D1C4E9")  


fonte_titulo = ("Arial", 14, "bold")
fonte_input = ("Arial", 12)
fonte_resultado = ("Arial", 12, "italic")


titulo = tk.Label(root, text="Calculadora de IMC", bg="#D1C4E9", fg="#4A148C", font=fonte_titulo)
titulo.pack(pady=20)


label_peso = tk.Label(root, text="Peso (kg):", bg="#D1C4E9", fg="black", font=fonte_input)
label_peso.pack(pady=10)
entry_peso = tk.Entry(root, font=fonte_input, bd=2, relief="solid", justify="center")
entry_peso.pack(pady=5, ipadx=10, ipady=5)

label_altura = tk.Label(root, text="Altura (m):", bg="#D1C4E9", fg="black", font=fonte_input)
label_altura.pack(pady=10)
entry_altura = tk.Entry(root, font=fonte_input, bd=2, relief="solid", justify="center")
entry_altura.pack(pady=5, ipadx=10, ipady=5)


botao_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc, bg="#8A2BE2", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
botao_calcular.pack(pady=20)


botao_sobre = tk.Button(root, text="Sobre", command=mostrar_sobre, bg="#8A2BE2", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=3)
botao_sobre.pack(pady=10)

label_resultado = tk.Label(root, text="", bg="#D1C4E9", fg="black", font=fonte_resultado)
label_resultado.pack(pady=10)


root.mainloop()
