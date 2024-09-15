from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base
from .concert import Concert
from .band import Band

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def concerts(self):
        return self.concerts

    def bands(self):
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        from sqlalchemy import func
        most_frequent_band = session.query(
            Band, func.count().label('concert_count')
        ).join(Band.concerts).filter(Concert.venue_id == self.id).group_by(
            Band.id
        ).order_by(func.count().desc()).first()
        return most_frequent_band[0]
