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
		from app.controllers.campsite_controller import CampsiteController
		campsite_controller = CampsiteController(request.data)
		campsite = Campsite.query.filter_by(id=id).first()
		if not campsite:
			abort(404)

		if request.method == 'DELETE':
			campsite.delete()
			return {
				"message": "campsite {} deleted successfully".format(campsite.id)
			}, 200

		elif request.method == 'PUT':
			return campsite_controller.update(campsite)
		else:
			return campsite_controller.show(campsite)
				
	@app.route('/campsites/', methods=['POST', 'GET'])
	def campsites():
		from app.controllers.campsite_controller import CampsiteController
		campsite_controller = CampsiteController(request.data)
		if request.method == "POST":
			return campsite_controller.create()
		else:
			return campsite_controller.index()


	@app.route('/campsites/<int:id>/comments', methods=['GET', 'POST'])
	def comments(id, **kwargs):
		from app.controllers.comments_controller import CommentsController
		comments_controller = CommentsController(request.data)
		campsite = Campsite.query.filter_by(id=id).first()
		if not campsite:
			abort(404)

		if request.method == 'POST':
			return comments_controller.create(campsite)

		else:
			return comments_controller.index(campsite)

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
