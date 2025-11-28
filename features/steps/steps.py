from behave import given, when, then
from fastapi.testclient import TestClient

@given('el número A "{numero_a:d}"')
def step_set_number_a(context, numero_a):
    context.numero_a = numero_a

@given('el número B "{numero_b:d}"')
def step_set_number_b(context, numero_b):
    context.numero_b = numero_b

@when('se realiza la resta')
def step_perform_subtraction(context):
    context.payload = {
        "numero_a": context.numero_a,
        "numero_b": context.numero_b
    }
    # Nota: context.client debe inicializarse en environment.py
    context.response = context.client.post("/resta", json=context.payload)

@then('el resultado es "{resultado_esperado:d}"')
def step_check_result(context, resultado_esperado):
    # Validación HTTP
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == 200, f"Error HTTP: {context.response.status_code}. Cuerpo: {context.response.text}"

    # Parseo robusto de JSON
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta no es JSON válido: {e}. Cuerpo: {context.response.text}")

    # Contrato
    assert "resultado" in data, f"Falta el campo 'resultado' en la respuesta: {data}"
    resultado = data["resultado"]

    # Tipo y dominio: la regla de negocio exige resultado >= 0
    assert isinstance(resultado, int), f"'resultado' debe ser entero, recibido: {type(resultado)} ({resultado})"
    assert resultado >= 0, f"El resultado no puede ser negativo según la regla: {resultado}"

    # Chequeo contra lo esperado
    assert resultado == resultado_esperado, f"Esperaba {resultado_esperado}, obtuve {resultado}"

    # (Opcional) Consistencia con los operandos recibidos, si el servicio los ecoa:
    # assert data.get("numero_a") == context.numero_a
    # assert data.get("numero_b") == context.numero_b

@then('falla porque A es menor que B con estado "{status_code:d}"')
def step_check_subtraction_negative_error(context, status_code):
    assert context.response is not None, "No hay respuesta del cliente."
    assert context.response.status_code == status_code, (
        f"Código HTTP distinto al esperado ({status_code}): {context.response.status_code}. "
        f"Cuerpo: {context.response.text}"
    )

    # Cuerpo de error legible
    try:
        data = context.response.json()
    except Exception as e:
        raise AssertionError(f"Respuesta de error no es JSON válido: {e}. Cuerpo: {context.response.text}")

    # Ejemplo: {"error": "resta_negativa_no_permitida", "detalle": "numero_a debe ser >= numero_b"}
    assert "error" in data, f"Falta clave 'error' en respuesta de error: {data}"
    error_text = str(data["error"]).lower()
    # Verificación semántica 
    assert ("resta" in error_text or "subtracción" in error_text or "subtraction" in error_text) and (
            "negativ" in error_text or "menor" in error_text or "invalid" in error_text
        ), f"El mensaje no refleja que A < B viola la regla: {data}"

