from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String, nullable=False)

    band = relationship('Band')
    venue = relationship('Venue')
