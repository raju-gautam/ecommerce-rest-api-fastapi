from fastapi import FastAPI
app=FastAPI()
@app.get("/home")
def add():
    return "hello world"




