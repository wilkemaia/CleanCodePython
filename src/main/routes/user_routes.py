from flask import Blueprint,jsonify,request

user_route_bp = Blueprint("user_route",__name__)
from src.Views.http_types.http_request import HttpRequest
from src.main.composer.user_creator_composer import user_creator_composer
from src.main.composer.user_finder_composer import user_finder_composer



@user_route_bp.route("/user",methods=['POST'])
def register_user():
     http_request = HttpRequest(body=request.json)
     user_creator  =  user_creator_composer()
     http_response  =  user_creator.handle_insert_new_user(http_request)
     
     return jsonify (http_response.body),http_response.status_code
   