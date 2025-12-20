from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return 1 / 0


@app.get("/hello")
def hello():
    return {"message": "Hello from Kubernetes DevOps Platform and updated to version 25.0.0."}

