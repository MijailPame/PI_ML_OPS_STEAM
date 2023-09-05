from typing import Union
from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

Juegos = None
UserItems = None
Review = None

@app.on_event("startup")
async def startup_event():
    global UserItems
    UserItems = pd.read_csv("ETL_UserItems.csv")
    global Juegos
    Juegos = pd.read_csv("ETL_DataSteam.csv")
    global Review
    Review = pd.read_csv("ETL_UserReview.csv")

@app.get("/")
def read_root():
    return {"mensaje": "Proyecto Individual de Mijail Pauro Meléndez"}

@app.get("/user/{user_id}")
async def userdata(user_id: str):
    if UserItems is None:
        return {"error": "Data no cargado"}
    
    user_data = UserItems[UserItems['user_id'] == user_id]

    if user_data.empty:
        return {"error": "Usuario no encontrado"}
    
    cantidad = user_data.iloc[0]['items_count'].item()

    return {"cantidad": cantidad}

