import csv
from database.connect import drivers, cars


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row


def init_taxi_drivers():
   drivers.drop()
   cars.drop()

   for row in read_csv('C:/Users/User/Desktop/codcode/Python/pymongo-project/data/practice_data.csv'):
       car = {
           'license_id': row['CarLicense'],
           'brand': row['CarBrand'],
           'color': row['CarColor']
       }

       try:
           car_id = cars.insert_one(car).inserted_id
       except Exception as e:
           print(f"Error inserting driver: {e}")


       address = {
           'city': row['City'],
           'street': row['Street'],
           'state': row['State']
       }


       driver = {
           'passport': row['PassportNumber'],
           'first_name': row['FullName'].split(' ')[0],
           'last_name': row['FullName'].split(' ')[1],
           'car_id': car_id,
           'address': address
       }

       try:
           drivers.insert_one(driver).inserted_id
       except Exception as e:
           print(f"Error inserting driver: {e}")

init_taxi_drivers()

