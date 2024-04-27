from db import Base
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import Session

class Product(Base):
    __tablename__ = "Produto"
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_produto = Column(String(50))
    preco_produto = Column(float)
        
    def __repr__(self) -> str:
        return f"<id:{self.id_produto}, Product Name:{self.nome_produto}, Preço:{self.preco_produto}>"
    