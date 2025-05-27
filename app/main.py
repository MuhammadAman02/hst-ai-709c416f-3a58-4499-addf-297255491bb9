from fastapi import FastAPI
import uvicorn

# Create a FastAPI app instance
app = FastAPI(
    title="My FastAPI Application",
    description="This is a simple FastAPI application.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health", tags=["Health Check"])
async def health_check():
    """
    Health check endpoint to verify the application is running.
    """
    return {"status": "healthy"}

# The application is run via the main.py in the project root (project_base/main.py)
# which imports this 'app' instance.