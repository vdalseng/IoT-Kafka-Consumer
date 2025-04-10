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

        # Start plot_realtime.py
        plot_process = subprocess.Popen([python_executable, "plot_realtime.py"])
        print("Plotting started.")

        # Wait for all processes to complete (or run indefinitely)
        producer_process.wait()
        consumer_process.wait()
        plot_process.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        # Terminate all processes on exit
        producer_process.terminate()
        consumer_process.terminate()
        plot_process.terminate()
        print("All processes terminated.")