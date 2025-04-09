from kafka import KafkaProducer
import json
import time
import random
from faker import Faker

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

devices = ["sensor-1", "sensor-2", "sensor-3"]

while True:
    data = {
        "device_id": random.choice(devices),
        "location": fake.city(),
        "temperature": round(random.uniform(15.0, 30.0), 2),
        "motion": bool(random.getrandbits(1)),
        # "timestamp": fake.iso8601()
    }
    producer.send("iot-sensors", data)
    print("Sent:", data)
    time.sleep(1)
