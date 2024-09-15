from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from . import Base
from .concert import Concert

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')
    
    def concerts(self):
        return self.concerts

    def venues(self):
        return {concert.venue for concert in self.concerts}

    def play_in_venue(self, venue, date):
        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]

    @classmethod
    def most_performances(cls):
        from sqlalchemy import func
        most_performances_band = session.query(
            cls, func.count().label('concert_count')
        ).join(cls.concerts).group_by(cls.id).order_by(
            func.count().desc()
        ).first()
        return most_performances_band[0]
