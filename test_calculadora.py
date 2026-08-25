import pytest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_media

def test_somar():
    assert somar(10, 5) == 15
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5.0

def test_divisao_por_zero():
    with pytest.raises(ValueError, match="Erro: Divisão por zero não é permitida."):
        dividir(10, 0)

def test_calcular_media():
    assert calcular_media([10, 8, 6]) == 8.0
    assert calcular_media([]) == 0
