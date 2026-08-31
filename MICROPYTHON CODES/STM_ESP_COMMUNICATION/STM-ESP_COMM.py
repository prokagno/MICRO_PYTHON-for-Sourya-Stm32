from pyb import UART

# Initialize UART1 on PA9 (TX) and PA10 (RX) at 115200 baud
# Note: In MicroPython for STM32, UART(1) automatically maps to PA9 and PA10
uart = UART(1, 115200)

print("STM32 UART1 Receiver Ready...")

while True:
    # Check if there is incoming data in the buffer
    if uart.any():
        # Read the available data
        command = uart.read()
        
        try:
            # Decode bytes to string
            command_str = command.decode('utf-8').strip()
            
            # Construct the response string
            response_str = f"{command_str} received from esp32\n"
            
            # Send the response back to ESP32
            uart.write(response_str.encode('utf-8'))
            
            # Optional: Print to STM32 REPL for local debugging
            print(f"Processed: {command_str}")
            
        except Exception as e:
            print("Error decoding data:", e)
