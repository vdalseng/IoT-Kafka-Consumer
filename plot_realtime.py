import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta

# CSV file to read data from
csv_file = "plot-realtime/stream-output.csv"

# Function to update the plot
def update(frame):
    plt.cla()  # Clear the current axes
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Ensure there is data to plot
        if df.empty:
            return

        # Parse the timestamp column
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        df = df.dropna(subset=["timestamp"])  # Drop rows with invalid timestamps

        # Filter data to only include the past minute
        two_minute_ago = datetime.now() - timedelta(minutes=2)
        df = df[df["timestamp"] >= two_minute_ago]

        # Sort the data by timestamp
        df = df.sort_values(by="timestamp")

        # Plot temperature over time for each city
        for city, group in df.groupby("location"):
            plt.plot(group["timestamp"], group["temperature"], label=city)

        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.title("Real-Time IoT Sensor Data (Past Minute)")
        plt.legend(loc="upper left")
        plt.xticks(rotation=45)
    except Exception as e:
        print(f"Error reading or plotting data: {e}")

# Set up the plot
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=1000)  # Update every second

plt.show()