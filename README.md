<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">WilderNests-BackEnd API</h3>

<p align="center">
WilderNests - A mobile app to find or post dispersed campsites in the United States. Giving adventurous campers peace of mind by providing community vetting in the back country.
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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

<!-- USAGE EXAMPLES -->
## Usage

There is a seed file for your development database. To seed the database you can run:

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


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/github_username/repo/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo](https://github.com/github_username/repo)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()



