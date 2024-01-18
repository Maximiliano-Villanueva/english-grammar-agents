# Standard imports
import logging
import os

# Third-party imports
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

# Internal imports
from application.agents.writting.routes import writting_routes
from application.agents.summary.routes import summary_routes

dotenv_file = os.path.join(os.getcwd(), "envs", f"{os.getenv('BUILD', 'debug')}.env")
dotenv_loaded = load_dotenv(dotenv_file)

# Initialize FastAPI app
app = FastAPI()

# Include Routers
app.include_router(writting_routes)
app.include_router(summary_routes)


def main():

    host = os.environ.get("FASTAPI_HOST", "localhost")
    port = int(os.environ.get("FASTAPI_PORT", "8000"))
    
    logging.info(f"Starting server at http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()