from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.validator import restar


class RestaRequest(BaseModel):
    numero_a: int
    numero_b: int


class RestaResponse(BaseModel):
    resultado: int


app = FastAPI(title="Base Converter Service")


@app.post("/resta", response_model=RestaResponse)
async def resta(req: RestaRequest):
    try:
        resultado = restar(
            req.numero_a,
            req.numero_b
        )
        return RestaResponse(resultado=resultado)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
