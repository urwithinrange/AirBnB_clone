#!/usr/bin/python3
"""
Review (models/review.py):
Public class attributes:
place_id: string - empty string: it will be the Place.id
user_id: string - empty string: it will be the User.id
text: string - empty string
"""


class Review(BaseModel):
    """Class BM sub"""
    place_id = ""
    user_id = ""
    text = ""
