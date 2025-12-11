from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "service": "k8s-devops-platform-backend",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "dev")
    }

@app.get("/hello")
def hello():
    return {"message": "Hello from Kubernetes DevOps Platform"}

