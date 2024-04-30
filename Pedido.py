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
    
    @staticmethod
    def criar(client_id):
        try:
            with Session(Base._engine) as session:
                new_order = Pedido(client_id=client_id)
                session.add(new_order)
                session.commit()
                return True, "Order created sucessfully"
        except Exception as e:
            return False, f"Error: {e}"
    
    @staticmethod
    def deleteById(id):
        try:
            with Session(Base._engine) as session:
                toDelete = session.get(Pedido, id)
                session.delete(toDelete)
                session.commit()
                return True, "Order deleted successfully"
        except Exception as e:
            return False, f"Error: {e}"
