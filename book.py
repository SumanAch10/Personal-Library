from pydantic import BaseModel
from typing import Optional
import random

book_list = []

class Book(BaseModel):
    bk_id:Optional[int]=None
    bk_name:str
    bk_author:str
    bk_description:str
    bk_price:str
    

    