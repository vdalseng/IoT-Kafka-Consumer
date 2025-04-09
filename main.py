import subprocess
import sys

if __name__ == "__main__":
    try:
        # Use the Python executable from the current environment
        python_executable = sys.executable

        # Start producer.py
        producer_process = subprocess.Popen([python_executable, "producer.py"])
        print("Producer started.")

        # Start consumer.py
        consumer_process = subprocess.Popen([python_executable, "consumer.py"])
        print("Consumer started.")

        # Wait for both processes to complete (or run indefinitely)
        producer_process.wait()
        consumer_process.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        # Terminate both processes on exit
        producer_process.terminate()
        consumer_process.terminate()
        print("Both producer and consumer terminated.")