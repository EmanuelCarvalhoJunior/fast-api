from fastapi import FastAPI
import uvicorn

app = FastAPI()
vendas = {
    1:{"item":"lata","preco_unitario":4,"quantidade":5},
    2:{"item":"garrafa 2 L","preco_unitario":4,"quantidade":5},
    3:{"item":"garrafa 750ml","preco_unitario":4,"quantidade":5},
    4:{"item":"lata mini","preco_unitario":4,"quantidade":5}
}

@app.get("/")
def home():
    return "minha APi está no ar"

@app.get("/vendas")
async def venda():
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_vendas}")
async def get_vendas(id_vendas: int):
    if id_vendas in vendas:
        return vendas[id_vendas]
    else:
        return {"Erro":"ID da venda inexistente"}



if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=7779)


