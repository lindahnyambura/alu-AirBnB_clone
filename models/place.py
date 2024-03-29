# models/place.py
from .base_model import BaseModel


class Place(BaseModel):
    """Place class for the HBNB project."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = super().to_dict()
        return dictionary
