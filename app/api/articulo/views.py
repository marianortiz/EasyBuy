from fastapi import APIRouter, HTTPException, status
from api.articulo.model import Articulo


articulo = APIRouter()

@articulo.get("/articulo", status_code= 200, response_model=list[Articulo])
def get_all_articles():
    try:
        raise HTTPException
    except HTTPException as ex:
        return HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail='No se encontraron articulos.') 

@articulo.get("/articulo/{articulo_id}")
def get_articulo(articulo_id:str):
    pass

@articulo.post("/articulo/{articulo_id}")
def add_user_to_article(articulo_id):
    pass

@articulo.delete("/articulo/{articulo_id}")
def delete_user_from_article(articulo_id):
    pass

