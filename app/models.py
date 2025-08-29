from sqlalchemy import Column, Integer, String, Float, UniqueConstraint
from .database import Base

class Business(Base):
    """
    Represents a business scraped from Google Maps.
    """
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    website = Column(String, nullable=True)
    google_maps_url = Column(String, nullable=False)
    rating = Column(Float, nullable=True)
    reviews_count = Column(Integer, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    __table_args__ = (UniqueConstraint('place_id', name='uq_place_id'),)

    def __repr__(self):
        return f"<Business(name='{self.name}', address='{self.address}')>"
