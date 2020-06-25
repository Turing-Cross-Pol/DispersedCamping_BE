from app.models import Campsite, Amenity, Comment
from flask import request, jsonify, abort

class CommentsController:

	def __init__(self, data):
			self.data = data

	def create(self, campsite):
		title = str(self.data.get('title', ''))
		description = str(self.data.get('description', ''))
		rating = int(self.data.get('rating', 0))
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

	def index(self, campsite):
		comments = campsite.comments
		avg_rating = { 'average_rating': campsite.average_rating() }
		results = []
		for comment in comments:
			obj = {
				'id': comment.id,
				'title': comment.title,
				'description': comment.description,
				'rating': comment.rating,
				'date_created': comment.date_created
			}
			results.append(obj)
		response = jsonify(results, avg_rating)
		response.status_code = 200
		return response
