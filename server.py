from fastapi import FastAPI
from auth import login
from pydantic import BaseModel
from database import *
app=FastAPI()

class getinput(BaseModel):
    log_id: str
    pwd: str

class CreateAccountRequest(BaseModel):
    token: str
    details: dict

class SearchAccount(BaseModel):
    token: str
    acn:int

@app.post("/login/customer")
def cust_login(cust_det: getinput):
    token = login("customer",cust_det.log_id,cust_det.pwd)
    return {"access_token":token}

@app.post("/login/admin")
def admin_login(admin_det: getinput):
    token = login("admin",admin_det.log_id,admin_det.pwd)
    return {"access_token":token}

@app.post("/create_account")
def define_account(payload: CreateAccountRequest):
    token = payload.token
    details = payload.details
    return {"account_number": storeCustomer(details)} 

@app.post("/search_customer")
def search(payload: SearchAccount):
    token=payload.token
    acn=payload.acn
    return {"accounts":searchCustomer(acn)}
