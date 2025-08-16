from fastapi import FastAPI
import schemas

app=FastAPI()



@app.post("/blog")
def create(req:schemas.Blog):
    return req
