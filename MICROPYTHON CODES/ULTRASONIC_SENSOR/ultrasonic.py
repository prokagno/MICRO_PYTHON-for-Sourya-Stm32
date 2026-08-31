import time
from machine import Pin, time_pulse_us

# --- STM32 Hardware Configuration ---
# Replace 'PA5' and 'PA6' with your actual STM32 pin names
TRIG = Pin('A0', Pin.OUT)  # Trigger pin (Outputs the pulse)
ECHO = Pin('A7', Pin.IN)   # Echo pin (Reads the return pulse)

# Ensure trigger starts low
TRIG.value(0)
time.sleep_ms(2)

print("Ultrasonic Sensor Initialized. Reading distance...")

def get_distance():
    """Sends a pulse and calculates the distance in centimeters."""
    # 1. Send a precise 10-microsecond high pulse to trigger the sensor
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)
    
    # 2. Measure the duration of the incoming high pulse on the Echo pin
    # time_pulse_us returns the time in microseconds, or -1/-2 on timeout
    duration_us = time_pulse_us(ECHO, 1, 30000) # 30ms timeout (~5 meters max)
    
    if duration_us < 0:
        return None  # Out of range or read error
        
    # 3. Calculate distance in cm
    # Speed of sound is ~0.0343 cm per microsecond. 
    # Divide by 2 because the wave travels to the object and back.
    distance_cm = (duration_us * 0.0343) / 2
    return round(distance_cm, 2)

# --- Main Measurement Loop ---
try:
    while True:
        distance = get_distance()
        
        # Print logs based on the sensor reading
        if distance is not None:
            print(f"LOG: Distance = {distance} cm")
        else:
            print("LOG: Out of range / No object detected")
            
        # Wait 500ms before the next reading to avoid overlapping echoes
        time.sleep_ms(500)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user.")
