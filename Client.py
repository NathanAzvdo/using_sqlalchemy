from db import Base
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import Session

class Client(Base):
    __tablename__ = "Client"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    cpf = Column(String(14))
    email = Column(String(120))
            
    def __repr__(self) -> str:
        return f"<id:{self.id}, Client Name:{self.name}, Cpf:{self.cpf}, Email: {self.email}>"
    
    @staticmethod
    def selectOne(param, value):
        try:
            with Session(Base._engine) as session:
                column = getattr(Client, param)
                stmt = select(Client).where(column == f"{value}")
                result = session.execute(stmt).scalar_one()
                return result
        except Exception as e:
            return False, f"Error: {e}"
            
        
    @staticmethod
    def selectAll():
        try:
            with Session(Base._engine) as session:
                stmt = select(Client)
                results = session.execute(stmt).fetchall()
                return results
        except Exception as e:
            return False, f"Error: {e}"
            
    
    @staticmethod    
    def deleteById(id):
        try:
            with Session(Base._engine) as session:
                toDelete = session.get(Client, id)
                session.delete(toDelete)
                session.commit()
                return True, "Client deleted successfully"
        except Exception as e:
            return False, f"Error: {e}"
            
    @staticmethod
    def insertClient(name, cpf, email):
        try:
            with Session(Base._engine) as session:
                new_client = Client(name=name, cpf=cpf, email=email)
                session.add(new_client)
                session.commit()
                return True, "Client created successfully"
        except Exception as e:
            return False, f"Error: {e}"
        
    @staticmethod
    def updateClientById(id, name=None, cpf=None, email=None):
        try:
            with Session(Base._engine) as session:
                client = session.get(Client, id)
                if client:
                    try:
                        if name is not None:
                            client.name = name
                        if cpf is not None:
                            client.cpf = cpf
                        if email is not None:
                            client.email = email
                        session.commit()
                        return True, "Client updated successfully"
                    except Exception as e:
                        session.rollback()
                        return False, f"Error updating client: {e}"
                else:
                    return False, f"Error to find a client: {e}"
        except Exception as e:
            return False, f"Error: {e}"