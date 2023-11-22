from api.user.schema import user_schema

def articuloEntity(item) -> dict:
    return {
        "articulo_id" : str(item['_id']),
        "articulo_stock" : item['stock'],
        "articulo_price" : item['price'],
        "users_list" : list(user_schema)
    }

def articulosEntities(entities) -> list:
    return [articuloEntity(item) for item in entities]