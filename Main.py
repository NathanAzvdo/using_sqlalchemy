from Client import Client
from db import Base

class Main(Client, Base): 
    Base.metadata.create_all(Base._engine)#essa linha cria as tabelas se elas não existirem(definido nas classes) 
    