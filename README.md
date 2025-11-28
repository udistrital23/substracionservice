# Base Converter Service - Endpoint de Resta

Este proyecto implementa un servicio sencillo usando **FastAPI** que expone un endpoint para realizar una operación de resta entre dos números enteros. El objetivo es mostrar una estructura básica de API utilizando modelos Pydantic, manejo de errores y arquitectura modular.

---

## 🚀 Tecnologías utilizadas

* **FastAPI**: Framework moderno y rápido para construir APIs.
* **Pydantic**: Validación de datos mediante modelos.
* **Python 3.11** o superior.

---

## 📂 Estructura del proyecto

```
app/
├── main.py        # Archivo principal con la API y el endpoint
├── validator.py   # Contiene la función `restar` usada por el endpoint
```

---

## 📌 Descripción del endpoint

### `POST /resta`

Realiza la resta entre dos números enteros.

#### **Request Body**

```json
{
  "numero_a": 10,
  "numero_b": 3
}
```

#### **Response**

```json
{
  "resultado": 7
}
```

#### **Modelos utilizados**

| Modelo          | Campos                           | Descripción               |
| --------------- | -------------------------------- | ------------------------- |
| `RestaRequest`  | `numero_a: int`, `numero_b: int` | Entrada para la operación |
| `RestaResponse` | `resultado: int`                 | Salida con el resultado   |

#### **Errores posibles**

Retorna:

* **400 Bad Request** si la función `restar` lanza un `ValueError`.

---

## 🧠 Funcionamiento interno

El endpoint ejecuta la función `restar(numero_a, numero_b)` definida en `validator.py`. Si ocurre una excepción del tipo `ValueError`, la API responde con un error HTTP 400.

---

## ▶️ Cómo ejecutar el proyecto

1. Instala dependencias:

   ```bash
   pip install fastapi uvicorn
   ```

2. Ejecuta el servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Accede a la documentación interactiva:

   * Swagger UI: `http://localhost:8000/docs`
   * ReDoc: `http://localhost:8000/redoc`

---

## 🧪 Prueba rápida con curl

```bash
curl -X POST "http://localhost:8000/resta" \
     -H "Content-Type: application/json" \
     -d '{"numero_a": 20, "numero_b": 5}'
```

---

## 📄 Licencia

Este código es de uso libre para fines educativos o de integración básica con FastAPI.
