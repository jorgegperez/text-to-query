COLLECTINON_EXTRACTION_TEMPLATE = """
Based on the user query, return a list of collections needed to answer the query.
You shold ONLY return a List of collections, nothing else.
COLLECTIONS: {collection_names}
----------------
QUERY: how many users are demo?
ANSWER: ['users']
QUERY: {query}
ANSWER:
"""
