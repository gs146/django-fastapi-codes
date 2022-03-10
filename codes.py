import fastapi

# installing fastapi
pip install fastapi
pip install uvicorn

#starter code:BASIC
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello Aliens!!"}

#DOCUMENTATION
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello Aliens!!"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# There are two ways to open documentation:
# 1]. go to http://127.0.0.1:8000/docs.
# 2]. or go to: http://127.0.0.1:8000/redoc