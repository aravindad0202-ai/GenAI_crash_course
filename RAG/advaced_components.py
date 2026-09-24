# Query enrichment

from google import genai
from dotenv import load_dotenv
import json

load_dotenv(r'D:\IT\AI\teaching\GenAI_module_1\.env')

client = genai.Client()

query_enrichment_prompt = """
Assume that you are a seniour prompt engineer you task is to expand the input query given by the user in triple backtics given below.
If the query is doesn't have enough information or flat. ask a followup question till have enough information. Then re-create the query based on the initial query and gathered information.
While generating the query don't go out of the box. You must stick with the core concept of the user query

```
{user_query}
```

Output_format: JSON it must have two keyse
'information_required': 'true' (if additional details requried) or 'false' (no need information)
'content': your response.
"""

query_decomposition_prompt = """**Role:** Expert Information Retrieval Architect & RAG Specialist

**Objective:** Your task is to analyze a complex user query and decompose it into a minimum of 3 distinct, self-contained sub-queries. This technique, known as Query Decomposition, is used to retrieve highly targeted documents for each specific facet of a multi-part question before synthesizing a final answer.

**Decomposition Guidelines:**
1. **Single-Intent Focus:** Break the complex query into smaller modules where each sub-query targets exactly one specific concept, question, or entity.
2. **Context Resolution (De-referencing):** Each sub-query must be completely self-contained. Resolve any pronouns (it, they, this) from the original query into their explicit nouns so the sub-query makes sense in isolation.
3. **MECE Principle:** The sub-queries should be Mutually Exclusive (minimal overlap) and Collectively Exhaustive (together, they cover the entirety of the original user's request).
4. **Volume:** Generate a minimum of 3 sub-queries. If the query is exceptionally complex, you may generate more.

**Output Format:**
Output ONLY a valid JSON array of strings containing the decomposed sub-queries. Do not include any introductory text, explanations, or markdown blocks outside the JSON array.

**Input Query:**
```{user_query}```
"""

def query_enricher(query: str) -> str:
    query_prompt = query_enrichment_prompt.format(user_query=query)
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = query_prompt
    )
    return response.text

loop = True
# while loop:
user_query = input("enter your query:")
raw_res = query_enricher(user_query)
print(raw_res)
print("-------------------")
json_res = json.loads(raw_res)
print(json_res)
print(json_res)

    