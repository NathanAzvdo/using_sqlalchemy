from db import Base
from sqlalchemy import Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import Session, relationship

class PedidoProduto(Base):
    __tablename__ = "pedido_produto"
    pedido_id = Column(Integer, ForeignKey('Pedido.id_pedido') ,primary_key=True)
    produto_id = Column(Integer, ForeignKey('Cliente.id'), primary_key=True)
    
    Produto = relationship("Produto")
    Pedido = relationship("Pedido")
    
        
def __repr__(self) -> str:
        return f"<id:{self.id_pedido}, Client ID:{self.client_id}>"