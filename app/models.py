from app import db
from sqlalchemy.orm import relationship, backref


class CampsiteAmenity(db.Model):
    __tablename__ = 'campsiteamenities'

    id = db.Column(db.Integer, primary_key=True)
    campsite_id = db.Column(db.Integer, db.ForeignKey('campsites.id'))
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id'))
    campsite = db.relationship('Campsite', backref=backref("campsiteamenities", cascade="all, delete-orphan"))
    amenities = db.relationship('Amenity', backref=backref("campsiteamenities", cascade="all, delete-orphan"))

class Campsite(db.Model):
    __tablename__ = 'campsites'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    name = db.Column(db.String())
    description = db.Column(db.String())
    driving_tips = db.Column(db.String())
    lon = db.Column(db.Float())
    lat = db.Column(db.Float())
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    comments = db.relationship('Comment', cascade='all,delete', backref='campsite', lazy=True)
    amenities = db.relationship('Amenity', secondary='campsiteamenities')

    def save(self):
    	db.session.add(self)
    	db.session.commit()


    @staticmethod
    def get_all():
    		return Campsite.query.all()

    def set_amenities(self, amenities):
        self.amenities = []
        for amenity in amenities:
            hold = Amenity.find_name(amenity)
            self.amenities.append(hold)
        if self.amenities == [None]:
            self.amenities = []
        return self.amenities

    def list_amenities(self):
        collect = []
        for amenity in self.amenities:
            collect.append(amenity.name)
        return collect

    def average_rating(self):
        all_comments = []
        comments = self.comments
        if not comments:
            total = 'no comments'

        for comment in comments:
            all_comments.append(int(comment.rating))
            total = sum(all_comments) / len(all_comments)
        return total

    def delete(self):
    		db.session.delete(self)
    		db.session.commit()

    def __str__(self):
        return '-'.join([str(thing) for thing in self.things.all()])

    def __repr__(self):
    		return "<Campsite: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    rating = db.Column(db.String())
    campsite_id = db.Column(db.Integer, db.ForeignKey('campsites.id'))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    def save(self):
      db.session.add(self)
      db.session.commit()

    @staticmethod
    def get_all():
    		return Campsite.comments.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
    		return "<Comment: {}>".format(self.title)


class Amenity(db.Model):
    __tablename__ = 'amenities'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    campsites = db.relationship('Campsite', secondary='campsiteamenities')

    def save(self):
      db.session.add(self)
      db.session.commit()

    @staticmethod
    def find_name(name):
        return Amenity.query.filter_by(name=name).first()

    def __repr__(self):
        return "<Amenity: {}>".format(self.name)
