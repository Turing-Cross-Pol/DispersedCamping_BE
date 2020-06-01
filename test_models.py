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
        comment1 = Comment(title = 'Best Biking in Western Colorado', description = 'It gets hot during the day but the campsites are right off the trail so you can go back to camp and cool off.', rating = "5")
        comment2 = Comment(title = 'Scorpians!', description = 'I did not know scorpians swarmed. At our camp they do...', rating = "3")
        campsite.comments.append(comment1)
        campsite.comments.append(comment2)
        fire = Amenity(name='fire')
        hike = Amenity(name='hike')
        campsite.amenities.append(fire)
        campsite.amenities.append(hike)
        self.assertEqual(campsite.description, 'Biking galore')
        self.assertEqual(campsite.name, '18 Rd')
        self.assertEqual(campsite.city, 'Fruita')
        self.assertEqual(campsite.image_url, 'test')
        self.assertEqual(campsite.state, 'CO')
        self.assertEqual(campsite.driving_tips, 'Turn left then turn right')
        self.assertEqual(campsite.lon, 123.0)
        self.assertEqual(campsite.lat, 567.0)
        self.assertEqual(campsite.comments, [comment1, comment2])
        self.assertEqual(campsite.amenities, [fire, hike])



    def test_average_rating(self):
        campsite1 = Campsite(
            name = '18 Rd-North Fruita Desert',
            description = 'Biking galore',
            city = 'Fruita',
            image_url = 'https://cdn-files.apstatic.com/mtb/285374_medium_1554167980.jpg',
            state = 'CO',
            driving_tips = 'Take Interstate 70 west to Fruita (exit 19). Turn north onto Cherry Street and take the first right onto Aspen Avenue. Go through the roundabout and continue on Aspen to Maple Street. Take a left on Maple Street and then travel north. The street will turn into 17.5 road. Take a right on N.3 Road and then a left on 18 Road. Travel approximately 7 miles on 18 Road to the trailhead. Camping is allowed in designated campsites; A firepan and a portable toilet are required outside of the developed campground. Camping in designated sites costs $10.00/night. If you go just a little North these is free campings with limited amenities',
            lon = -108.704,
            lat = 39.334
            )
        comment1 = Comment(title = 'Best Biking in Western Colorado', description = 'It gets hot during the day but the campsites are right off the trail so you can go back to camp and cool off.', rating = "5")
        comment2 = Comment(title = 'Scorpians!', description = 'I did not know scorpians swarmed. At our camp they do...', rating = "3")
        campsite1.comments.append(comment1)
        campsite1.comments.append(comment2)
        self.assertEqual(campsite1.average_rating(), 4)

    def test_list_amenities(self):
        campsite1 = Campsite(
            name = '18 Rd-North Fruita Desert',
            description = 'Biking galore',
            city = 'Fruita',
            image_url = 'https://cdn-files.apstatic.com/mtb/285374_medium_1554167980.jpg',
            state = 'CO',
            driving_tips = 'Take Interstate 70 west to Fruita (exit 19). Turn north onto Cherry Street and take the first right onto Aspen Avenue. Go through the roundabout and continue on Aspen to Maple Street. Take a left on Maple Street and then travel north. The street will turn into 17.5 road. Take a right on N.3 Road and then a left on 18 Road. Travel approximately 7 miles on 18 Road to the trailhead. Camping is allowed in designated campsites; A firepan and a portable toilet are required outside of the developed campground. Camping in designated sites costs $10.00/night. If you go just a little North these is free campings with limited amenities',
            lon = -108.704,
            lat = 39.334
            )
        fire = Amenity(name='fire')
        hike = Amenity(name='hike')
        campsite1.amenities.append(fire)
        campsite1.amenities.append(hike)
        self.assertEqual(campsite1.list_amenities(), ['fire', 'hike'])

    def tearDown(self):
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
