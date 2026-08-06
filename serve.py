import os

from dotenv import load_dotenv
from waitress import serve

from app import app

load_dotenv()

serve(
    app,
    host=os.getenv("HOST", "0.0.0.0"),
    port=int(os.getenv("PORT", 5000))
)