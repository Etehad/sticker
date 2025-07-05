from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiohttp
from PIL import Image
import io
import os
from fastapi.responses import JSONResponse
import uuid

app = FastAPI()

class StickerRequest(BaseModel):
    sticker_url: str

async def download_file(file_url: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status != 200:
                raise HTTPException(status_code=400, detail="Failed to download sticker")
            return await response.read()

@app.post("/convert")
async def convert_sticker_to_jpg(request: StickerRequest):
    try:
        # دانلود فایل استیکر از URL ارائه‌شده
        file_bytes = await download_file(request.sticker_url)
        
        # تبدیل به JPG
        image = Image.open(io.BytesIO(file_bytes))
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        output = io.BytesIO()
        image.save(output, format="JPEG")
        jpg_bytes = output.getvalue()
        
        # ذخیره موقت فایل JPG
        file_id = str(uuid.uuid4())
        temp_file_path = f"/tmp/{file_id}.jpg"
        with open(temp_file_path, "wb") as f:
            f.write(jpg_bytes)
        
        # لینک موقت به فایل JPG (برای تولید واقعی، از S3 یا مشابه استفاده کنید)
        jpg_url = f"https://sticker-74no.onrender.com/tmp/{file_id}.jpg"
        
        return JSONResponse(content={"jpg_url": jpg_url})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing sticker: {str(e)}")
