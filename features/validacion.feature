# language: es
Característica: Resta de dos numeros enteros no negativos en base 10
  
  Escenario: Resta exitosa con resultado positivo
    Dado los numeros enteros 20 y 5
    Cuando realizo la resta
    Entonces el resultado debe ser 15

  Escenario: Intento de resta que produce un resultado negativo
    Dado los numeros enteros 5 y 20
    Cuando intento realizar la resta
    Entonces se lanza una excepcion de "El resultado de la resta no puede ser negativo"

  Escenario: Intento de resta con un numero negativo en la entrada
    Dado los numeros enteros 10 y -2
    Cuando intento realizar la resta
    Entonces se lanza una excepcion de "Ambos numeros deben ser enteros no negativos"

