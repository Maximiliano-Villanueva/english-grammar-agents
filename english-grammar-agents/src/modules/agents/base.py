"""
This script defines the abstract classes / interfaces to be implemented by agents.
"""
# Standard imports
from abc import ABC, abstractmethod

# Internal imports
from common.entities.strategy import Strategy
from common.entities.template_type import PromptTemplate
from common.entities.writting import WrittingFixType


class AgentOpenAi(ABC):

    def __init__(self, api_key: str, model_name: str):
        """
        Initialize the English Improvement Agent with OpenAI API key.

        Args:
            api_key (str): OpenAI API key.
            model_name (str): OpenAI model name.
        """
        self.api_key = api_key
        self.model_name = model_name

    def _get_template(self, strategy: Strategy,
                      writting_fix_type: WrittingFixType,
                      template_type: PromptTemplate) -> str:
        """
        Get the right template given an strategy, writting_fix_type and template_type
        Args:
            strategy (Strategy): Strategy to use.
            writting_fix_type (WrittingFixType): type of writting.
            template_type (PromptTemplate): type of template.
        Returns:
            Template (str)
        Raises:
            TemplateNotFound: template could not be found.
        """
        pass

    @abstractmethod
    def run(self, message: str, **kwargs) -> str:
        """
        Enhances both grammar and style of the input message.

        Args:
            message (str): The input message.
        Returns:
            str: Enhanced message.
        """
