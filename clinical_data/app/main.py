"""Endpoints FastAPI"""

import logging
from fastapi import FastAPI, HTTPException
from app.schemas import EvolucaoMedica, Anamnese, Receituario
from app.rabbitmq import publish_message

app = FastAPI()

@app.post("/evolucao/")
async def create_evolucao(evolucao: EvolucaoMedica):
    try:
        publish_message("evolucoes_queue", evolucao.model_dump(mode="json"))
        return {"message": "Evolução médica enviada com sucesso."}
    except Exception as e:
        logging.exception(e)
        raise e

@app.post("/anamnese/")
async def create_anamnese(anamnese: Anamnese):
    try:
        publish_message("anamneses_queue", anamnese.model_dump(mode="json"))
        return {"message": "Anamnese enviada com sucesso."}
    except Exception as e:
        logging.exception(e)
        raise e

@app.post("/receituario/")
async def create_receituario(receituario: Receituario):
    try:
        publish_message("receituarios_queue", receituario.model_dump(mode="json"))
        return {"message": "Receituário enviado com sucesso."}
    except Exception as e:
        logging.exception(e)
        raise e
