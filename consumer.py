from kafka import KafkaConsumer
import json
from collections import defaultdict
import pandas as pd

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'iot-sensors',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Initialize stats for tracking device data
stats = defaultdict(list)

# CSV file to store data
csv_file = "plot-realtime/stream-output.csv"

# Initialize the CSV file with headers if it doesn't exist
df = pd.DataFrame(columns=["device_id", "location", "temperature", "motion", "timestamp"])
df.to_csv(csv_file, index=False, mode='w')

print("Listening for messages...")

# Consume messages
for msg in consumer:
    data = msg.value
    device = data["device_id"]
    temp = data["temperature"]

    # Update stats
    stats[device].append(temp)
    readings = stats[device]
    print(f"[{device}] Count: {len(readings)} | Min: {min(readings)} | Max: {max(readings)} | Avg: {sum(readings)/len(readings):.2f}")

    # Append the data to the CSV file
    df = pd.DataFrame([data])  # Convert message to DataFrame
    df.to_csv(csv_file, mode='a', header=False, index=False)  # Append to CSV