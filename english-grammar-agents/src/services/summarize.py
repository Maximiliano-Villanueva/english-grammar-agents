
# Standard imports
import logging
import os

from typing import Optional

# Internal imports
from common.entities.strategy import StrategySummarize

from modules.agents.summarizer import Summarizer


def summarize(message: str,
              strategy: Optional[StrategySummarize] = StrategySummarize.MAP_REDUCE) -> str:
    """ Implementation of the business logic for the writte properly case. """

    logging.info("Start process writte properly.")
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("OPENAI_MODEL_NAME")

    agent = Summarizer(api_key=api_key, model_name=model_name)
    result = agent.run(message=message,
                       strategy=strategy)

    logging.info("End process writte properly.")
    return result

