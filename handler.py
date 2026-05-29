import runpod
import requests
from rembg import remove
from PIL import Image
import base64
from io import BytesIO

def handler(job):
    try:
        image_url = job["input"]["image_url"]
        img_bytes = requests.get(image_url, timeout=30).content
        img = Image.open(BytesIO(img_bytes)).convert("RGBA")
        result = remove(img)
        buffer = BytesIO()
        result.save(buffer, format="PNG")
        return {
            "image_base64": base64.b64encode(buffer.getvalue()).decode()
        }
    except Exception as e:
        return { "error": str(e) }
        

runpod.serverless.start({ "handler": handler })
