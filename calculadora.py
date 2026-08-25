import sys

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return a / b

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    print("=== Calculadora Backend CLI ===")
    if len(sys.argv) > 3:
        op = sys.argv[1]
        n1 = float(sys.argv[2])
        n2 = float(sys.argv[3])
        if op == "soma":
            print(f"Resultado: {somar(n1, n2)}")
        elif op == "sub":
            print(f"Resultado: {subtrair(n1, n2)}")
        elif op == "mult":
            print(f"Resultado: {multiplicar(n1, n2)}")
        elif op == "div":
            print(f"Resultado: {dividir(n1, n2)}")
    else:
        print("Execução padrão: 10 + 5 =", somar(10, 5))
