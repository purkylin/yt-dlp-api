# yt-dlp-api

A simple FastAPI service that provides a wrapper around [yt-dlp](https://github.com/yt-dlp/yt-dlp) to extract video information.

## Features

- **Video Info Extraction**: Retrieve metadata for videos supported by yt-dlp.
- **Authentication**: Secured endpoints using API Key header.
- **Docker Support**: Ready for containerized deployment.

## Authentication

This service is protected by API Key authentication for the main endpoints.

- **Header Name**: `AUTH`
- **Default Token**: `secret` (or `HAWK` if using the provided Dockerfile defaults)
- **Environment Variable**: `AUTH_TOKEN`

## Endpoints

### 1. Health Check
- **URL**: `/status`
- **Method**: `GET`
- **Auth Required**: No
- **Response**: `{'status': 'ok'}`

### 2. Get Video Info
- **URL**: `/info`
- **Method**: `POST`
- **Auth Required**: Yes
- **Headers**:
  - `AUTH`: <your-token>
- **Body**:
  ```json
  {
      "url": "https://www.youtube.com/watch?v=..."
  }
  ```
- **Response**: JSON object containing video metadata.

## Running Locally

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start Server**:
    ```bash
    fastapi dev app/main.py
    # OR
    uvicorn app.main:app --reload
    ```

3.  **Run with Custom Token**:
    ```bash
    export AUTH_TOKEN=mysecurekey
    fastapi dev app/main.py
    ```

## Docker

1.  **Build Image**:
    ```bash
    docker build -t yt-dlp-api .
    ```

2.  **Run Container**:
    ```bash
    # Runs with default token set in Dockerfile (HAWK)
    docker run -d -p 8000:80 yt-dlp-api
    ```

3.  **Run with Custom Token**:
    ```bash
    docker run -d -p 8000:80 -e AUTH_TOKEN=supersecret yt-dlp-api
    ```
