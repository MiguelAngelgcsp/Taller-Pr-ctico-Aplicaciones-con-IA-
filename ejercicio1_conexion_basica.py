"""
Ejercicio 1: Conexión y Petición Básica.

Inicializa el cliente de Gemini y realiza una consulta simple pidiendo
una explicación de "Inferencia en IA" en menos de 50 palabras.
"""

import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()


# El cliente toma la API key automáticamente de la variable de entorno
# GEMINI_API_KEY. Validamos que exista antes de continuar.
if not os.environ.get("GEMINI_API_KEY"):
    raise EnvironmentError(
        "No se encontró la variable de entorno GEMINI_API_KEY. "
        "Defínela antes de ejecutar el script (ver README.md)."
    )

MODELO = "gemini-2.5-flash"


def main() -> None:
    """Realiza una petición simple al modelo y muestra la respuesta."""
    cliente = genai.Client()

    pregunta = "Explica en menos de 50 palabras qué es la 'Inferencia en IA'."

    respuesta = cliente.models.generate_content(
        model=MODELO,
        contents=pregunta,
        # Limitamos la longitud para reforzar la restricción de 50 palabras.
        config=types.GenerateContentConfig(max_output_tokens=120),
    )

    print("Pregunta:", pregunta)
    print("\nRespuesta del modelo:\n")
    print(respuesta.text)


if __name__ == "__main__":
    main()
