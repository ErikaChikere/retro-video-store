from flask import current_app
from app import db
from dataclasses import dataclass 
from datetime import datetime


@dataclass
class Customer(db.Model):
    id: int 
    name : str 
    postal_code: str
    phone: str
    registered_at: datetime
    videos_checked_out_count:int 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)
    registered_at = db.Column(db.DateTime)
    videos_checked_out_count = db.Column(db.Integer)
    
    
    def as_json(self):

        result_dict = {
                "id": self.id,
                "name": self.name,
                "registered_at": self.registered_at,
                "postal_code": self.postal_code,
                "phone": self.phone,
                "videos_checked_out_count": 0, 

            }

        return result_dict

    @classmethod
    def from_json(cls,customer_dict): 

        return Customer(name = customer_dict["name"], 
                postal_code = customer_dict["postal_code"],
                phone = customer_dict["phone"],
                videos_checked_out_count = 0)