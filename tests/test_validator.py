import pytest

def restar(a: int, b: int) -> int:
    return a - b

def test_division_exitosa_enteros():
    assert restar(10, 3) == 7
    
@pytest.mark.parametrize("minuendo, sustraendo, esperado", [
    (10, 5, 5),     # Positivo - Positivo = Positivo
    (5, 5, 0),      # Igual - Igual = Cero
    (10, 0, 10),    # Cero en sustraendo
    (0, 0, 0),      # Cero - Cero
    (200, 150, 50)  # Grandes positivos
])
def test_resta_exitosa_resultado_no_negativo(minuendo, sustraendo, esperado):
    assert restar(minuendo, sustraendo) == esperado

def test_resta_resultado_negativo():
    with pytest.raises(Exception) as excinfo:
        restar(5, 10) # 5 < 10, resultado sería -5
    assert str(excinfo.value) == "El resultado de la resta no puede ser negativo"

@pytest.mark.parametrize("minuendo, sustraendo", [
    (-5, 10),     # Minuendo negativo
    (10, -5),     # Sustraendo negativo
    (10, 3.5),    # Sustraendo flotante
    (3.5, 5),     # Minuendo flotante
    (10, "a")     # Sustraendo no numérico
])
def test_numeros_de_entrada_no_validos(minuendo, sustraendo):
    with pytest.raises(Exception) as excinfo:
        restar(minuendo, sustraendo)
    assert str(excinfo.value) == "Ambos numeros deben ser enteros no negativos"
