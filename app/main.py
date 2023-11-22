from fastapi import FastAPI
from api.articulo.views import articulo

app = FastAPI(
    title="Easy Buy Api" ,
    description= "Api Rest desarrollada con FastApi y mongoDB",
    version= "0.0.1",
)


app.include_router(articulo)


#@app.get("/")
#def main():
#    return "Home Page"
