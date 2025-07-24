from typing import Annotated
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.encoders import jsonable_encoder
import base64
from rembg import remove
import os

app = FastAPI()

UPLOAD_DIR = r"./data"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/file")
async def process_file(file: Annotated[bytes, File()]):
    print(">file", len(file))

    input_filename = 'input'
    input_path = os.path.join(UPLOAD_DIR, input_filename)
    output_filename = input_filename + '.png'
    output_path = os.path.join(UPLOAD_DIR, output_filename)

    with open(input_path, "wb") as f:
        f.write(file)

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)

    print("<file")
    return FileResponse(output_path, media_type='image/png')
