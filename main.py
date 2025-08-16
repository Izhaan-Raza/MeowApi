from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get("/blog")
def index(limit=10,published:bool=True, sort:Optional[str]=None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} unpublished blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {id : {"1","2"}} }


@app.post("/blog")
def create_blog(req: Blog):
    return {"data":f"BLog created meow with {req.title} and {req.body}"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
