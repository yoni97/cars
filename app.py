from flask import Flask

from repository.csv_repository import init_taxi_drivers
from routes.car_route import car_blueprint
from routes.driver_route import driver_blueprint



app = Flask(__name__)
app.register_blueprint(car_blueprint)
app.register_blueprint(driver_blueprint)

f = init_taxi_drivers()

if __name__ == '__main__':
    f
    app.run(debug=True)