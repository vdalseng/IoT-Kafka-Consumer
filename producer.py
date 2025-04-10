from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

devices = ["sensor-1", "sensor-2", "sensor-3", "sensor-4", "sensor-5"]
cities = ["Oslo", "Berlin", "Paris", "Rome", "Copenhagen"]

while True:
    # Get the current timestamp
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate data for all cities simultaneously
    for city in cities:
        data = {
            "device_id": random.choice(devices),
            "location": city,
            "temperature": round(random.uniform(15.0, 30.0), 2),
            "motion": bool(random.getrandbits(1)),
            "timestamp": current_timestamp  # Use the current timestamp
        }
        producer.send("iot-sensors", data)
        print("Sent:", data)

    time.sleep(10)  # Wait 10 seconds before sending the next batch