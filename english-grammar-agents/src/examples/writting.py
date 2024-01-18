from dotenv import load_dotenv

from services.writting import writte_grammar_only, writte_properly

load_dotenv('./envs/debug.env')

message = """
Yesturday, I goes to the store to byed some opples, but they was all out.
"""

result = writte_properly(message=message)

print(f"write_propperly: {result}")

result = writte_grammar_only(message=message)

print(f"writte_grammar_only: {result}")