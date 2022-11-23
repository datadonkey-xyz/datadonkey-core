from fastapi import FastAPI
from os import getenv
import cv2 as cv
from tools import math_transform

app = FastAPI(
    openapi_url="/resources/openapi.json",
    docs_url="/resources/docs"
) if getenv("ENV") == 'dev' else FastAPI()

@app.post("/image/math-transform")
def math_image_transform_grayscale(image_b64: str, latex: str):
    img = cv.imdecode(image_b64)

    transformed = img.copy()
    func = math_transform.generate_func(latex)

    for i in range(len(img)):
        for j in range(len(img[i])):
            transformed[i][j] = func(inputs)

    return {
        "transformed_b64": transformed
    }
