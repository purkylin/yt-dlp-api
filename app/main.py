from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

import yt_dlp
import secrets
import os

app = FastAPI()

api_key_header = APIKeyHeader(name="AUTH", auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    if not api_key_header:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    correct_token = os.getenv("AUTH_TOKEN", "secret")
    if not secrets.compare_digest(api_key_header, correct_token):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return api_key_header

class DownloadRequest(BaseModel):
    url: str

    def get_config(self):
        return {
            'noplaylist': True,
        }

@app.get("/status")
def health_check():
    return {'status': 'ok'}

@app.get("/", dependencies=[Depends(get_api_key)])
async def parse_video_info(url: str):
    try:
        ydl_opts = {
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))