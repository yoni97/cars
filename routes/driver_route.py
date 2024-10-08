from flask import Blueprint, jsonify, request
from repository.driver_repository import create_driver, get_all_drivers, get_driver_by_id, update_driver, delete_driver

driver_blueprint = Blueprint('driver_blueprint', __name__)

@driver_blueprint.route('/drivers', methods=['POST'])
def add_driver():
    data = request.get_json()
    if not data:
        return jsonify('No driver provided'), 400
    driver_id = create_driver(data)
    return jsonify({'driver_id':f'{driver_id}'}), 201

@driver_blueprint.route('/drivers', methods=['GET'])
def get_drivers():
    drivers = get_all_drivers()
    if not drivers:
        return jsonify('No drivers found'), 404
    return jsonify(drivers), 200

@driver_blueprint.route('/drivers<driver_id>', methods=['GET'])
def get_driver(id):
    driver = get_driver_by_id(id)
    if not driver:
        return jsonify({'error': 'No such driver exists.'}), 404
    return jsonify({'driver': driver}), 200

@driver_blueprint.route('/drivers<driver_id>', methods=['PUT'])
def update_driver(id):
    data = request.get_json()
    if not data:
        return jsonify('No driver provided'), 400
    res = update_driver(id, data)
    if not res:
        return jsonify('Failed to update driver'), 400
    return jsonify({'driver_id':f'{id}, updated successfully.'}), 200

@driver_blueprint.route('/drivers<driver_id>', methods=['DELETE'])
def delete_driver_by_id(id):
    res = delete_driver(id)
    if not res:
        return jsonify('Failed to delete driver'), 400
    return jsonify({'driver_id':f'{id}, deleted successfully.'}), 200





