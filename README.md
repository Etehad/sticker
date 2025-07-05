Telegram Sticker to JPG Converter
A public web service to convert Telegram sticker URLs to JPG image links using FastAPI.
Setup

Deploy the app on Render.
Push the code to a GitHub repository.

Deployment on Render

Create a new Web Service on Render.
Connect your GitHub repository.
Deploy the service with Python runtime.

Usage
Send a POST request to /convert with a JSON body containing the sticker file URL:
{
  "sticker_url": "https://api.telegram.org/file/bot<token>/<file_path>"
}

Response:
{
  "jpg_url": "https://your-render-service.onrender.com/tmp/<file_id>.jpg"
}

Notes

The service assumes the provided URL is publicly accessible or accessible by the server.
For production, consider using a cloud storage service like AWS S3 for persistent file storage.
