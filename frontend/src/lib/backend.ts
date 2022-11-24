import { VITE_BACKEND_URL } from "$env/static/private"

export async function mathTransform(
    image: File, 
    latex: string,
    autoMinMax: boolean,
    heatmapOut: boolean
): Promise<{
    img_b64: string,
    legend: object | null
}> {
    const b64 = "abc"

    const resp = await fetch(`${VITE_BACKEND_URL}/math-transform`, {
        method: "POST",
        body: {
            img: b64,
            latex: latex,
            autominmax: autoMinMax,
            heatmap_out: false
        }
    })
    const data = resp.json()
}

export async function ()
