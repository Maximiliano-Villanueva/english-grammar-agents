
# Standard imports
import json
import logging
import os

from json.decoder import JSONDecodeError
from typing import Optional

# Internal imports
from common.entities.strategy import Strategy
from common.entities.writting import WrittingFixType
from common.exceptions.services_exceptions import JsonException

from modules.agents.writting_improvement_agent import WrittingImprovementAgent


def writte_properly(message: str,
                    strategy: Optional[Strategy] = Strategy.ZERO_SHOT) -> str:
    """ Implementation of the business logic for the writte properly case. """

    logging.info("Start process writte properly.")
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL_NAME")

    agent = WrittingImprovementAgent(api_key=api_key, model_name=model_name)
    result = agent.run(message=message,
                       strategy=strategy,
                       writting_fix_type=WrittingFixType.WRITE_PROPERLY)

    logging.info("End process writte properly.")
    return result


def writte_grammar_only(message: str,
                        strategy: Optional[Strategy] = Strategy.ZERO_SHOT) -> str:
    """ Implementation of the business logic for the writte grammar only case. """

    logging.info("Start process writte only grammar.")
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL_NAME")
    
    agent = WrittingImprovementAgent(api_key=api_key, model_name=model_name)
    errors = agent.run(message=message,
                       strategy=strategy,
                       writting_fix_type=WrittingFixType.WRITE_SAME_GRAMMAR_FIXED
                       )

    try:
        errors = json.loads(errors)
        result = ""
        for error in errors:
            if "type of error" in error and error["type of error"] == "grammar":
                result += error["correct"]
            else:
                result += error["original"]
        
        logging.info("End process writte only grammar.")
        return result
            
    except (JSONDecodeError, TypeError) as e:
        logging.error(e)
        raise JsonException
    except Exception as e:
        logging.exception(e)
        raise
