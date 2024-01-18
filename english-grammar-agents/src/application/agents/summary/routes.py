"""
This script defines the endpoints for summarizing cases
"""
# Standard imports
import logging

# Third-party imports
from fastapi import APIRouter, HTTPException, status
from application.validator.message_validation import validate_input_message

# Internal imports
from common.entities.api.response import Response
from common.entities.api.message import Message

from services.summarize import summarize


summary_routes = APIRouter(
    prefix="/summary",
    tags=["summary"],
)


@summary_routes.post("", response_model=Response)
async def writting(message: Message) -> Response:
    """
    This endpoint provides acces to summarizing agent.
    """
    try:
        logging.info("Entering summary endpoint")
        if not validate_input_message(message=message):
            logging.error("Input message invalid")
            raise ValueError()
        result = summarize(message=message.data)
        logging.info("Leaving summary endpoint")
        return Response(message=result)
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message cannot be empty"
        )
    except Exception as e:
        logging.error(f"Exception: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )