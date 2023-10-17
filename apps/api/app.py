import json
import os
import re
import pymongo
from chains import collection_extraction_chain, get_collections_schemas, aggregation_chain
from dotenv import load_dotenv
from fastapi import FastAPI
from uvicorn import run
from bson import json_util
from utils import utils


app = FastAPI()


def init_db():
    mongodb_host = os.environ.get("MONGO_DB_HOST")
    mongodb_port = int(os.environ.get("MONGO_DB_PORT"))

    client = pymongo.MongoClient(mongodb_host, mongodb_port)
    return client["test"]


@app.get("/")
async def root(query: str):
    database = init_db()
    collections = collection_extraction_chain.run(
        collection_names=database.list_collection_names(),
        query=query
    )
    schemas = get_collections_schemas(collections, database)
    aggregation_str = aggregation_chain.run(schemas=schemas, query=query)
    aggregation_str = re.sub(r'ISODate\("([^"]+)"\)', utils.replace_isodate, aggregation_str)
    # print(aggregation_str)

    aggregation = json.loads(aggregation_str)
    print(aggregation)
    pipeline = utils.replace_with_datetime(aggregation["aggregate"])

    print(pipeline)
    result = database[aggregation["collection"]].aggregate(pipeline)
    result_list = list(json.loads(json_util.dumps(result)))
    # print(result_list)
    if result_list:
        if aggregation["type"] == "COUNT":
            return {"message": result_list[0], "type": aggregation["type"]}
        else:
            return {"message": result_list, "type": aggregation["type"]}
    return {"message": "No results found", "type": aggregation["type"]}


if __name__ == "__main__":
    load_dotenv()
    run(app, host="0.0.0.0", port=8000)
