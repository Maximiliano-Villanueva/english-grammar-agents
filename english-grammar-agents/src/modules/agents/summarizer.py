# Standard imports
import logging
from typing import Union

# Internal imports
from common.entities.strategy import StrategySummarize
from modules.agents.base import AgentOpenAi
import modules.prompts.summarizer as summarizer_prompts

# Third party imports
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate


class Summarizer(AgentOpenAi):
    """ Implementation of a summarizer agent using OpenAi. """

    def __init__(self, *args, temperature=0.5, **kwargs):
        super().__init__(*args, **kwargs)
        self.llm = ChatOpenAI(temperature=temperature,
                              openai_api_key=self.api_key,
                              model_name=self.model_name)

    def _run_stuff(self, message: str):
        """ Run the summarizer using the stuff strategy. """
        logging.info("Start running _run_stuff in summary")
        # Define prompt
        prompt_template = summarizer_prompts.SUMMARIZER_STUFF_HUMAN_MESSAGE
        prompt = PromptTemplate.from_template(prompt_template)

        logging.debug(f"prompt: {prompt}")
        # Define LLM chain
        llm_chain = LLMChain(llm=self.llm, prompt=prompt)

        # Define StuffDocumentsChain
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain,
                                          document_variable_name="text")

        # Convert string to docs
        text_splitter = RecursiveCharacterTextSplitter(
            # Set a really small chunk size, just to show.
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )

        docs = text_splitter.create_documents([message])

        logging.info("Finished running _run_stuff in summary")
        return stuff_chain.run(docs)

    def _run_map_reduce(self, message: str):
        """ Run the summarizer using the map reduce strategy. """
        # Define prompts
        logging.info("Start running _run_map_reduce in summary")
        # Map
        map_template = summarizer_prompts.SUMMARIZER_MAP_TEMPLATE
        map_prompt = PromptTemplate.from_template(map_template)
        logging.debug(f"map_prompt: {map_prompt}")

        # Define the chain for map
        map_chain = LLMChain(llm=self.llm, prompt=map_prompt)
        
        # Reduce
        reduce_template = summarizer_prompts.SUMMARIZER_REDUCE_TEMPLATE
        reduce_prompt = PromptTemplate.from_template(reduce_template)
        logging.debug(f"reduce_prompt: {reduce_prompt}")

        # Define the chain for reduce
        reduce_chain = LLMChain(llm=self.llm, prompt=reduce_prompt)

        # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="docs"
        )

        # Combines and iteratively reduces the mapped documents
        reduce_documents_chain = ReduceDocumentsChain(
            # This is final chain that is called.
            combine_documents_chain=combine_documents_chain,
            # If documents exceed context for `StuffDocumentsChain`
            collapse_documents_chain=combine_documents_chain,
            # The maximum number of tokens to group documents into.
            token_max=4000,
        )

        # Combining documents by mapping a chain over them, then combining results
        map_reduce_chain = MapReduceDocumentsChain(
            llm_chain=map_chain,
            reduce_documents_chain=reduce_documents_chain,
            # The variable name in the llm_chain to put the documents in
            document_variable_name="docs",
            return_intermediate_steps=False,
        )

        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000, chunk_overlap=0
        )

        # Convert string to docs
        text_splitter = RecursiveCharacterTextSplitter(
            # Set a really small chunk size, just to show.
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
            is_separator_regex=False,
        )

        docs = text_splitter.create_documents([message])

        split_docs = text_splitter.split_documents(docs)

        logging.info("Finished running _run_map_reduce in summary")
        return map_reduce_chain.run(split_docs)

    def run(self, message: str, strategy: StrategySummarize) -> str:
        """
        Enhances both grammar and style of the input message.

        Args:
            message (str): The input message.
            strategy (StrategySummarize): strategy to use when summarizing
        Returns:
            str: Enhanced message.
        """
        if strategy == StrategySummarize.STUFF:
            return self._run_stuff(message=message)
        elif strategy == StrategySummarize.MAP_REDUCE:
            return self._run_map_reduce(message=message)
        else:
            raise NotImplementedError