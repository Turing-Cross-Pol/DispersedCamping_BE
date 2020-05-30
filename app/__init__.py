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
	from app.models import Campsite, Comment
	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	@app.route('/campsites/<int:id>', methods=['GET', 'PUT', 'DELETE'])
	def campsite_manipulation(id, **kwargs):
		campsite = Campsite.query.filter_by(id=id).first()
		if not campsite:
			abort(404)

		if request.method == 'DELETE':
			campsite.delete()
			return {
				"message": "campsite {} deleted successfully".format(campsite.id)
			}, 200

		elif request.method == 'PUT':
			name = str(request.data.get('name', campsite.name))
			image_url = str(request.data.get('image_url', campsite.image_url))
			city = str(request.data.get('city', campsite.city))
			state = str(request.data.get('state', campsite.state))
			description = str(request.data.get('description', campsite.description))
			driving_tips = str(request.data.get('driving_tips', campsite.driving_tips))
			lon = float(request.data.get('lon', campsite.lon))
			lat = float(request.data.get('lat', campsite.lat))
			amenities = str(request.data.get('amenities', '')).split(', ')
			campsite.name = name
			campsite.image_url = image_url
			campsite.city = city
			campsite.state = state
			campsite.description = description
			campsite.driving_tips = driving_tips
			campsite.lon = lon
			campsite.lat = lat
			campsite.set_amenities(amenities)
			campsite.save()
			response = jsonify({
            'id': campsite.id,
            'name': campsite.name,
            'city': campsite.city,
            'state': campsite.state,
            'description': campsite.description,
            'driving_tips': campsite.driving_tips,
            'lon': campsite.lon,
            'lat': campsite.lat
      })	
			response.status_code = 200
			return response
		else:
				# GET
				response = jsonify({
						'id': campsite.id,
            'name': campsite.name,
            'city': campsite.city,
            'state': campsite.state,
            'description': campsite.description,
            'driving_tips': campsite.driving_tips,
            'lon': campsite.lon,
            'lat': campsite.lat,
						'amenities': str(campsite.list_amenities())
      	})
				response.status_code = 200
				return response


	@app.route('/campsites/', methods=['POST', 'GET'])
	def campsites():
		from app.models import Amenity
		if request.method == "POST":
			name = str(request.data.get('name', ''))
			image_url = str(request.data.get('image_url', ''))
			city = str(request.data.get('city', ''))
			state = str(request.data.get('state', ''))
			description = str(request.data.get('description', ''))
			driving_tips = str(request.data.get('driving_tips', ''))
			lon = float(request.data.get('lon', 0))
			lat = float(request.data.get('lat', 0))
			amenities = str(request.data.get('amenities', '')).split(', ')
			campsite = Campsite(name=name, image_url=image_url, city=city, state=state, description=description, driving_tips=driving_tips, lon=lon, lat=lat)
			campsite.set_amenities(amenities)
			campsite.save()
			response = jsonify({
						'id': campsite.id,
						'name': campsite.name,
            'image_url': campsite.image_url,
            'city': campsite.city,
            'state': campsite.state,
            'description': campsite.description,
            'driving_tips': campsite.driving_tips,
            'lon': campsite.lon,
            'lat': campsite.lat,
						'amenities': str(campsite.list_amenities())
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
						'city': campsite.city,
						'state': campsite.state,
						'description': campsite.description,
						'driving_tips': campsite.driving_tips,
						'lon': campsite.lon,
						'lat': campsite.lat,
						'amenities': str(campsite.list_amenities())
						}
				results.append(obj)
			response = jsonify(results)
			response.status_code = 200
			return response

	@app.route('/campsites/<int:id>/comments', methods=['GET', 'POST'])
	def comments(id, **kwargs):
		campsite = Campsite.query.filter_by(id=id).first()
		if not campsite:
			abort(404)

		if request.method == 'POST':
			title = str(request.data.get('title', ''))
			description = str(request.data.get('description', ''))
			rating = int(request.data.get('rating', 0))
			comment = Comment(title=title, description=description, rating=rating, campsite_id=campsite.id)
			campsite.comments.append(comment)
			campsite.save()
			comment.save()				
			response = jsonify({
				'id': comment.id,
				'title': comment.title,
				'description': comment.description,
				'rating': comment.rating
			})
			response.status_code = 201
			return response

		else:
			comments = campsite.comments
			results = []	
			for comment in comments:
				obj = {
					'id': comment.id,
					'title': comment.title,
					'description': comment.description,
					'rating': comment.description
				}
				results.append(obj)
			response = jsonify(results)
			response.status_code = 200
			return response

	@app.route('/campsites/<int:camp_id>/comments/<int:comment_id>', methods=['DELETE'])
	def destroy_comment(camp_id, comment_id, **kwargs):
		campsite = Campsite.query.filter_by(id=camp_id).first()
		comment = Comment.query.filter_by(id=comment_id).first() 
		if not campsite or not comment:
			abort(404)
		comment.delete()
		return  {
       "message": "comment {} deleted successfully".format(comment.id)
		}, 200


	return app
