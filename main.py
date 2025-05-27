import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the FastAPI app instance from the 'app' package.
# The 'app' package's __init__.py imports 'app' from 'app.main'.
from app import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    # Set reload=True for development to auto-reload on code changes.
    # For production, set reload=False or remove the reload parameter.
    uvicorn.run(app, host=host, port=port, reload=True)