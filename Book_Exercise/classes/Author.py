from pydantic import BaseModel, Field, validator
import re

class Author(BaseModel):
    author_id: str
    name: str
    
    #validation
    @validator("author_id")
    @classmethod
    def check_author_id(cls, value):
        if re.match(r"^[A-Z]{4}-\d{4}$", value):
            return value
        else:
            raise ValueError("Format is incorrect")



