# IoT-Kafka-Consumer

## Setup requirements
- Docker desktop

- Pentaho spoon enterprise edition

- Virtual environment


### Creating a virtual environment (venv)
For Windows: In your terminal, use **py -m venv .venv**

Activating the virtual environment: In your terminal, use **.venv\Scripts\activate**

Installing the dependencies for the project: In your terminal, use **pip install -r requirements.txt**


### Pentaho setup
The needed transformation files are included in the pentaho folder inside this project, load the two seperate transformations.
 
### How it works

#### 1. Two Transformations Involved

Inside the pentaho/ folder:

    IoT-Kafka-Transformation.ktr: Main entry point, consumes Kafka messages.

    get-data-from-stream.ktr: A sub-transformation that parses and processes each Kafka message.

#### 2. Main Transformation: IoT-Kafka-Transformation.ktr

    Contains a Kafka Consumer step

    Kafka settings like:

        localhost:9092 for broker

        Set the full path to get-data-from-stream.ktr

        iot-sensors as topic

        Consumes JSON sensor messages (from your Python producer)

Inside that Kafka step:

    There's a config option: "Transformation to run for each message"

    This points to get-data-from-stream.ktr — a sub-transformation

    Each Kafka message triggers this transformation once

Important: You must set the absolute path to get-data-from-stream.ktr in the Kafka step, or else Pentaho won’t find it.


#### 3. Sub-Transformation: get-data-from-stream.ktr

This does the actual message handling:

    JSON Input: Parses the incoming message (which is a JSON string)

    Extracts fields like:

        device_id, temperature, motion, location, timestamp

    Optionally processes them:

        Logging to console

        Writing to DB or CSV

        Computing statistics (min, max, avg, etc.)


### How to run

    Run docker-compose up -d (-d is optional, just for a detached terminal)

    Run main.py or just producer.py (main.py is to run both producer and consumer files if the Pentaho step fails, or just to check if the real time data is actually being consumed)
    
    Run IoT-Kafka-Transformation.ktr

    Let it generate data and save to the stream-output.csv file, stop the consumer transformation when satisfied with amount of samples.

    Open analytics transformation to view the csv file for analytics.