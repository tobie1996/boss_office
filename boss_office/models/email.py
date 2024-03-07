from ..core.db import Base
from sqlalchemy import Column, String, Integer
import uuid


class Email(Base):
    __tablename__ = 'email'
    id = Column(String, nullable=False, primary_key=True, default=str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    code = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<email={self.email}, id={self.id}, code={self.code}>"
