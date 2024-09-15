from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Setup the database engine
DATABASE_URL = 'sqlite:///concerts.db'
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
