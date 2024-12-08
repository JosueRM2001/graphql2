from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from typing import List
@strawberry.type
class Tienda:
    producto: str
    precio: int
    cantidad: int
@strawberry.type
class Query:
    @strawberry.field
    def tiendas(self)->List[Tienda]:
        tienda_data=[
            Tienda(producto="telefonos", precio= 150, cantidad= 20),
             Tienda(producto="camputadoras", precio= 500, cantidad= 30),
              Tienda(producto="tablets", precio= 250, cantidad= 35),
               Tienda(producto="laptops", precio= 400, cantidad= 40),
                Tienda(producto="impresoras", precio= 300, cantidad= 10),
        ]
        return tienda_data
schema=strawberry.Schema(query=Query)
app=FastAPI()
@app.get("/")
def index():
    return{"message":"Bienbenido este es una pagina en Graphql"}
app.add_route("/graphql", GraphQL(schema,debug=True))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8080)
