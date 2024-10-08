from flask import Blueprint, jsonify, request
from repository.car_repository import create_car, get_all_cars, get_car_by_id, update_car, delete_car

car_blueprint = Blueprint('car_blueprint', __name__)

@car_blueprint.route('/cars', methods=['POST'])
def add_car():
    car_data = request.json
    car_id = create_car(car_data)
    return jsonify({"car_id": car_id}), 201

@car_blueprint.route('/cars', methods=['GET'])
def get_cars():
    cars = get_all_cars()
    return jsonify(cars), 200

@car_blueprint.route('/cars<car_id>', methods=['GET'])
def get_car(car_id):
    car = get_car_by_id(car_id)
    return jsonify(car), 200

@car_blueprint.route('/cars<car_id>', methods=['PUT'])
def edit_car(car_id):
    car_data = request.json
    update_car(car_id, car_data)
    return jsonify({"msg": "Car updated"}), 200

@car_blueprint.route('/cars<car_id>', methods=['DELETE'])
def remove_car(car_id):
    delete_car(car_id)
    return jsonify({"msg": "Car deleted"}), 200

