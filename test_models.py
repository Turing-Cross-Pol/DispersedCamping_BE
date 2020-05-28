# test_models.py
import unittest
import os
from app import create_app, db
from app.models import Campsite, Amenity, Comment


class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.campsite = {
        'name': '18 Rd',
        'description': 'Biking galore',
        'city': 'Fruita',
        'image_url': 'test',
        'state': 'CO',
        'driving_tips': 'Turn left then turn right',
        'lon': 123.2,
        'lat': 456.6
        }

        with self.app.app_context():
            db.create_all()


    def test_campsite_creation(self):
        campsite = Campsite(
            name = '18 Rd',
            description = 'Biking galore',
            city = 'Fruita',
            image_url = 'test',
            state = 'CO',
            driving_tips = 'Turn left then turn right',
            lon = 123.0,
            lat = 567.0
            )
        self.assertEqual(campsite.description, 'Biking galore')
        self.assertEqual(campsite.name, '18 Rd')
        self.assertEqual(campsite.city, 'Fruita')
        self.assertEqual(campsite.image_url, 'test')
        self.assertEqual(campsite.state, 'CO')
        self.assertEqual(campsite.driving_tips, 'Turn left then turn right')
        self.assertEqual(campsite.lon, 123.0)
        self.assertEqual(campsite.lat, 567.0)
        

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
