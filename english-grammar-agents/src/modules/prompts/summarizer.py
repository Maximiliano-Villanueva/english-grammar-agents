SUMMARIZER_STUFF_HUMAN_MESSAGE = """
Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:
"""

SUMMARIZER_MAP_TEMPLATE = """
The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes 
Helpful Answer:
"""

SUMMARIZER_REDUCE_TEMPLATE = """
The following is set of summaries:
{docs}
Take these and distill it into a final, consolidated summary of the main themes. 
Helpful Answer:
"""