import pytest
from conversor import converter_dolar_para_real

def test_conversor_sucesso():
    # Testando conversões normais com ponto flutuante
    assert converter_dolar_para_real(10.0, 5.5) == 55.0
    assert converter_dolar_para_real(100.0, 5.0) == 500.0
    assert converter_dolar_para_real(5.40, 5.50) == 29.7

def test_conversor_valores_negativos():
    # Garante que a função dispara erro se receber valores inválidos
    with pytest.raises(ValueError):
        converter_dolar_para_real(-10, 5.5)
        
    with pytest.raises(ValueError):
        converter_dolar_para_real(10, -5.5)
