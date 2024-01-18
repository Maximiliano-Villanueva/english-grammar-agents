"""
This script defines the endpoints for writting cases
"""
# Standard imports
from typing import Any
import logging

# Third-party imports
from fastapi import APIRouter, HTTPException, status
from application.validator.message_validation import validate_input_message

# Internal imports
from common.entities.api.response import Response
from common.entities.api.message import Message
from modules.cleaner.sanitizer import sanitize_input_prompt_injection

from services.writting import writte_properly, writte_grammar_only


writting_routes = APIRouter(
    prefix="/writting",
    tags=["writting"],
)


@writting_routes.post("", response_model=Response)
async def writting(message: Message) -> Response:
    """
    This endpoint provides acces to enhancing writting properly.
    """
    try:
        logging.info("Entering writte properly endpoint")
        if not validate_input_message(message=message):
            logging.error("Input message invalid")
            raise ValueError()
        message.data = sanitize_input_prompt_injection(message.data)
        result = writte_properly(message=message.data)
        logging.info("Leaving writte properly endpoint")
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


@writting_routes.post("/grammar", response_model=Response)
async def writting_grammar(message: Message) -> Response:
    """
    This endpoint provides acces to enhancing only grammar.
    """
    try:
        logging.info("Entering writte grammar endpoint")
        if not validate_input_message(message=message):
            logging.error("Input message invalid")
            raise ValueError()
        message.data = sanitize_input_prompt_injection(message.data)
        result = writte_grammar_only(message=message.data)
        logging.info("Leaving writte grammar endpoint")
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

