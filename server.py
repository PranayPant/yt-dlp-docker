from fastapi import FastAPI
from urllib.parse import unquote

from task import download_subs

app = FastAPI()

@app.get("/sub/")
def write_subs(url: str, filename: str = None):
    # Execute your Python script here
    file_contents = download_subs(url, filename) 
    return file_contents