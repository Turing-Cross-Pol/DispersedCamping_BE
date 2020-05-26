from app import db
#from sqlalchemy.dialects.postgresql import JSON


class Campsite(db.Model):
    __tablename__ = 'campsites'

    id = db.Column(db.Integer, primary_key=True)
#    image_url = db.Column(db.String())
#    city = db.Column(db.String())
#    state = db.Column(db.String())
    name = db.Column(db.String())
#    description = db.Column(db.String())
#    driving_tips = db.Column(db.String())
#    lon = db.Column(db.Float())
#    lat = db.Column(db.Float())
#    date_created = db.Column(db.DateTime, default=db.func.current_timestamp()


    def __init__(self, name):
    #		self.image_url = image_url
    #		self.city = city
    #		self.state = state
    		self.name = name
    #		self.description = description
    #		self.driving_tips = driving_tips
    #		self.lon = lon
    #		self.lat = lat 
    
    
    def save(self):
    	db.session.add(self)
    	db.session.commit()
    
    
    @staticmethod
    def get_all():
    		return Campsite.query.all()
    
    
    def delete(self):
    		db.session.delete(self)
    		db.session.commit()
    
    
    def __repr__(self):
    		return "<Campsite: {}>".format(self.name)
    

#class CampsiteSchema(ma.SQLAlchemyAutoSchema):
#		class Meta:
#				model = Campsite
