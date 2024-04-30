from db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PedidoProduto(Base):
    __tablename__ = "pedido_produto"
    pedido_id = Column(Integer, ForeignKey('Pedido.id_pedido'), primary_key=True)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True)
    quantidade = Column(Integer, default=1)
    
    produto = relationship("Produto")
    pedido = relationship("Pedido")
    
    @classmethod
    def adicionar_produto(cls, pedido_id, produto_id):
        try:
            nova_relacao = cls(pedido_id=pedido_id, produto_id=produto_id)
            nova_relacao.save()
            return True, "Produto adicionado ao pedido com sucesso"
        except Exception as e:
            return False, f"Erro ao adicionar produto ao pedido: {e}"

    @classmethod
    def remover_produto(cls, pedido_id, produto_id):
        try:
            relacao_produto = cls.query.filter_by(pedido_id=pedido_id, produto_id=produto_id).first()
            if relacao_produto:
                relacao_produto.delete()
                return True, "Produto removido do pedido com sucesso"
            else:
                return False, "Relação produto-pedido não encontrada"
        except Exception as e:
            return False, f"Erro ao remover produto do pedido: {e}"

    