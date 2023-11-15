from pydantic import BaseModel, Field, validator
from classes.BookItem import BookItem
from typing import List

class BookStore(BaseModel):
    name: str
    book_shelf: List[BookItem]


    