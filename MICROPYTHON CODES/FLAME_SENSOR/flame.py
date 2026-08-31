import time
from machine import Pin

# --- STM32 Hardware Configuration ---
# Modify these pin names to match your physical wiring setup
FLAME_SENSOR = Pin('A7', Pin.IN)   # Connected to HW-072 DO pin
BUZZER = Pin('B0', Pin.OUT)         # Connected to active buzzer
ALERT_LIGHT = Pin('B1', Pin.OUT)    # Connected to LED/Light module

# Tracking variable to prevent console log flooding
# None = Init, 0 = Safe/No Flame, 1 = Fire Detected
last_state = None  

print("HW-072 Flame Detection System Active. Monitoring...")

try:
    while True:
        # READ SENSOR: Most HW-072 boards output a 0 (LOW) when a flame is 
        # detected and a 1 (HIGH) when the environment is safe.
        sensor_value = FLAME_SENSOR.value()
        
        if sensor_value == 0:
            # --- FLAME DETECTED STATE ---
            BUZZER.value(0)       # Turn buzzer ON
            ALERT_LIGHT.value(1)  # Turn light ON
            
            if last_state != 1:
                timestamp = time.ticks_ms() / 1000.0
                print(f"[{timestamp:.2f}s] ⚠️ ALERT: Fire/Flame Detected!")
                last_state = 1  # Update local state
                
        else:
            # --- NO FLAME STATE ---
            BUZZER.value(1)       # Turn buzzer OFF
            ALERT_LIGHT.value(0)  # Turn light OFF
            
            if last_state != 0:
                timestamp = time.ticks_ms() / 1000.0
                print(f"[{timestamp:.2f}s] LOG: No flame detected. Status: Safe.")
                last_state = 0  # Update local state

        # Check the sensor status every 100 milliseconds
        time.sleep_ms(100)

except KeyboardInterrupt:
    # Emergency fallback shutdown of safety peripherals on script stop
    BUZZER.value(0)
    ALERT_LIGHT.value(0)
    print("\nMonitoring system deactivated by user.")
