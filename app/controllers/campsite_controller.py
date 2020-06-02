import pdb
from app.models import Campsite, Amenity, Comment
from flask import request, jsonify, abort

class CampsiteController:

	def __init__(self, data):
			self.data = data

	def create(self):
		name = str(self.data.get('name', ''))
		image_url = str(self.data.get('image_url', ''))
		city = str(self.data.get('city', ''))
		state = str(self.data.get('state', ''))
		description = str(self.data.get('description', ''))
		driving_tips = str(self.data.get('driving_tips', ''))
		lon = float(self.data.get('lon', 0))
		lat = float(self.data.get('lat', 0))
		amenities = str(self.data.get('amenities', '')).split(', ')
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
            'amenities': campsite.list_amenities()
            })
		response.status_code = 201
		return response

	def index(self):
		campsites = Campsite.get_all()
		results = []

		for campsite in campsites:
			obj = {
            'id': campsite.id,
            'name': campsite.name,
            'city': campsite.city,
            'state': campsite.state,
            'image_url': campsite.image_url,
            'description': campsite.description,
            'driving_tips': campsite.driving_tips,
            'lon': campsite.lon,
            'lat': campsite.lat,
            'timestamp': campsite.date_created,
            'amenities': campsite.list_amenities(),
            'average_rating': campsite.average_rating()
            }
			results.append(obj)
			response = jsonify(results)
			response.status_code = 200
			return response

	def update(self, campsite):
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
				'image_url': campsite.image_url,
				'description': campsite.description,
				'driving_tips': campsite.driving_tips,
				'lon': campsite.lon,
				'lat': campsite.lat
		})
		response.status_code = 200
		return response


	def show(self, campsite):
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
			'timestamp': campsite.date_created,
			'amenities': campsite.list_amenities()
		})
		response.status_code = 200
		return response

