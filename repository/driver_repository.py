from bson import ObjectId
from database.connect import drivers


def create_driver(driver_data):
    driver = {
        'passport': driver_data['passport'],
        'first_name': driver_data['first_name'],
        'last_name': driver_data['last_name'],
        'car_id': driver_data['car_id'],
        'address': driver_data['address']
    }
    driver_id = drivers.insert_one(driver).inserted_id
    return str(driver_id)


def get_driver_by_name(name):
    driver = drivers.find_one({'name': name}, {'_id': 0, 'car_id':0})
    return driver if driver else None

def get_all_drivers():
    drivers_list = drivers.find({}, {'_id': 0 , 'car_id': 0})
    return list(drivers_list) if drivers_list else None

def get_driver_by_id(driver_id):
    return drivers.find_one({'_id': ObjectId(driver_id)}, {'_id': 0, 'car_id':0})

def update_driver(driver_id, driver):
    result = drivers.update_one({'_id': ObjectId(driver_id)}, {'$set': driver})
    return result.modified_count > 0

def delete_driver(driver_id):
    result = drivers.delete_one({'_id': ObjectId(driver_id)})
    return result.deleted_count > 0

# def create_driver(driver):
#     res = drivers.insert_one(driver)
#     return res.inserted_id









