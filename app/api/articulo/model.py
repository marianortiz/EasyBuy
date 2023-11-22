from pydantic import BaseModel
from typing import List
from api.user.model import User

class Articulo(BaseModel):
    articulo_id : str
    articulo_stock : int
    articulo_price : float 
    users : List[User]


