from behave import given, when, then


@given('los numeros enteros {a} y {b}')
def step_given_numeros_enteros(context, a, b):
    """Almacena los dos enteros en el contexto."""
    try:
        context.a = int(a)
        context.b = int(b)
    except ValueError:
        # Mantener la excepción para que los pasos 'when' la detecten si es necesario
        context.exception = ValueError("Ambos numeros deben ser enteros no negativos")


def _perform_subtraction(context):
    """Realiza la resta con las validaciones requeridas y guarda resultado o excepción en el contexto."""
    # Si ya había una excepción previa (p. ej. al parsear), preservarla
    if hasattr(context, "exception") and context.exception is not None:
        return

    a = context.a
    b = context.b

    if a < 0 or b < 0:
        context.exception = ValueError("Ambos numeros deben ser enteros no negativos")
        return

    result = a - b
    if result < 0:
        context.exception = ValueError("El resultado de la resta no puede ser negativo")
        return

    context.result = result


@when('realizo la resta')
def step_when_realizo_la_resta(context):
    _perform_subtraction(context)


@when('intento realizar la resta')
def step_when_intento_realizar_la_resta(context):
    _perform_subtraction(context)


@then('el resultado debe ser {expected}')
def step_then_resultado_debe_ser(context, expected):
    """Verifica que el resultado almacenado en contexto coincide con el esperado."""
    assert not hasattr(context, "exception") or context.exception is None, (
        f"Se esperaba un resultado, pero se lanzó una excepción: {getattr(context, 'exception', None)}"
    )
    assert hasattr(context, "result"), "No se encontró resultado en el contexto"
    assert context.result == int(expected), f"Resultado esperado {expected}, obtenido {context.result}"


@then('se lanza una excepcion de "{message}"')
def step_then_se_lanza_una_excepcion(context, message):
    """Verifica que una excepción fue guardada en el contexto y que su mensaje coincide."""
    assert hasattr(context, "exception") and context.exception is not None, "No se lanzó ninguna excepción"
    assert str(context.exception) == message, (
        f"Se esperaba la excepción con mensaje '{message}', pero fue '{str(context.exception)}'"
    )
