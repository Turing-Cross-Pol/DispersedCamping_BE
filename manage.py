import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models
from app.models import Amenity, Campsite, Comment

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed():
    fire = Amenity(name='fire')
    horse = Amenity(name='horse')
    boat = Amenity(name='boat')
    fish = Amenity(name='fish')
    hike = Amenity(name='hike')
    bike = Amenity(name='bike')
    atv = Amenity(name='atv')

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
    campsite1.amenities.append(fire)
    campsite1.amenities.append(hike)
    campsite1.amenities.append(bike)
    comment1 = Comment(title = 'Best Biking in Western Colorado', description = 'It gets hot during the day but the campsites are right off the trail so you can go back to camp and cool off.', rating = "5")
    comment2 = Comment(title = 'Scorpians!', description = 'I did not know scorpians swarmed. At our camp they do...', rating = "3")
    campsite1.comments.append(comment1)
    campsite1.comments.append(comment2)

    campsite2 = Campsite(
        name = 'McInnis Canyons Nation Conservation Area',
        description = 'Hikers will be stunned. Views of the Black Ridge Canyons',
        city = 'Fruita',
        image_url = 'https://www.tripsavvy.com/thmb/7NDLY4l9IqOVrDivKfIb6uz5eu0=/2048x1366/filters:fill(auto,1)/mcinniscanyons-5c51e8ecc9e77c00016f38ed.jpg',
        state = 'CO',
        driving_tips = 'Accessable via a number of routes',
        lon = -108.886,
        lat = 39.128
        )
    campsite2.amenities.append(fire)
    campsite2.amenities.append(hike)
    comment3 = Comment(title = 'The Views!', description = 'The dispersed camping has eveything you need.', rating = "5")
    comment4 = Comment(title = 'The camping areas flood.', description = 'Do not go if there is rain in forecast.', rating = "5")
    campsite2.comments.append(comment3)
    campsite2.comments.append(comment4)

    campsite3 = Campsite(
        name = 'North Fruita Desert',
        description = '35 Campsites. Challenging environment. No water! Bring your own.',
        city = 'Fruita',
        image_url = 'https://www.gofruita.com/sites/default/files/imageattachments/gofruita/page/4889/28152210118_a327aa8051_h.jpg',
        state = 'CO',
        driving_tips = 'Take Interstate 70 west to Fruita (exit 19). Turn north onto Cherry Street and take the first right onto Aspen Avenue. Go through the roundabout and continue on Aspen to Maple Street. Take a left on Maple Street and then travel north. The street will turn into 17.5 road. Take a right on N.3 Road and then a left on 18 Road. Travel approximately 7 miles on 18 Road to the campground.',
        lon = -108.704,
        lat = 39.400
        )
    campsite3.amenities.append(fire)
    campsite3.amenities.append(hike)
    campsite3.amenities.append(bike)

    campsite4 = Campsite(
        name = 'Knowles Overlook',
        description = '7 Undevolped Sites. High clearance vehicle required to enter. Pit toliet.',
        city = 'Grand Junction',
        image_url = 'https://live.staticflickr.com/790/39454032510_5b66ff4702_b.jpg',
        state = 'CO',
        driving_tips = 'From Grand Junction travel west on I-70 and take exit 2 towards Rabbit Valley. Take a left over the interstate and travel straight into McInnis Canyons National Conservation Area. Take a right at the first intersection and a left at the second intersection. Stay on the main road for approximately 2.8 miles and take a left. The campground is approximately 1.3 miles further.',
        lon = -109.03,
        lat = 39.136
        )
    campsite4.amenities.append(fire)
    campsite4.amenities.append(hike)

    campsite5 = Campsite(
        name = 'Rabbit Valley',
        description = 'Great for motorcyles and ATVs. Dispersed camping only allowe at designated sites.',
        city = 'Grand Junction',
        image_url = 'https://www.riderplanet-usa.com/atv/trails/photo/370/50cc7275ac384baf8fd8077acab53e3e.jpg',
        state = 'CO',
        driving_tips = 'From Grand Junction travel west on Hwy 70 and take exit 2. Take a left over the Interstate and go straight into the McInnis Canyons National Conservation Area.',
        lon = -109.02,
        lat = 39.191
        )
    campsite5.amenities.append(fire)
    campsite5.amenities.append(hike)
    campsite5.amenities.append(bike)
    campsite5.amenities.append(atv)

    campsite6 = Campsite(
        name = 'Kokopellis Trail',
        description = 'Camping in designated spots only. 9 Small camping areas. Most campgrounds are free.',
        city = 'Moab',
        image_url = 'https://images.singletracks.com/blog/wp-content/uploads/2017/02/image46202-1200x900.jpg',
        state = 'UT',
        driving_tips = 'From Grand Junction, travel west on Interstate 70 about 15 miles. Take the Loma exit (exit 15), then travel west on gravel frontage road south of the interstate. The trailhead is on the left. Look for signs. Contact the Moab or Grand Junction Field Office for more information.',
        lon = -108.82744,
        lat = 39.177737
        )

    campsite6.amenities.append(fire)
    campsite6.amenities.append(hike)
    campsite6.amenities.append(bike)

    db.session.add(fire)
    db.session.add(horse)
    db.session.add(boat)
    db.session.add(fish)
    db.session.add(hike)
    db.session.add(bike)
    db.session.add(campsite1)
    db.session.add(campsite2)
    db.session.add(campsite3)
    db.session.add(campsite4)
    db.session.add(campsite5)
    db.session.add(campsite6)
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
