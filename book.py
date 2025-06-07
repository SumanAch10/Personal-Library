from pydantic import BaseModel
from typing import Optional
import random

book_list = []

class UpdateBook(BaseModel):
    bk_name: Optional[str] = None
    bk_author: Optional[str] = None
    bk_description: Optional[str] = None
    bk_price: Optional[str] = None

class Book(BaseModel):
    bk_id:Optional[int]=None
    bk_name:str
    bk_author:str
    bk_description:str
    bk_price:str
    

    