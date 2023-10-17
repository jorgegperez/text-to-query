import ast
import os
from dotenv import load_dotenv
from pymongo.database import Database
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, TransformChain
from langchain.llms import openai
from templates import aggregation, collection_extraction

load_dotenv()

llm = openai.OpenAI(openai_api_key=os.environ.get('OPENAI_API_KEY'))


def get_collections_schemas(collection_names_str: str, database: Database):
    try:
        collection_names = ast.literal_eval(collection_names_str)
        schemas = []
        for collection in collection_names:
            sample = database[collection].find_one()
            schemas.append({"collection": collection, "schema": sample})
        return {"schemas": str(schemas)}
    except ValueError:
        ValueError("collection_names_str is not a valid json string")


schema_chain = TransformChain(
    input_variables=["collection_names"], output_variables=["schemas"], transform=get_collections_schemas
)

collection_extraction_prompt = PromptTemplate(input_variables=["collection_names", "query"], template=collection_extraction.COLLECTINON_EXTRACTION_TEMPLATE)

collection_extraction_chain = LLMChain(llm=llm, prompt=collection_extraction_prompt)

aggregation_prompt = PromptTemplate(input_variables=["schemas", "query"], template=aggregation.AGGREGATION_TEMPLATE)

aggregation_chain = LLMChain(llm=llm, prompt=aggregation_prompt)
