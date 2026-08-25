import tkinter as tk
from tkinter import messagebox

# =====================================================================
# 1. FUNÇÕES MATEMÁTICAS (LÓGICA TESTÁVEL)
# =====================================================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero!")
    return a / b

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# =====================================================================
# 2. INTERFACE GRÁFICA (EXECUTADA APENAS DIRETO NO PYTHON)
# =====================================================================

def criar_interface():
    def executar_operacao(tipo):
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            
            if tipo == 'soma':
                resultado = somar(num1, num2)
            elif tipo == 'sub':
                resultado = subtrair(num1, num2)
            elif tipo == 'mult':
                resultado = multiplicar(num1, num2)
            elif tipo == 'div':
                resultado = dividir(num1, num2)
                
            lbl_resultado.config(text=f"Resultado: {resultado}", fg="blue")
        except ValueError as e:
            messagebox.showerror("Erro", str(e) if "Divisão" in str(e) else "Insira números válidos.")

    def executar_media():
        try:
            texto = entry_media.get()
            if not texto:
                raise ValueError
            
            numeros = [float(x.strip()) for x in texto.split(',')]
            resultado = calcular_media(numeros)
            lbl_resultado.config(text=f"Média: {resultado}", fg="green")
        except ValueError:
            messagebox.showerror("Erro", "Insira números válidos separados por vírgula.")

    janela = tk.Tk()
    janela.title("Calculadora Completa")
    janela.geometry("400x480")
    janela.resizable(False, False)

    tk.Label(janela, text="--- Operações Básicas ---", font=("Arial", 11, "bold")).pack(pady=10)

    frame_inputs = tk.Frame(janela)
    frame_inputs.pack()

    tk.Label(frame_inputs, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
    entry_num1 = tk.Entry(frame_inputs, width=15)
    entry_num1.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
    entry_num2 = tk.Entry(frame_inputs, width=15)
    entry_num2.grid(row=1, column=1, padx=5, pady=5)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=15)

    tk.Button(frame_botoes, text="+", width=6, command=lambda: executar_operacao('soma')).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes, text="-", width=6, command=lambda: executar_operacao('sub')).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes, text="*", width=6, command=lambda: executar_operacao('mult')).grid(row=0, column=2, padx=5)
    tk.Button(frame_botoes, text="/", width=6, command=lambda: executar_operacao('div')).grid(row=0, column=3, padx=5)

    tk.Label(janela, text="--- Média Aritmética ---", font=("Arial", 11, "bold")).pack(pady=10)
    entry_media = tk.Entry(janela, width=35)
    entry_media.pack(pady=5)

    tk.Button(janela, text="Calcular Média", command=executar_media, bg="#d1e7dd").pack(pady=5)

    lbl_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 14, "bold"))
    lbl_resultado.pack(pady=20)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
