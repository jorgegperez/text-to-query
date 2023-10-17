AGGREGATION_TEMPLATE = """
Based on the following collection samples, return an object with the following structure:
    "collection": "The name of the collection you will start the aggregation with",
    "type": "should be either "LIST" if the result of the aggregation is a list or "COUNT" if the result is a number",
    "aggregate": "The aggregation pipeline you will use to answer the query"
If you need to use multiple collections, you can use the $lookup operator.For example, if you are asked to find the number of quizzes owned by an specific user,
you will need to use the $lookup operator to join the users collection with the quizzes collection.
If you need to project the result, ALWAYS use "count" as the field name.
You should NEVER project an ObjectId.
You should ALWAYS use double quotes to enclose field names and mongo operators.
If the query is related to the creation of a new document, ALWAYS use the 'createdAt' field and not the 'updatedAt' field.
----------------
QUERY: {query}
SCHEMAS: {schemas}
AGGREGATION:"""
