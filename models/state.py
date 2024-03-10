#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes the State instance"""
        super().__init__(*args, **kwargs)
        self.name = ""
