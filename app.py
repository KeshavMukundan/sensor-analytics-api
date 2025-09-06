from flask import Flask, request, jsonify
import redis
import json
from time import strftime


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route("/sensor_data", methods=["POST"])
def sensor_data():
    data = request.get_json()
    try:
        if data.get("sensor_id") == "living_room_temp":
            r.hset("set1", "living_room_temp", data.get("value"))
    except Exception as e:
        print(e)    
    data = json.dumps(data)

    r.lpush("Sensor:Analytics", data)
    
    r.ltrim("Sensor:Analytics", 0, 499)
        
    return jsonify(    {
        "status": "success",
        "message": "Sensor data ingested successfully."
    }

)    
    

@app.route("/sensor_analytics")
def sensor_analytics():
    
    avgCel = 0.0
    cachReading = r.llen("Sensor:Analytics")
    latestLivingTemp = None
    timestamp = strftime("%a, %d %b %Y %H:%M:%S")
    sum = 0
    count = 0
    
    for i in r.lrange("Sensor:Analytics", 0, -1):
        try:
            data = json.loads(i)
            if data["unit"] == "celsius":
                sum += float(data["value"])
                count += 1
        except Exception as e:
            print(e)
        
    if count > 0:
        avgCel = sum / count
        
    res1 = r.hget("set1", "living_room_temp")
    if res1 is not None:
        latestLivingTemp = float(res1)
            

    
        
    return jsonify({"average_temperature_celsius": avgCel,  
    "total_cached_readings": cachReading,       
    "latest_living_room_temp": latestLivingTemp,      
    "timestamp_of_analysis": timestamp})
        
            
            
            


if __name__ == "__main__":
    app.run(debug= True)

