import pytest
from funcoes import soma, subtracao
from funcoes import multiplicacao, potencia

def test_soma():
    assert soma(2, 3)   == 5
    assert soma(-1, 1)  == 0
    assert soma(0, 0)   == 0
    assert soma(-1,-5)  == -6
    assert soma (0,-15) == -15
