from Client import Client
from Pedido import Pedido
from PedidoProduto import PedidoProduto
from Produto import Produto
from db import Base

class Main:
    def __init__(self):
        Base.metadata.create_all(Base._engine)
        print(f"Clientes: {Client.selectAll()}")
        print(f"Produtos: {Produto.selectAll()}")

if __name__ == "__main__":
    main = Main()
