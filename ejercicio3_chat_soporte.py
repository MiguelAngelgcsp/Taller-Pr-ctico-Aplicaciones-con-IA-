"""
Ejercicio 3: Chat de Soporte con Historial (Few-Shot).

Simula el chat de soporte de una tienda de tecnología. La IA actúa como
vendedor amable (system_instruction) y arranca con un historial few-shot
de dos ejemplos pregunta-respuesta sobre productos. El bucle continúa
hasta que el usuario escribe "finalizar".
"""

import os
from google import genai
from google.genai import types
from google.genai.types import UserContent, ModelContent

if not os.environ.get("GEMINI_API_KEY"):
    raise EnvironmentError(
        "No se encontró la variable de entorno GEMINI_API_KEY. "
        "Defínela antes de ejecutar el script (ver README.md)."
    )

MODELO = "gemini-2.5-flash"

# Rol del vendedor: tono amable, cercano y orientado a ayudar al cliente.
SYSTEM_INSTRUCTION = (
    "Eres un vendedor amable y entusiasta de una tienda de tecnología. "
    "Respondes de forma cercana, clara y honesta, resaltando las "
    "especificaciones relevantes de los productos y ayudando al cliente "
    "a decidir según sus necesidades."
)

# Historial few-shot: ejemplos de interacción previa que guían el estilo
# y el tipo de respuesta esperada (especificaciones concretas).
HISTORIAL_FEW_SHOT = [
    UserContent(parts=[types.Part(text="¿Qué especificaciones tiene el portátil Aurora X14?")]),
    ModelContent(parts=[types.Part(
        text=(
            "¡Buena elección para preguntar! El Aurora X14 trae procesador "
            "Intel Core i7 de última generación, 16 GB de RAM, "
            "almacenamiento SSD de 512 GB y pantalla de 14 pulgadas Full HD. "
            "Es ideal si buscas portabilidad sin sacrificar rendimiento."
        )
    )]),
    UserContent(parts=[types.Part(text="¿Y el mouse inalámbrico Nébula M2 sirve para diseño gráfico?")]),
    ModelContent(parts=[types.Part(
        text=(
            "¡Claro que sí! El Nébula M2 tiene sensor óptico de 4000 DPI "
            "ajustable, conexión dual (Bluetooth y USB receptor), batería "
            "de hasta 3 meses de duración y botones programables, lo que "
            "lo hace muy cómodo para trabajo de precisión como diseño gráfico."
        )
    )]),
]


def iniciar_chat_soporte() -> None:
    """Inicia el bucle de chat de soporte hasta que el usuario escriba 'finalizar'."""
    cliente = genai.Client()

    chat = cliente.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION),
        history=HISTORIAL_FEW_SHOT,
    )

    print("=== Chat de Soporte - Tienda de Tecnología ===")
    print("Escribe tu pregunta sobre algún producto. Escribe 'finalizar' para salir.\n")

    while True:
        mensaje_usuario = input("Tú: ").strip()

        if mensaje_usuario.lower() == "finalizar":
            print("Vendedor: ¡Gracias por tu visita! Que tengas un excelente día.")
            break

        if not mensaje_usuario:
            continue

        respuesta = chat.send_message(mensaje_usuario)
        print(f"Vendedor: {respuesta.text}\n")


if __name__ == "__main__":
    iniciar_chat_soporte()
