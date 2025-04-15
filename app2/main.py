import os
import time
import requests
import threading
from fastapi import FastAPI

app = FastAPI()

APP1_URL = os.getenv("APP1_URL", "http://app1:8000")

def poll_app1():
    while True:
        try:
            response = requests.get(APP1_URL)
            print(f"App2 -> App1 response: {response.status_code} | {response.text}")
        except Exception as e:
            print(f"Failed to reach App1: {e}")
        time.sleep(10)

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=poll_app1, daemon=True)
    thread.start()

@app.get("/ping")
def ping():
    return {"message": "App2 is running"}
