from pydantic import BaseModel, Field, validator
from classes.Author import Author


class BookItem(BaseModel):
    name: str
    author: Author
    year_published: int
    
    #validation
    @validator("year_published")
    @classmethod
    def check_year_published(cls, value):
        if value >= 2023 and value < 3000:
            return value
        else: 
            raise ValueError("Year Published Format is Incorrect")

#validation
#year published = range 2023-3000
