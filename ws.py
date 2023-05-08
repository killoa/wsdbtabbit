from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Create a function to fetch data from a specific table
def get_data_from_table(table_name):
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    
    data = cursor.fetchall()
    conn.close()
    
    return data

@app.route('/fact_ride', methods=['GET'])
def get_fact_ride_data():
    return jsonify(get_data_from_table('Fact_Ride'))

@app.route('/dim_passenger', methods=['GET'])
def get_dim_passenger_data():
    return jsonify(get_data_from_table('Dim_Passenger'))

@app.route('/dim_driver', methods=['GET'])
def get_dim_driver_data():
    return jsonify(get_data_from_table('Dim_Driver'))

@app.route('/dim_location', methods=['GET'])
def get_dim_location_data():
    return jsonify(get_data_from_table('Dim_Location'))

@app.route('/dim_passenger_rating', methods=['GET'])
def get_dim_passenger_rating_data():
    return jsonify(get_data_from_table('Dim_Passenger_Rating'))

@app.route('/dim_driver_rating', methods=['GET'])
def get_dim_driver_rating_data():
    return jsonify(get_data_from_table('Dim_Driver_Rating'))

if __name__ == '__main__':
    app.run(debug=True)
