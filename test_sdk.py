import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "library_sdk"))

from openapi_client import ApiClient, Configuration
from openapi_client.api.books_api import BooksApi


config = Configuration(host="http://127.0.0.1:8000")
client = ApiClient(config)
api = BooksApi(client)

books = api.get_books_books_get()
print(books)
