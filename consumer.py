from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

stats = defaultdict(list)

for msg in consumer:
    data = msg.value
    device = data["device_id"]
    temp = data["temperature"]
    
    stats[device].append(temp)
    
    readings = stats[device]
    print(f"[{device}] Count: {len(readings)} | Min: {min(readings)} | Max: {max(readings)} | Avg: {sum(readings)/len(readings):.2f}")
