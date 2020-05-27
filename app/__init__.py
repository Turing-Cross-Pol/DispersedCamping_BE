# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
import pdb

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
	from app.models import Campsite
	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)


	@app.route('/campsites/', methods=['POST', 'GET'])
	def campsites():


		if request.method == "POST":
			name = str(request.data.get('name', ''))
			if name:
				campsite = Campsite(name=name)
				campsite.save()
				response = jsonify({
								'id': campsite.id,
								'name': campsite.name,
								})
				response.status_code = 201
			return response
		else:
			# GET
			campsites = Campsite.get_all()
			results = []

			for campsite in campsites:
				obj = {
						'id': campsite.id,
						'name': campsite.name,
						}
				results.append(obj)
				response = jsonify(results)
				response.status_code = 200
			return response

	return app
