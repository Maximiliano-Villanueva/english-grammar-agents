# Standard Imports
import logging
from typing import Optional

# Third Party Imports
from langchain.chat_models.openai import ChatOpenAI
# from langchain_community.llms.openai import OpenAI


from langchain.chains import ConversationChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.memory import ReadOnlySharedMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Internal imports
from common.entities.strategy import Strategy
from common.entities.template_type import PromptTemplate
from common.entities.writting import WrittingFixType
from modules.agents.base import AgentOpenAi
from common.exceptions.template_exceptions import TemplateNotFound
from modules.prompts import writte_properly, same_grammar_fix

# Initialize Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WrittingImprovementAgent(AgentOpenAi):
    """
    This class implements the EnglishImprovementAgentOpenAi class using langchain
    Methods:
        fix -> this method implements the logic to fix the writting of an input message.
    """

    def __init__(self, *args, temperature=0.5, **kwargs):
        super().__init__(*args, **kwargs)
        self.llm = ChatOpenAI(temperature=temperature,
                          openai_api_key=self.api_key,
                          model_name=self.model_name)

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
        constant_name = f"{strategy.value}_{template_type}"
        try:
            logging.debug(f"retrieving {constant_name} FROM  {writting_fix_type.value}")
            return getattr(writting_fix_type.value, constant_name)
        except AttributeError:
            logging.error(f"Template {constant_name} not found for strategy {strategy}, writting_fix_type: {writting_fix_type}, template: {template_type}")
            raise TemplateNotFound

    def run(self, message: str, strategy: Strategy,
            writting_fix_type: Optional[WrittingFixType]) -> str:
        """
        Enhances both grammar and style of the input message.

        Args:
            message (str): The input message.

        Returns:
            str: Enhanced message.
        """
        logging.info(f"Start run for strategy: {strategy}, writting_fix_type: {writting_fix_type}.")
        # Creaate prompts
        system_template = self._get_template(strategy=strategy,
                                             writting_fix_type=writting_fix_type,
                                             template_type="SYSTEM_MESSAGE")
        human_template = self._get_template(strategy=strategy,
                                            writting_fix_type=writting_fix_type,
                                            template_type="HUMAN_MESSAGE")

        logging.debug(f"system_template: {system_template}")
        logging.debug(f"human_template: {human_template}")
        final_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_template),
                # few_shot_prompt,
                MessagesPlaceholder(variable_name="history"),
                ("human", human_template),
            ]
        )
        
        memory = ConversationBufferMemory(
            memory_key="history", return_messages=True
        )

        conversation = ConversationChain(llm=self.llm,
                                         memory=memory,
                                         prompt=final_prompt)
        
        result = conversation.predict(input=message)
        logging.info(f"Leaving run for strategy: {strategy}, writting_fix_type: {writting_fix_type}.")
        return result

