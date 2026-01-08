import json
from fastapi import FastAPI

with open("errores_http.json", "r", encoding="utf-8") as f:
    errores = json.load(f)

api = FastAPI(
    title="API Errores HTTP",
    version="1.0.0",
    description="API para consultar la definición de los errores http"
)

@api.get('/api/error-http/{codigo}', response_model=dict, tags=["Leer definición"])
def obtener_definicion(codigo: str):
    return { codigo: errores.get(codigo) }