CREATE TABLE humidity (
    id SERIAL PRIMARY KEY,
    value REAL NOT NULL,
    plant_id VARCHAR(50) NOT NULL,
    sensor_id VARCHAR(50) NOT NULL
);

CREATE TABLE temperature (
    id SERIAL PRIMARY KEY,
    value REAL NOT NULL,
    plant_id VARCHAR(50) NOT NULL,
    sensor_id VARCHAR(50) NOT NULL
);

CREATE TABLE id_plant (
    id SERIAL PRIMARY KEY
);

CREATE TABLE id_sensors (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE anomaly (
    id SERIAL PRIMARY KEY,
    value_temp REAL NOT NULL,
    value_humidity REAL NOT NULL,
    plant_id VARCHAR(50) NOT NULL,
    sensor_id VARCHAR(50) NOT NULL
)