<a name="top"></a>
# EasyBuy Service v0.1.0

Microservicio de Compra Facil

- [RabbitMQ_GET](#rabbitmq_get)
    - [Artículo con Stock modificado](#artículo-stock-modificado)
    - [Artículo con Precio modificado](#artículo-precio-modificado)
    - [Artículo eliminado del catálogo](#artículo-eliminado-del-catálogo)
    - [Logout de Usuarios](#logout-de-usuarios)
    
- [RabbitMQ_POST](#rabbitmq_post)
    - [Alerta de nuevo stock](#alerta-de-nuevo-stock)
    - [Alerta de nueva oferta](#alerta-de-nuevo-precio)

- [EasyBuy](#easybuy)
    - [Obtener todos los articulos](#get-all-articles)
    - [Obtener Articulo por ID](#get-article-by-id)
    - [Asociar usuario a un Articulo](#add-user-to-article)
    - [Eliminar usuario de un Articulo](#delete-user-from)
    - [Eliminar Articulo](#delete-article)



# <a name='rabbitmq_get'></a> RabbitMQ_GET

## <a name="artículo-stock-modificado"></a> Artículo con Stock modificado.

<p>Escucha a Catalog para saber cuando se modifica el stock (agrega mas stock) de un artículo.</p>

	TOPIC catalog-stock/stock-update


### Success Response

Mensaje

```
{
  "type": "article-stock-update",
  "message": {
    "articleId": "{articleId}",
    "stock": "{newArticleStock}",
    "price": "{articlePrice}"
    }
}
```

## <a name='artículo-precio-modificado'></a> Artículo con Precio modificado
[Back to top](#top)

<p>Escucha a Catalog para saber cuando se modifica el precio (menor precio) de un artículo.</p>

	TOPIC catalog-price/price-update


### Success Response

Mensaje

```
{
  "type": "article-price-update",
  "message": {
    "articleId": "{articleId}",
    "stock": "{articleStock}",
    "price": "{newArticlePrice}"
    }
}
```

## <a name='artículo-eliminado-del-catálogo'></a> Artículo eliminado del catálogo
[Back to top](#top)

<p>Escucha a Catalog para eliminar el Articulo cuando este se elimine del catálogo.</p>

	catalog-stock/articles


### Success Response

Mensaje

```
{
  "type": "article-delete",
    "message": {
      "articleId": "{articleId}"
      }
   }
```

## <a name='logout-de-usuarios'></a> Logout de Usuarios
[Back to top](#top)

<p>Escucha de mensajes logout desde auth.</p>

	auth/logout


### Success Response

Mensaje

```
{
   "type": "logout",
   "message": "{tokenId}"
}
```

# <a name='rabbitmq_post'></a> RabbitMQ_POST

## <a name='alerta-de-nuevo-stock'></a> Alerta de nuevo Stock
[Back to top](#top)

<p>Cuando se agrega nuevo stock a un Articulo que no tenia stock, se da alerta para que se notifique al usuario asociado al articulo que ya hay nuevo stock disponible.</p>

	stock/new-stock


### Success Response

Mensaje

```
{
  "exchange": "stock",
  "queue": "new-stock"
  "type": "new-stock",
    "message": {
      "article": [{
        "articleId": "{articleId}",
        "stock": "{stock}",
        "updated": "{date}",
        "enabled": true,
        "users": [
            "{user_id}",
            "{user_id}",
            ...
            ]
      }]
    }
}
```

## <a name='alerta-de-nuevo-precio'></a> Alerta de nuevo Precio
[Back to top](#top)

<p>Cuando se modifica el precio de un Articulo con un precio menor al que tenia, se da alerta para que se notifique al usuario asociado al articulo de que hay una oferta en el Articulo.</p>

	price/new-price


### Success Response

Mensaje

```
{
  "exchange": "price",
  "queue": "new-price"
  "type": "new-price",
    "message": {
      "article": [{
        "articleId": "{articleId}",
        "price": "{price}",
        "updated": "{date}",
        "enabled": true,
        "users": [
            "{user_id}",
            "{user_id}",
            ...
            ]
      }]
    }
}
```

# <a name='EasyBuy'></a> EasyBuy

## <a name='get-all-articles'></a> Obtener todos los articulos
[Back to top](#top)

<p>Obtener todos los Articulos.</p>

    GET /v1/articulo


Header Autorización

```
Authorization=bearer {token}
```

### Success Response

```
HTTP/1.1 200 OK

{
    [
    'articulo_id' : {ariculo_id}
    'articulo_stock' : {articulo_stock}
    'articulo_price' : {articulo_precio} 
    'users' : {[
        'user_id' : {user_id}
        ]}
    ],
    [
     'articulo_id' : {ariculo_id}
     'articulo_stock' : {articulo_stock}
     'articulo_price' : {articulo_precio} 
     'users' : {[
        'user_id' : {user_id}
        ]}
    ]
}
```

### Error Response

```
HTTP/1.1 404 NOT_FOUND

{   
    'error' : 'NOT_FOUND',
    'status_code : '404,
    'message' : 'No se encontraron Articulos.'
}
```
```
HTTP/1.1 400 BAD_REQUEST
{
    'error' : 'BAD_REQUEST',
    'status_code : '400,
    'message' : 'Method not allowed' 
}
```
```
HTTP/1.1 403 FORBIDDEN
{
    'error' : 'FORBIDDEN',
    'status_code : '403,
    'message' : 'Access denied' 
}
```

```
HTTP/1.1 {CODE} Custom Error
 {
    'error' : {Custom Error}
    'status_code': {code},
    'message' : 'Custom error message'
 }
```

## <a name='get-article-by-id'></a> Obtener Articulo por Id
[Back to top](#top)

<p>Obtener un articulo en particular por id .</p>

    GET /v1/articulo/{articulo_id}


Header Autorización

```
Authorization=bearer {token}
```

### Success Response

```
HTTP/1.1 200 OK

{   
    'articulo_id' : {ariculo_id}
    'articulo_stock' : {articulo_stock}
    'articulo_price' : {articulo_precio} 
    'users' : {[
        'user_id' : {user_id}
        ]}
}
```
### Error Response

```
HTTP/1.1 404 NOT_FOUND

{   
    'error' : 'NOT_FOUND',
    'status_code : '404,
    'message' : 'Articulo: {articulo_id} no encontrado'
}
```
```
HTTP/1.1 400 BAD_REQUEST
{
    'error' : 'BAD_REQUEST',
    'status_code : '400,
    'message' : 'Method not allowed' 
}
```
```
HTTP/1.1 403 FORBIDDEN
{
    'error' : 'FORBIDDEN',
    'status_code : '403,
    'message' : 'Access denied' 
}
```

```
HTTP/1.1 {CODE} Custom Error
 {
    'error' : {Custom Error}
    'status_code': {code},
    'message' : 'Custom error message'
 }
```

## <a name='add-user-to-article'></a> Asociar usuario a un Articulo
[Back to top](#top)

<p>Asocia un usuario a un Articulo.
El usuario se agrega al consultar el Current User</p>

    POST /v1/articulo/add/{articulo_id}


Header Autorización

```
Authorization=bearer {token}
```

### Success Response

```
HTTP/1.1 200 OK

{   
    'Message' : 'Usuario {user_id} agregado a la lista del articulo {ariculo_id}'
}
```

### Error Response

```
HTTP/1.1 404 NOT_FOUND

{   
    'error' : 'NOT_FOUND',
    'status_code : '404,
    'message' : 'Articulo: {articulo_id} no encontrado'
}
```
```
HTTP/1.1 400 BAD_REQUEST
{
    'error' : 'BAD_REQUEST',
    'status_code : '400,
    'message' : 'Method not allowed' 
}
```
```
HTTP/1.1 403 FORBIDDEN
{
    'error' : 'FORBIDDEN',
    'status_code : '403,
    'message' : 'Access denied' 
}
```

```
HTTP/1.1 {CODE} Custom Error
 {
    'error' : {Custom Error}
    'status_code': {code},
    'message' : 'Custom error message'
 }
```

## <a name='delete-user-from'></a> Eliminar usuario de un Articulo

[Back to top](#top)

<p>Eliminar usuario de la lista asociada al Articulo.</p>

    DELETE /v1/articulo/delete/user/{articulo_id}


Header Autorización

```
Authorization=bearer {token}
```

### Success Response

```
HTTP/1.1 200 OK

{   
    'Message' : 'Usuario {user_id} eliminado de la lista del articulo {ariculo_id}'
}
```

### Error Response

```
HTTP/1.1 404 NOT_FOUND

{   
    'error' : 'NOT_FOUND',
    'status_code : '404,
    'message' : 'Articulo: {articulo_id} no encontrado'
}
```
```
HTTP/1.1 400 BAD_REQUEST
{
    'error' : 'BAD_REQUEST',
    'status_code : '400,
    'message' : 'Method not allowed' 
}
```
```
HTTP/1.1 403 FORBIDDEN
{
    'error' : 'FORBIDDEN',
    'status_code : '403,
    'message' : 'Access denied' 
}
```

```
HTTP/1.1 {CODE} Custom Error
 {
    'error' : {Custom Error}
    'status_code': {code},
    'message' : 'Custom error message'
 }
```

## <a name='delete-article'></a> Eliminar Articulo

[Back to top](#top)

<p>Eliminar un Articulo.</p>

    DELETE /v1/articulo/delete/{articulo_id}


Header Autorización

```
Authorization=bearer {token}
```

### Success Response

```
HTTP/1.1 200 OK

{   
    'Message' : 'Articulo eliminado.'
}
```

### Error Response

```
HTTP/1.1 404 NOT_FOUND

{   
    'error' : 'NOT_FOUND',
    'status_code : '404,
    'message' : 'Articulo: {articulo_id} no encontrado'
}
```
```
HTTP/1.1 400 BAD_REQUEST
{
    'error' : 'BAD_REQUEST',
    'status_code : '400,
    'message' : 'Method not allowed' 
}
```
```
HTTP/1.1 403 FORBIDDEN
{
    'error' : 'FORBIDDEN',
    'status_code : '403,
    'message' : 'Access denied' 
}
```

```
HTTP/1.1 {CODE} Custom Error
 {
    'error' : {Custom Error}
    'status_code': {code},
    'message' : 'Custom error message'
 }
```
