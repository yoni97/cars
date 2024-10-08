from bson import ObjectId
from database.connect import cars


def create_car(driver_data):
    driver = {
        'passport': driver_data['passport'],
        'first_name': driver_data['first_name'],
        'last_name': driver_data['last_name'],
        'car_id': driver_data['car_id'],
        'address': driver_data['address']
    }
    car_id = cars.insert_one(driver).inserted_id
    return str(car_id)


def get_driver_by_name(name):
    car = cars.find_one({'name': name}, {'_id': 0, 'car_id':0})
    return cars if cars else None

def get_all_cars():
    cars_list = cars.find({}, {'_id': 0 , 'car_id': 0})
    return list(cars_list) if cars_list else None

def get_car_by_id(car_id):
    return cars.find_one({'_id': ObjectId(car_id)}, {'_id': 0, 'car_id':0})

def update_car(car_id, car):
    result = cars.update_one({'_id': ObjectId(car_id)}, {'$set': car})
    return result.modified_count > 0

def delete_car(car_id):
    result = cars.delete_one({'_id': ObjectId(car_id)})
    return result.deleted_count > 0

# def create_driver(driver):
#     res = drivers.insert_one(driver)
#     return res.inserted_id
