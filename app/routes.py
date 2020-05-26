from webapp import app
from flask import jsonify
import pdb
from .models import Campsite, CampsiteSchema

campsite_schema = CampsiteSchema()

@app.route("/")
def hello_world():
	return "hello world"


@app.route("/api/campsites", methods=['GET'])
def campsite_details():
  campsites = Campsite.query.all()
  if not campsites:
    response = {
              'message': 'Ain\'t no campsites here'
               }
    return jsonify(response), 404
  result = campsite_schema.dumps(campsite).data
  response = {
            'data': result,
            'status_code' : 202
            }
  return jsonify(response)

