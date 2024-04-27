from db import Base
from sqlalchemy import Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import Session, relationship

class Product(Base):
    __tablename__ = "Pedido"
    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('Cliente.id'))
    
    cliente = relationship("Cliente")
        
    def __repr__(self) -> str:
        return f"<id:{self.id_pedido}, Client ID:{self.client_id}>"