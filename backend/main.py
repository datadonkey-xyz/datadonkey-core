from fastapi import FastAPI, Request
from os import getenv
import cv2 as cv
from tools import math_transform
import base64
import numpy as np

app = FastAPI(
    openapi_url="/resources/openapi.json",
    docs_url="/resources/docs"
) if getenv("ENV") == 'dev' else FastAPI()

# Image endpoints

@app.post("/image/math-transform")
async def math_image_transform_grayscale(
    req: Request
):

    image_b64: str = req.body['image_b64']
    latex: str = req.body['latex']
    autominmax: bool = req.body['autominmax']
    heatmap_out: bool = req.body['heatmap_out']

    img = cv.imdecode(image_b64)

    transformed = img.copy()

    func = math_transform.transform_func_from_latex(
        latex,
        ["R", "G", "B", "A"]
    )

    alpha_on = len(img[0][0]) == 4

    for i in range(len(img)):
        for j in range(len(img[i])):
            pix = img[i][j]
            transformed[i][j] = func(
                pix[2],
                pix[1],
                pix[0],
                255 if alpha_on else pix[3]
            )

    transformed_b64 = base64.b64encode(
        cv.imencode('.png', transformed)[1]
    ).decode(encoding='utf-8')

    return {
        "img_b64": transformed_b64,
        "legend": None
    }

@app.post("/image/smooth-conv")
async def convolutional_smooth(
    image_b64: str,
    smoothing_radius: int
):
    img = cv.imdecode(image_b64)

    # build & apply smoothing conv kernel
    k = []
    for i in range(smoothing_radius):
        k.append([1/(smoothing_radius**2) for i in range(smoothing_radius)])
    kernel = np.array(k)

    transformed = cv.filter2D(img, -1, kernel)

    transformed_b64 = base64.b64encode(
        cv.imencode('.png', transformed)[1]
    ).decode(encoding='utf-8')

    return transformed_b64


@app.post("/image/heatmap")
async def intensity_heatmap(
    image_b64: str,
    smoothing_radius: int
):
    img = cv.imdecode(image_b64)

    transformed = cv.applyColorMap(img, cv.COLORMAP_JET)

    transformed_b64 = base64.b64encode(
        cv.imencode('.png', transformed)[1]
    ).decode(encoding='utf-8')

    return transformed_b64
