import pytest
from calculadora import somar, subtrair, multiplicar, dividir, calcular_media

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_calcular_media():
    assert calcular_media([10, 8, 6]) == 8
    assert calcular_media([]) == 0
