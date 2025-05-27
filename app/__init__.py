# This file makes the 'app' directory a Python package.
# It imports the FastAPI application instance from app.main
# so that it can be imported by project_base/main.py as 'from app import app'.

from .main import app

# You can add package-level initializations here if needed in the future.
# For now, simply exposing the 'app' from .main is sufficient.