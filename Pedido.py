from db import Base
from sqlalchemy import Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import Session, relationship

class Pedido(Base):
    __tablename__ = "Pedido"
    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('Client.id'))
    
    cliente = relationship("Client")
        
    def __repr__(self) -> str:
        return f"<id:{self.id_pedido}, Client ID:{self.client_id}>"