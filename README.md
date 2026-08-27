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
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu API key como variable de entorno:
   También puedes copiar `.env` y cargarla con una librería
   como `python-dotenv`,así mismo debes importar la librería de google-genai.

   ## Comando de importación de librerias
     pip install google-genai python-dotenv

   ## inicia el entorno
      Se debe crear la carpeta venv con el comando python -m venv venv
      Inicializar la carpeta con: .\venv\Scripts\activate 

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

#Ejecución Ejercicio 1
<img width="1600" height="863" alt="image" src="https://github.com/user-attachments/assets/bf32517c-e6a4-4d37-9797-ce8f1135e78b" />

#Ejecución Ejercicio 2
<img width="1600" height="872" alt="image" src="https://github.com/user-attachments/assets/03a273c7-001c-4032-91d4-8b8c0c02e1f8" />

#Ejecución Ejercicio 3
<img width="1600" height="873" alt="image" src="https://github.com/user-attachments/assets/2cbd8504-a4dc-465f-9832-aa6bdd7a38d1" />


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
