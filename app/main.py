#importacion de librerias necesarias
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

#cargar variables de entorno desde .env
load_dotenv()

#instrancia de la clase FastAPI
app = FastAPI()


#clase pregunta para el manejo de la solicitud de los usuarios
class Pregunta (BaseModel):
    texto: str

# Manejo global de errores HTTP
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

# Manejo global de errores generales
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": f"Ocurrió un error inesperado: {str(exc)}"}
    )

#endpoint de saludo inicial
@app.get("/inicio")
def inicio():
    return {"Bienvenido ":"Gracias por usar esta API, mas informacion en README.md"}

#endpoint para recibir preguntas y devolver la respuesta
@app.post("/preguntar")
async def preguntar(pregunta: Pregunta):
    #variables para la conexion al modelo de IA
    url = os.getenv("OLLAMA_URL")
    model = os.getenv("OLLAMA_MODEL")

    #validar que existan las variables
    if not url or not model:
        raise HTTPException(status_code=500, detail="Variables de entorno no definidas")

    # Configuración de la solicitud a Ollama
    payload = {
        "model": model,  #modelo descargado en Ollama
        "prompt": pregunta.texto,
        "stream": False  #repuestas en tiempo real
    }
    #en response se ejecuta y guarda la respuesta
    response = requests.post(url, json=payload)

    #respuesta de ollama
    print("Respuesta de Ollama:", response.status_code, response.text)

    # Si la respuesta es 200 OK, procesamos la respuesta
    if response.status_code == 200:
        resultado = response.json()
        return {"respuesta": resultado.get("response", "No se obtuvo respuesta del modelo")}
        
    raise HTTPException(
        status_code=500,
        detail=f"Error al consultar el modelo de IA: {response.status_code} - {response.text}"
    )