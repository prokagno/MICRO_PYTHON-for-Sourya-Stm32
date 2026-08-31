import time
import dht
from machine import Pin

# --- STM32 Hardware Configuration ---
# Set up the data pin. Replace 'PA8' with your actual STM32 pin name.
# Using Pin.PULL_UP acts as an internal backup pull-up resistor.
dht_pin = Pin('A7', Pin.IN, Pin.PULL_UP)

# Initialize the native MicroPython DHT11 driver
sensor = dht.DHT11(dht_pin)

print("DHT11 Sensor Initialized. Reading data...")

# --- Main Measurement Loop ---
while True:
    try:
        # CRITICAL: The DHT11 is a slow sensor. It requires at least 
        # a 1 to 2-second pause between readings, or it will throw an error.
        time.sleep(2)
        
        # Trigger a new hardware sensor transmission measurement
        sensor.measure()
        
        # Extract the calculated readings from the buffer
        temp_c = sensor.temperature()
        humidity = sensor.humidity()
        
        # Optional: Convert Celsius to Fahrenheit
        temp_f = (temp_c * 9/5) + 32
        
        # Print results neatly to the console logs
        print("-" * 40)
        print(f"LOG: Temperature = {temp_c}°C ({temp_f:.1f}°F)")
        print(f"LOG: Humidity    = {humidity}%")
        
    except OSError as e:
        # Catch reading transmission failures (e.g., loose wires, timeouts)
        print("LOG ERROR: Failed to read from DHT11 sensor. Checking connection...")
        
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        break
