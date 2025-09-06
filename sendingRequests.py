import requests
import random 
from time import strftime, time


choices = ["kitchen_temp", "living_room_temp", "hallway_humidity, temp_1"]
value_choices = [24.1, 25.0, 25.1, 55.2, 22.2]
unit_choices = ["percent", "celsius", "fahrenheit"]


start_time = time()
num_requests = 1000

for _ in range(num_requests):
    
    sensor_id = random.choice(choices)
    value = random.choice(value_choices)
    unit = random.choice(unit_choices)
    timestamp = strftime("%a, %d %b %Y %H:%M:%S")
    
    data = {
    "sensor_id": sensor_id,
    "value": value,
    "unit": unit,
    "timestamp": timestamp
    }

    link = requests.post("http://localhost:5000/sensor_data", data= data)

end_time = time()

duration = end_time - start_time
requests_per_second = num_requests / duration

print(requests_per_second)



