import csv
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'academicmysql.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'kgp4805'
app.config['MYSQL_PASSWORD'] = 'Tatto@1996'
app.config['MYSQL_DB'] = 'kgp4805'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# Read customers from database
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # Get all users from MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM customer")
        customers = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        customer_list = []
        for customer in customers:
            customer_list.append({
                'id': customer['customerID'],
                'name': customer['name'],
                'phone': customer['phone'],
                'customerType': customer['customerType'],
            })
        
        return jsonify(customers=customer_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Add a new customer to the database
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        # Retrieve data from request payload
        customer_data = request.get_json()
        name = customer_data['name']
        phone = customer_data['phone']
        customerType = customer_data['customerType']

        # Generate a random customerID
        customerId = random.randint(100000, 999999)

        # Insert customer data into MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s)",
                       (customerId, name, phone, customerType))
        mysql.connection.commit()
        cursor.close()

        return jsonify(message='Customer added successfully'), 200

    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Read owners from database
@app.route('/owners', methods=['GET'])
def get_owners():
    try:
        # Get all users from MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM owner")
        owners = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        owner_list = []
        for owner in owners:
            owner_list.append({
                'ownerId': owner['Id'],
                'name': owner['name'],
                'ownerType': owner['ownerType']
            })
        
        return jsonify(owners=owner_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
def get_owners():
    try:
        # Get all users from MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM owner")
        owners = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        owner_list = []
        for owner in owners:
            owner_list.append({
                'ownerId': owner['Id'],
                'name': owner['name'],
                'ownerType': owner['ownerType']
            })
        
        return jsonify(owners=owner_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Read cars data from database
@app.route('/cars', methods=['GET'])
def get_cars():
    try:
        # Get all users from MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM car")
        cars = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        cars_list = []
        for car in cars:
            cars_list.append({
                'vehicleID': car['vehicleID'],
                'ownerId': car['ownerId'],
                'model': car['model'],
                'year': car['year'],
                'location': car['location'],
                'carType': car['carType'],
                'carCategory': car['carCategory'],
                'dailyRate': car['dailyRate'],
                'weeklyRate': car['weeklyRate']
            })
        
        return jsonify(cars=cars_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Add a new customer to the database
@app.route('/cars', methods=['POST'])
def add_car():
    try:
        # Retrieve data from request payload
        car_data = request.get_json()
        vehicleID = car_data['vehicleID']
        ownerId = car_data['ownerId']
        model = car_data['model']
        year = car_data['year']
        location = car_data['location']
        carType = car_data['carType']
        carCategory = car_data['carCategory']
        dailyRate = car_data['dailyRate']
        weeklyRate = car_data['weeklyRate']

        # Insert car data into MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO car VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)",
                       (vehicleID, ownerId, model, year, location, carType, carCategory, dailyRate, weeklyRate))
        mysql.connection.commit()
        cursor.close()

        return jsonify(message='Car added successfully'), 200

    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500

# Read rentals from database
@app.route('/rental', methods=['GET'])
def get_rentals():
    try:
        # Get all users from MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM rental")
        rentals = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        rental_list = []
        for rental in rentals:
            rental_list.append({
                'custID': rental['custID'],
                'carID': rental['carID'],
                'rentalStatus': rental['rentalStatus'],
                'rentalType': rental['rentalType'],
                'noOfDays': rental['noOfDays'],
                'noOfWeeks': rental['noOfWeeks'],
                'startDate': rental['startDate'],
                'endDate': '2023-05-05'
            })
        
        return jsonify(rentals=rental_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Add a new rental to the database
@app.route('/rental', methods=['POST'])
def add_rental():
    try:
        # Retrieve data from request payload
        rental_data = request.get_json()
        custID = rental_data['custID']
        carID = rental_data['carID']
        rentalStatus = rental_data['rentalStatus']
        rentalType = rental_data['rentalType']
        noOfDays = rental_data['noOfDays']
        noOfWeeks = rental_data['noOfWeeks']
        startDate = rental_data['startDate']

        # Insert rental data into MySQL database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO rental VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (custID, carID, rentalStatus, rentalType, noOfDays or None, noOfWeeks or None, startDate))
        mysql.connection.commit()
        cursor.close()

        return jsonify(message='Rental added successfully'), 200

    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
# Read available rental cars from database
@app.route('/availability', methods=['POST'])
def get_available_cars():
    try:

        # Retrieve data from request payload
        rental_available_data = request.get_json()
        carType = rental_available_data['carType']
        carCategory = rental_available_data['carCategory']
        startDate = rental_available_data['startDate']
        endDate = rental_available_data['endDate']

        cursor = mysql.connection.cursor()
        print(carType,carCategory,startDate,endDate)
        cursor.execute("SELECT c.* FROM Car c INNER JOIN Availability a ON c.vehicleID = a.carID LEFT JOIN Rental r ON c.vehicleID = r.carID WHERE c.carType = %s AND c.carCategory = %s AND a.startDate <= %s AND a.endDate >= %s AND r.rentalStatus IS NULL", (carType, carCategory, startDate, endDate))
        availableCars = cursor.fetchall()
        cursor.close()
        
        # Convert the result into a list of dictionaries
        cars_list = []
        for car in availableCars:
            cars_list.append({
                'vehicleID': car['vehicleID'],
                'ownerId': car['ownerId'],
                'model': car['model'],
                'year': car['year'],
                'location': car['location'],
                'carType': car['carType'],
                'carCategory': car['carCategory'],
                'dailyRate': car['dailyRate'],
                'weeklyRate': car['weeklyRate']
            })
        
        return jsonify(availableCars=cars_list), 200
    
    except Exception as e:
        # Handle error and return error response
        return jsonify(message=str(e)), 500
    
if __name__ == '__main__':
    app.run(debug=True)
