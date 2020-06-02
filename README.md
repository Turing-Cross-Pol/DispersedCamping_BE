<!-- PROJECT LOGO -->
<p align="center">
  <a>
   <img align="center" src="https://i.ibb.co/j66cs42/tent-location-icon.png" alt="tent-location-icon">
  </a>

<h3 align="center">WilderNests-BackEnd API </h3>

  <p align="center">
  WilderNests - A mobile app to find or post dispersed campsites in the United States. Giving adventurous campers peace of mind by providing community vetting in the back country.
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

This Backend application acts as an API. The [Frontend](https://github.com/Turing-Cross-Pol/WilderNests_FE) lives in a seperate github repo. This application is currently deployed to [Heroku](https://dpcamping-be-stage.herokuapp.com/) and all endpoints are currently accessable. Please see the 'Usage' portion of the README for the primary endpoints.


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

To get a local copy up of the backend api and running follow these simple steps.

### Prerequisites


```sh
Python 3.7
PostgreSQL 12.2
```


### Installation

1. Clone the repo
```sh
git clone git@github.com:Turing-Cross-Pol/DispersedCamping_BE.git
```
2. Set up and activate a virtual environment. Each time you enter this directory you will want to active the virtual environment. 
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
# create database dp-camping-be;
CREATE DATABASE
# \q
```
6. Migrate the database:
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
7. You can spin up a local server in debug mode with:
```she
python run.py
```

Optional.
There is a seed file for your development/production database. To seed the database you can run:

```sh
$ python manage.py seed 
```

Migrate the heroku database with:
```sh
heroku run python manage db migrate
heroku run python manage db upgrade
```

To seed a heroku development database run:
```sh
heroku run python manage.py seed
```

<!-- USAGE EXAMPLES -->
## Usage

Currently Deployed to Heroku:
https://dpcamping-be-stage.herokuapp.com/

Primary Endpoints:
```sh
GET-POST /campsites/ (get/post to the collection of campsites)
GET /campsites/:ID/ (get a single campsite by ID)
GET-POST /campsites/:ID/comments (get all comments for a single campsite)
```

There are also PUT and DELETE endpoints for each resource. 


<!-- CONTACT -->
## Contact

[Harry Borrelli FE](https://github.com/hborrelli1)<br>
[Lili Manrique FE](https://github.com/lmanriq)<br>
[Nathan Keller BE](https://github.com/nkeller1)<br>
[Will Kunz BE](https://github.com/willkunz13)<br>
 

Front End Project Link: [Wildernests](https://github.com/Turing-Cross-Pol/WilderNests_FE)




