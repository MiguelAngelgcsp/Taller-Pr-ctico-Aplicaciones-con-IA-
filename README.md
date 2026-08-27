# Taller: Desarrollo de Aplicaciones con IA — API de Gemini

Script en Python que usa la librería `google-genai` para realizar peticiones,
procesar textos y gestionar un chat con roles definidos.

## Requisitos previos

- Python 3.9 o superior.
- Una API key de Gemini, obtenida en [Google AI Studio](https://aistudio.google.com/apikey).

## Instalación

1. Clona este repositorio y entra a la carpeta:
   ```bash
   git clone <url-del-repositorio>
   cd <carpeta-del-repositorio>
   ```

2. (Recomendado) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu API key como variable de entorno:
   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY="tu_api_key_aqui"

   # Linux / macOS
   export GEMINI_API_KEY="tu_api_key_aqui"
   ```
   También puedes copiar `.env.example` a `.env` y cargarla con una librería
   como `python-dotenv` si lo prefieres.

## Ejecución de cada ejercicio

### Ejercicio 1 — Conexión y Petición Básica
```bash
python ejercicio1_conexion_basica.py
```
Inicializa el cliente y pide al modelo que explique la "Inferencia en IA"
en menos de 50 palabras. La respuesta se imprime en consola.

### Ejercicio 2 — Procesador de Textos Inteligente
```bash
python ejercicio2_procesador_textos.py
```
Ejecuta la función `procesar_articulo(texto, tarea)` sobre un artículo de
ejemplo incluido en el script, mostrando primero el resumen ejecutivo
(`tarea="resumir"`) y luego la versión formal (`tarea="profesionalizar"`).
Para usarla con tu propio texto, impórtala en otro script o modifica la
variable `articulo_ejemplo` dentro del archivo.

### Ejercicio 3 — Chat de Soporte con Historial (Few-Shot)
```bash
python ejercicio3_chat_soporte.py
```
Abre un chat interactivo en consola. El modelo ya conoce dos ejemplos
previos de preguntas sobre productos (few-shot) y responde como un
vendedor amable. Escribe tus preguntas y presiona Enter; escribe
`finalizar` para terminar la conversación.

##  Evidencias de ejecución

Las capturas de pantalla con la ejecución y salida de cada ejercicio se
encuentran en la carpeta `evidencias/` (agregar al subir a GitHub).

##  Estructura del repositorio

```
.
├── ejercicio1_conexion_basica.py
├── ejercicio2_procesador_textos.py
├── ejercicio3_chat_soporte.py
├── requirements.txt
├── .env.example
├── README.md
└── evidencias/
    ├── ejercicio1.png
    ├── ejercicio2.png
    └── ejercicio3.png
```
