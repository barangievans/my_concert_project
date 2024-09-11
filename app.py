from models import Band, Venue, Concert
from database import session

# Example usage
band = session.query(Band).first()
print(band.name)
