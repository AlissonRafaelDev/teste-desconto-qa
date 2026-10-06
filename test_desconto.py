import pytest
from desconto import calcular_desconto


# ---------- Cenários válidos (Critérios de Aceite) ----------
@pytest.mark.parametrize("valor, tipo, esperado", [
    (50,      "COMUM", 0.00),     # 1
    (50,      "VIP",   2.50),     # 2
    (99.99,   "COMUM", 0.00),     # 3
    (100,     "COMUM", 10.00),    # 4  limite exato
    (100,     "VIP",   15.00),    # 5  limite exato
    (300,     "COMUM", 30.00),    # 6
    (300,     "VIP",   45.00),    # 7
    (499.99,  "COMUM", 50.00),    # 8
    (500,     "COMUM", 100.00),   # 9  limite exato
    (500,     "VIP",   125.00),   # 10 limite exato
    (800,     "COMUM", 160.00),   # 11
    (1000,    "COMUM", 200.00),   # 12 teto exato
    (1000,    "VIP",   200.00),   # 13 teto aplicado
    (5000,    "COMUM", 200.00),   # 14
    (5000,    "VIP",   200.00),   # 15
    (0,       "COMUM", 0.00),     # 20
    (333.33,  "COMUM", 33.33),    # 26
])
def test_calculo_desconto(valor, tipo, esperado):
    assert calcular_desconto(valor, tipo) == esperado


# ---------- Variações de escrita do tipo de cliente ----------
@pytest.mark.parametrize("tipo, esperado", [
    ("vip",    45.00),   # 16
    ("Vip",    45.00),   # 17
    (" VIP ",  45.00),   # 18
    ("comum",  30.00),   # 19
])
def test_tipo_cliente_case_insensitive(tipo, esperado):
    assert calcular_desconto(300, tipo) == esperado


# ---------- Dados inesperados ----------
def test_valor_negativo_deve_gerar_erro():          # 21
    with pytest.raises(ValueError):
        calcular_desconto(-100, "VIP")


def test_tipo_cliente_invalido_deve_gerar_erro():   # 22
    with pytest.raises(ValueError):
        calcular_desconto(300, "PREMIUM")


def test_tipo_cliente_nulo_deve_gerar_erro():       # 23
    with pytest.raises(TypeError):
        calcular_desconto(300, None)


def test_valor_nulo_deve_gerar_erro():              # 24
    with pytest.raises(TypeError):
        calcular_desconto(None, "COMUM")


def test_valor_texto_deve_gerar_erro():             # 25
    with pytest.raises(TypeError):
        calcular_desconto("abc", "COMUM")