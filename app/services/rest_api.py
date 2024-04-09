import random
import time
import sqlite3

# Setup Database
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_readings
             (timestamp DATETIME, temperature REAL, humidity REAL)''')
conn.commit()

def generate_sensor_data():
    return {
        'temperature': round(random.uniform(20, 30), 2),
        'humidity': round(random.uniform(30, 60), 2)
    }

def store_data(data):
    c.execute('INSERT INTO sensor_readings VALUES (datetime("now"), ?, ?)', 
              (data['temperature'], data['humidity']))
    conn.commit()

def analyze_data():
    c.execute('SELECT AVG(temperature), AVG(humidity) FROM sensor_readings')
    result = c.fetchone()
    print(f"Average Temperature: {result[0]}, Average Humidity: {result[1]}")

# Main loop
while True:
    sensor_data = generate_sensor_data()
    print(f"Generated data: {sensor_data}")
    store_data(sensor_data)
    analyze_data()
    time.sleep(5)  # Wait for 5 seconds

# Don't forget to close the database connection when done
conn.close()
