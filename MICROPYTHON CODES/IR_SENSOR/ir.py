import time
from machine import Pin

# --- STM32 Hardware Configuration ---
# Replace 'PA3' and 'PA4' with your actual STM32 pin names
IR_SENSOR = Pin('A0', Pin.IN)          # IR Sensor signal line
BOARD_LED = Pin('A7', Pin.OUT)         # LED control pin

# Tracking variable to remember the last state (prevents log flooding)
# None = System start, 0 = Not Detected, 1 = Detected
last_state = None  

print("System Initialized. Monitoring IR Sensor...")

# --- Main Logic Loop ---
try:
    while True:
        # Read the raw sensor value. 
        # Most IR sensors output 1 (HIGH) for empty space, and 0 (LOW) for an obstacle.
        sensor_value = IR_SENSOR.value()
        
        if sensor_value == 0:
            # --- OBJECT DETECTED STATE ---
            BOARD_LED.value(1)  # Turn the LED OFF
            
            if last_state != 1:
                timestamp = time.ticks_ms() / 1000.0
                print(f"[{timestamp:.2f}s] LOG: Object Detected!")
                last_state = 1  # Update state
                
        else:
            # --- OBJECT NOT DETECTED STATE ---
            BOARD_LED.value(0)  # Keep the LED ON continuously
            
            if last_state != 0:
                timestamp = time.ticks_ms() / 1000.0
                print(f"[{timestamp:.2f}s] LOG: Object Not Detected")
                last_state = 0  # Update state

        # Tiny delay to prevent maxing out the STM32 core processing speed
        time.sleep_ms(50)

except KeyboardInterrupt:
    BOARD_LED.value(0)  # Safe shutdown
    print("\nProgram stopped by user.")
