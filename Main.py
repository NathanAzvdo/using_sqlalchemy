from Client import Client
from Pedido import Pedido
from PedidoProduto import PedidoProduto
from Produto import Produto
from db import Base

class Main:
    def __init__(self):
        Base.metadata.create_all(Base._engine)
        print("Qual seu nome?")
        nome =input()
        print("Cpf?")
        cpf = input()
        print("email?")
        email = input()
        client = Client.insertClient(nome, email, cpf)
        print(Pedido.criar(client))
        
        
if __name__ == "__main__":
    main = Main()
