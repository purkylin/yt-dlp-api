from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

class DownloadRequest(BaseModel):
    url: str

    def get_config(self):
        return {
            'noplaylist': True,
        }

@app.get("/status")
def status():
    return {'status': 'ok'}

@app.post("/info")
async def parse_video_info(request: DownloadRequest):
    try:
        ydl_opts = request.get_config()
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=False)
            return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
