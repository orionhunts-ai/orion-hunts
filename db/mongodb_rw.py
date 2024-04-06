import asyncio
from typing import Any, Dict, List
from motor.motor_asyncio import AsyncIOMotorClient
from multiprocessing import Pool
import os

class DatabaseConnector:
    """A connector class for asynchronous operations with MongoDB using motor and multiprocessing."""

    def __init__(self, uri: str, database_name: str) -> None:
        """
        Initializes the DatabaseConnector instance.

        Parameters:
        - uri: A string representing the MongoDB URI.
        - database_name: The name of the database to connect to.
        """
        self.uri = uri
        self.database_name = database_name
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client[self.database_name]

    async def insert_document(self, collection_name: str, document: Dict[str, Any]) -> str:
        """
        Asynchronously inserts a single document into a collection.

        Parameters:
        - collection_name: The name of the collection to insert the document into.
        - document: The document to be inserted.

        Returns:
        The ID of the inserted document.
        """
        collection = self.db[collection_name]
        result = await collection.insert_one(document)
        return result.inserted_id

    async def query_documents(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Asynchronously queries documents from a collection based on a query.

        Parameters:
        - collection_name: The name of the collection to query.
        - query: The query criteria.

        Returns:
        A list of documents matching the query criteria.
        """
        collection = self.db[collection_name]
        cursor = collection.find(query)
        documents = await cursor.to_list(length=100)  # Adjust length as needed
        return documents

def run_in_loop(coroutine: asyncio.coroutine) -> Any:
    """
    Runs a coroutine in a new event loop.

    Parameters:
    - coroutine: The coroutine to be run.

    Returns:
    The result of the coroutine execution.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(coroutine)
    loop.close()
    return result

def worker_process(task_info: Dict[str, Any]) -> Any:
    """
    Processes a task in a separate process. Initializes a DatabaseConnector and executes a specified task.

    Parameters:
    - task_info: A dictionary containing task information, including URI, database name, task type, collection name, and task-specific data.

    Returns:
    The result of the task execution.
    """
    connector = DatabaseConnector(task_info['uri'], task_info['database_name'])
    task = task_info['task']
    if task == 'insert':
        return run_in_loop(connector.insert_document(task_info['collection_name'], task_info['document']))
    elif task == 'query':
        return run_in_loop(connector.query_documents(task_info['collection_name'], task_info['query']))

if __name__ == "__main__":
    tasks = [
        {'uri': 'mongodb://localhost:27017', 'database_name': 'testdb', 'task': 'insert', 'collection_name': 'test_collection', 'document': {'name': 'John Doe', 'age': 30}},
        {'uri': 'mongodb://localhost:27017', 'database_name': 'testdb', 'task': 'query', 'collection_name': 'test_collection', 'query': {'age': 30}},
    ]

    with Pool(os.cpu_count()) as p:
        results = p.map(worker_process, tasks)
        print(results)