from sqlalchemy import Column, Integer, String
from database import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)
