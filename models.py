from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    name = db.Column(db.String())
    description = db.Column(db.String())
    driving_tips = db.Column(db.String())
    lon = db.Column(db.Float())
    lat = db.Column(db.Float())
		datetime = db.Column(db.DateTime())
		

    def __init__(self, image_url, city, state, name, description, driving_tips, lon, lat, datetime):
        self.image_url = image_url
				self.city = city
				self.state = state
				self.name = name
				self.description = description
				self.driving_tips = driving_tips 
				self.lon = lon 
				self.lat = lat 
				self.datetime = datetime 

    def __repr__(self):
        return '<id {}>'.format(self.id)
