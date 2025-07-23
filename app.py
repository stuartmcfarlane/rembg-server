from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import base64

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

file_path = '../faces/MDgyNTQ5LmpwZw.jpg'

@app.post("/process")
async def process():
    print(">process")
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    json_response = jsonable_encoder({
        'filename': 'foreground.jpg',
        'image': encoded_string
    })
    print("<process", json_response)
    return JSONResponse(json_response)
