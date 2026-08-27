"""
Ejercicio 2: Procesador de Textos Inteligente.

Define procesar_articulo(texto, tarea), que usa una system_instruction
fija ("Editor Editorial de prestigio") y cambia el comportamiento según
la tarea solicitada: "resumir" o "profesionalizar".
"""

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("GEMINI_API_KEY"):
    raise EnvironmentError(
        "No se encontró la variable de entorno GEMINI_API_KEY. "
        "Defínela antes de ejecutar el script (ver README.md)."
    )

MODELO = "gemini-2.5-flash"

# Instrucción de sistema fija: define el rol/persona de la IA.
SYSTEM_INSTRUCTION = (
    "Eres un Editor Editorial de prestigio, con décadas de experiencia "
    "en publicaciones técnicas y de negocios. Tu trabajo es intervenir "
    "textos con precisión, claridad y un tono profesional impecable."
)

# Instrucciones puntuales por tipo de tarea.
INSTRUCCIONES_POR_TAREA = {
    "resumir": (
        "Genera un resumen ejecutivo del siguiente texto. Debe ser breve, "
        "capturar las ideas clave y estar redactado en un máximo de 5 líneas."
    ),
    "profesionalizar": (
        "Reescribe el siguiente texto para que suene formal, técnico y "
        "profesional, conservando el significado original."
    ),
}


def procesar_articulo(texto: str, tarea: str) -> str:
    """
    Procesa un texto largo según la tarea indicada.

    Args:
        texto: Texto de entrada a procesar.
        tarea: "resumir" o "profesionalizar".

    Returns:
        El texto procesado por el modelo.

    Raises:
        ValueError: si la tarea no es una de las soportadas.
    """
    if tarea not in INSTRUCCIONES_POR_TAREA:
        raise ValueError(
            f"Tarea '{tarea}' no soportada. Usa 'resumir' o 'profesionalizar'."
        )

    cliente = genai.Client()

    prompt = f"{INSTRUCCIONES_POR_TAREA[tarea]}\n\nTexto:\n{texto}"

    respuesta = cliente.models.generate_content(
        model=MODELO,
        contents=prompt,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
    )

    return respuesta.text


if __name__ == "__main__":
    articulo_ejemplo = (
        "La empresa lanzó su nuevo producto la semana pasada y la verdad "
        "es que a la gente le encantó un montón. Las ventas subieron bastante "
        "rápido y el equipo de marketing está feliz porque todo salió mejor "
        "de lo que pensaban. Ahora quieren repetir la estrategia en otros "
        "países porque creen que puede funcionar igual de bien."
    )

    print("=== Resumen ejecutivo ===")
    print(procesar_articulo(articulo_ejemplo, "resumir"))

    print("\n=== Versión profesionalizada ===")
    print(procesar_articulo(articulo_ejemplo, "profesionalizar"))
