def restar(a, b):
    """Resta segura de dos enteros no negativos.

    Reglas:
    - Ambos operandos deben ser enteros y >= 0.
    - Si la resta resulta negativa se lanza una excepción con el mensaje esperado.

    Mensajes de excepción (para que los tests los chequen exactamente):
    - "Ambos numeros deben ser enteros no negativos"
    - "El resultado de la resta no puede ser negativo"
    """
    # Validar tipos y dominio
    if not (isinstance(a, int) and isinstance(b, int)):
        raise Exception("Ambos numeros deben ser enteros no negativos")
    if a < 0 or b < 0:
        raise Exception("Ambos numeros deben ser enteros no negativos")

    resultado = a - b
    if resultado < 0:
        raise Exception("El resultado de la resta no puede ser negativo")

    return resultado
