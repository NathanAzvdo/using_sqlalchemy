from db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PedidoProduto(Base):
    __tablename__ = "pedido_produto"
    pedido_id = Column(Integer, ForeignKey('Pedido.id_pedido'), primary_key=True)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True)
    
    produto = relationship("Produto")
    pedido = relationship("Pedido")
