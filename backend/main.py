
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from lib.persistence import add_calculation, fetch_calculations
from lib.rpn_calculator import rpn_calculator
from lib.utils import calculations_as_csv_response

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputExpression(BaseModel):
    expression: str

class OutputExpression(BaseModel):
    result: str

class ErrorExpression(BaseModel):
    error: str

@app.post("/process")
def process(input_object: InputExpression) -> OutputExpression:

    try:
        dec_result = rpn_calculator(input_object.expression)
        str_result = str(dec_result)

        add_calculation(input_object.expression, str_result)

        return OutputExpression(result=str_result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/calculations")
def get_calculations():

    calculations = fetch_calculations()

    return calculations_as_csv_response(calculations)
