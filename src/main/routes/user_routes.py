from flask import Blueprint,jsonify

user_route_bp = Blueprint("user_route",__name__)

@user_route_bp.route("/user",methods=['POST'])
def register_user():
     return jsonify ({"rota":"rota de cadastro"}),200
   