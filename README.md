<!-- PROJECT LOGO -->
<p align="center">
  <a>
   <img align="center" src="https://i.ibb.co/j66cs42/tent-location-icon.png" alt="tent-location-icon">
  </a>

<h3 align="center">WilderNests-BackEnd API </h3>

  <p align="center">
  WilderNests - A mobile app to find or post dispersed campsites in the United States. Giving adventurous campers peace of mind by providing community vetting in the backcountry. 
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
See a short youtube video of the Wildernest's application [here](https://www.youtube.com/watch?v=GVoGGwNy4Rk)

This Backend application acts as an API. The [Frontend](https://github.com/Turing-Cross-Pol/WilderNests_FE) lives in a separate GitHub repo. This application is currently deployed to [Heroku](https://dpcamping-be-stage.herokuapp.com/) and all endpoints are currently accessible. Please see the 'Usage' portion of the README for the primary endpoints.


### Built With

* Python 3.7
* Flask
* Postgresql
* SQLAlchemy
* Marshmallow
* Heroku
* Gunicorn
* Unittest


<!-- GETTING STARTED -->
## Getting Started

To clone and download a copy up of the backend API and running follow these simple steps.

### Prerequisites


```sh
Python 3.7
PostgreSQL 12.2
```


### Installation

1. Clone the repo
```sh
$ git clone git@github.com:Turing-Cross-Pol/DispersedCamping_BE.git
```
2. Set up and activate a virtual environment. Each time you enter this directory you will want to activate the virtual environment. 
```sh
$ python3 -m venv env
$ source env/bin/activate
```
3. Export the required files:
```sh
$ export FLASK_APP="run.py"
$ export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
$ export APP_SETTINGS="development"
$ export DATABASE_URL="postgresql:///dp-camping-be"
```
4. Install the required python and flask packages
```sh
$ pip install -r requirements.txt
```
5. Create a local database:
```
$ psql
$ create database dp-camping-be;
CREATE DATABASE
$ \q
```
6. Migrate the database:
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
7. You can spin up a local server in debug mode with:
```she
$ python run.py
```

Optional.
There is a seed file for your development/production database. To seed the database you can run:

```sh
$ python manage.py seed 
```

Migrate the heroku database with:
```sh
$ heroku run python manage.py db migrate
$ heroku run python manage.py db upgrade
```

To seed a heroku development database run:
```sh
$ heroku run python manage.py seed
```

<!-- USAGE EXAMPLES -->
## Usage

Currently Deployed to Heroku:
https://dpcamping-be-stage.herokuapp.com/

Primary Endpoints:
```sh
GET- /campsites/ (GET a collection of all of the available campsites)
```
```sh
Example Response for GET /campsites/
[
    {
        "amenities": [
            "fire",
            "hike",
            "bike"
        ],
        "average_rating": 4.0,
        "city": "Fruita",
        "description": "Biking galore",
        "driving_tips": "Take Interstate 70 west to Fruita (exit 19). Turn north onto Cherry Street and take the first right onto Aspen Avenue. Go through the roundabout and continue on Aspen to Maple Street. Take a left on Maple Street and then travel north. The street will turn into 17.5 road. Take a right on N.3 Road and then a left on 18 Road. Travel approximately 7 miles on 18 Road to the trailhead. Camping is allowed in designated campsites; A firepan and a portable toilet are required outside of the developed campground. Camping in designated sites costs $10.00/night. If you go just a little North these is free campings with limited amenities",
        "id": 1,
        "image_url": "https://cdn-files.apstatic.com/mtb/285374_medium_1554167980.jpg",
        "lat": 39.334,
        "lon": -108.704,
        "name": "18 Rd-North Fruita Desert",
        "state": "CO",
        "timestamp": "Thu, 04 Jun 2020 02:11:37 GMT"
    },
    {
        "amenities": [
            "fire",
            "hike"
        ],
        "average_rating": 5.0,
        "city": "Fruita",
        "description": "Hikers will be stunned. Views of the Black Ridge Canyons",
        "driving_tips": "Accessable via a number of routes",
        "id": 2,
        "image_url": "https://www.tripsavvy.com/thmb/7NDLY4l9IqOVrDivKfIb6uz5eu0=/2048x1366/filters:fill(auto,1)/mcinniscanyons-5c51e8ecc9e77c00016f38ed.jpg",
        "lat": 39.128,
        "lon": -108.886,
        "name": "McInnis Canyons Nation Conservation Area",
        "state": "CO",
        "timestamp": "Thu, 04 Jun 2020 02:11:37 GMT"
    },
 ]
```
```sh
POST- /campsites/ 
All attributes of a campsite should be included in the body of the request as form-data. Each should be a key/value pair.
Attributes of a campsite site currently include:
name, description, city, state, driving_toips, lat, lon, image_url

The amenities for a campsite are a separate resource in the database and are sent comma separated.
Ex fire, hike
```

```sh
GET /campsites/:ID (get a single campsite by ID)
Example response for GET /campsites/1
{
    "amenities": [
        "fire",
        "hike",
        "bike"
    ],
    "city": "Fruita",
    "description": "Biking galore",
    "driving_tips": "Take Interstate 70 west to Fruita (exit 19). Turn north onto Cherry Street and take the first right onto Aspen Avenue. Go through the roundabout and continue on Aspen to Maple Street. Take a left on Maple Street and then travel north. The street will turn into 17.5 road. Take a right on N.3 Road and then a left on 18 Road. Travel approximately 7 miles on 18 Road to the trailhead. Camping is allowed in designated campsites; A firepan and a portable toilet are required outside of the developed campground. Camping in designated sites costs $10.00/night. If you go just a little North these is free campings with limited amenities",
    "id": 1,
    "image_url": "https://cdn-files.apstatic.com/mtb/285374_medium_1554167980.jpg",
    "lat": 39.334,
    "lon": -108.704,
    "name": "18 Rd-North Fruita Desert",
    "state": "CO",
    "timestamp": "Thu, 04 Jun 2020 02:11:37 GMT"
}
```
```sh
DELETE and PUT requests are also supported for a single campsite
DELETE campsites/1
Returns:
{ "message": "campsite (CAMPSITE ID) deleted successfully". }

PUT campsites/1
All attributes to be updated should mirror a POST request. All attributes to be updated should be sent in key/value pairs as form data in the body of the request.
```

Comments:
```sh
GET-/campsites/:ID/comments (Gets all comments for a single campsite)
Example response:
[
    [
        {
            "description": "It gets hot during the day but the campsites are right off the trail so you can go back to camp and cool off.",
            "id": 1,
            "rating": "5",
            "title": "Best Biking in Western Colorado"
        },
        {
            "description": "I did not know scorpions swarmed. At our camp they do...",
            "id": 2,
            "rating": "3",
            "title": "Scorpions!"
        }
    ],
    {
        "average_rating": 4.0
    }
]
```

```sh 
POST /campsites/:ID/comments
All attributes for a post request should be sent via the body as form data.
Attributes of a comment are:
description, rating(int) and title
```

```sh
DELETE  /campsites/comments/:ID
Response:
{ "message": "comment {COMMENT ID} deleted successfully" }
```

```sh
PUT /campsites/comments/:ID
All attributes to be updated should mirror a POST request. All attributes to be updated should be sent in key/value pairs as form data in the body of the request.
```

## Future Extensions
1. User Authentication.
2. Ability to drop a pin on the map to start the process of posting a campsite.
3. Save your favorite campsites.
4. Recommendations-a machine learning algorithm that takes into account location and search history. 


<!-- CONTACT -->
## Contact

[Harry Borrelli-FE](https://github.com/hborrelli1)<br>
[Lili Manrique-FE](https://github.com/lmanriq)<br>
[Nathan Keller-BE](https://github.com/nkeller1)<br>
[Will Kunz-BE](https://github.com/willkunz13)<br>
 

Front End Project Link: [Wildernests](https://github.com/Turing-Cross-Pol/WilderNests_FE)




