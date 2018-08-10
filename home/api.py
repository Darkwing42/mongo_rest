from home.mongo_rest import app, db
from flask import Blueprint, request, jsonify
import uuid
import logging, datetime


home_api = Blueprint('home_api', __name__)

@home_api.route("/home/", methods=["GET", "POST"])
def all_Homes():
	#response
	response_object = {
		"status": "success"
	}

	if request.method == "POST":
		logging.debug("HOME_API ENDPOINT HIT: {}".format(request.method))
		
		data = request.get_json()
		logging.info(data)
		home = db.Home()
		home.section_name = data['section_name']
		for url in data['urls']:
			home.urls.append(url)
	
		try:
			home.validate()
		except StructureError as e:
			response_object['status'] = "error"
			response_object['error'] = e
			return jsonify(response_object)
		
		home.save()
	else:
		home = db.Home.find()	
		response_object['homes'] = home 
		
		return jsonify(response_object)

@home_api.route('/home/<id>')
def get_Home(id):
	
