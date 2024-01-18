
import os
from dotenv import load_dotenv

# Internal imports
from common.entities.strategy import StrategySummarize

from modules.agents.summarizer import Summarizer

load_dotenv('./envs/debug.env')

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL_NAME")

agent = Summarizer(api_key=api_key, model_name=model_name)

text_path = os.path.join("sample_data", "rome.txt")

with open(text_path, "r") as f:
    message = f.read()

result = agent.run(message=message,
                   strategy=StrategySummarize.MAP_REDUCE
                   )

print(result)