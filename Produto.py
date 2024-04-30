from db import Base
from sqlalchemy import Column, Integer, String, select, Float
from sqlalchemy.orm import Session

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    preco = Column(Float)
        
    def __repr__(self) -> str:
        return f"<Produto - ID:{self.id}, Nome:{self.nome}, Preço:{self.preco}>"
    
    @staticmethod
    def selectOne(param, value):
        try:
            with Session(Base._engine) as session:
                Column = getattr(Produto, param)
                stmt = select(Produto).where(Column == f"{value}")
                result = session.execute(stmt).scalar_one()
                return result
        except Exception as e:
            return False, f"Error: {e}"
        
    @staticmethod
    def selectAll():
        try:
            with Session(Base._engine) as session:
                stmt = select(Produto)
                results = session.execute(stmt).fetchall()
                return results
        except Exception as e:
            return False, f"Error: {e}"
        
    @staticmethod
    def deleteById(id):
        try:
            with Session(Base._engine) as session:
                toDelete = session.get(Produto, id)
                session.delete(toDelete)
                session.commit()
                return True, "Product deleted successfully"
        except Exception as e:
            return False, f"Error: {e}"
        
    @staticmethod
    def insertProduct(nome, preco):
        try:
            with Session(Base._engine) as session:
                new_product = Produto(nome=nome, preco=preco)
                session.add(new_product)
                session.commit()
                return True, "Product created sucessfully"
        except Exception as e:
            return False, f"Error: {e}"
    
    @staticmethod
    def updateProductById(id, nome=None, preco=None):
        try:
            with Session(Base._engine) as session:
                produto = session.get(Produto, id)
                if Produto:
                    try:
                        if nome is not None:
                            produto.nome = nome
                        if preco is not None:
                            produto.preco = preco
                        session.commit()
                        return True, "Product updated successfully"
                    except Exception as e:
                        session.rollback()
                        return False, f"Error updating product"
                else:
                    return False, "Product don't found"
        except Exception as e:
            return False, f"Error: {e}"#se cair aqui :(