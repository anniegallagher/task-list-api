from app import db
from app.models.goal import Goal
from flask import Blueprint, jsonify, request, make_response, abort
from app.routes.task import validate_model
import requests
import os

bp = Blueprint("goal_bp", __name__, url_prefix="/goals")

@bp.route("", methods=["POST"])
def create_goal():
    try:
        request_body = request.get_json()
        new_goal = Goal.from_dict(request_body)

        db.session.add(new_goal)
        db.session.commit()

        goal_dict = new_goal.to_dict()

        return make_response(jsonify({
            "goal": goal_dict}), 201)
    
    except:
        abort(make_response({"details": "Invalid data"}, 400))