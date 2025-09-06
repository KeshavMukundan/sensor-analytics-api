# Sensor Analytics API

A simple Flask API for ingesting and analyzing simulated IoT sensor data.  
Stores sensor readings in Redis for fast caching and provides basic analytics like averages and latest values.

## Features
- Ingests simulated sensor data (temperature, humidity, etc.) through POST requests
- Caches data in Redis for low-latency retrieval
- Analytics endpoint for average temperature and latest readings
- Includes Python script to simulate sensor requests

## Built With
- Python (Flask)
- Redis
- Requests (for simulation)


## API Endpoints
- POST /sensor_data

  Example:


  ```
  {
    "sensor_id": "kitchen_temp",
    "value": 24.1,
    "unit": "celsius",
    "timestamp": "2025-07-22T14:35:15.678Z"
  }
  ```





- GET /sensor_analytics

  Example:
  
  ```
  {
    "average_temperature_celsius": 24.5,
    "total_cached_readings": 500,
    "latest_living_room_temp": 25.1,
    "timestamp_of_analysis": "Mon, 23 Sep 2025 10:30:45"
  
  }```
