from machine import UART, Pin, PWM
import time


# ============================================================
# UART1 - ESP32 COMMUNICATION
# ============================================================

# STM32H563 MicroPython build uses the predefined UART1 pins.
#
# UART1:
# PA9  -> TX
# PA10 -> RX
#
# ESP32 TX must connect to STM32 PA10
# ESP32 RX must connect to STM32 PA9

uart = UART(1, 115200)

print()
print("========================================")
print("   STM32H563 CAR CONTROLLER")
print("========================================")
print("UART1 : 115200 baud")
print("TX    : PA9")
print("RX    : PA10")
print("========================================")


# ============================================================
# MOTOR DRIVER
# ============================================================

# ENA / ENB
# These are PWM pins.

ENA = PWM(Pin('A6'))
ENB = PWM(Pin('A7'))

# PWM frequency
ENA.freq(1000)
ENB.freq(1000)


# ============================================================
# MOTOR DIRECTION PINS
# ============================================================

# LEFT MOTOR
LEFT_IN1 = Pin('B0', Pin.OUT)
LEFT_IN2 = Pin('B1', Pin.OUT)

# RIGHT MOTOR
RIGHT_IN1 = Pin('C0', Pin.OUT)
RIGHT_IN2 = Pin('C1', Pin.OUT)


# ============================================================
# MOTOR SPEED
# ============================================================

# duty_u16 range:
#
# 0     = 0%
# 32768 = 50%
# 65535 = 100%
#
# ------------------------------------------------------------
# STRAIGHT SPEED
# ------------------------------------------------------------

STRAIGHT_SPEED = 60000
# Approximately 91.6%


# ------------------------------------------------------------
# TURNING SPEED
# ------------------------------------------------------------

TURN_SPEED = 64000
# Approximately 95.0%


# ------------------------------------------------------------
# BACKWARD SPEED
# ------------------------------------------------------------

BACKWARD_SPEED = 50000
# Approximately 76.3%


# ============================================================
# PWM SPEED FUNCTION
# ============================================================

def set_speed(speed):

    if speed < 0:
        speed = 0

    if speed > 65535:
        speed = 65535

    ENA.duty_u16(speed)
    ENB.duty_u16(speed)


# ============================================================
# STOP CAR
# ============================================================

def stop_car():

    # Stop PWM
    ENA.duty_u16(0)
    ENB.duty_u16(0)

    # Stop left motor
    LEFT_IN1.value(0)
    LEFT_IN2.value(0)

    # Stop right motor
    RIGHT_IN1.value(0)
    RIGHT_IN2.value(0)

    print("ACTION -> STOP")


# ============================================================
# FORWARD
# ============================================================

def move_forward():

    # Left motor forward
    LEFT_IN1.value(1)
    LEFT_IN2.value(0)

    # Right motor forward
    RIGHT_IN1.value(1)
    RIGHT_IN2.value(0)

    # STRAIGHT SPEED
    set_speed(STRAIGHT_SPEED)

    print(
        "ACTION -> FORWARD | SPEED =",
        STRAIGHT_SPEED
    )


# ============================================================
# BACKWARD
# ============================================================

def move_backward():

    # Left motor backward
    LEFT_IN1.value(0)
    LEFT_IN2.value(1)

    # Right motor backward
    RIGHT_IN1.value(0)
    RIGHT_IN2.value(1)

    # BACKWARD SPEED
    set_speed(BACKWARD_SPEED)

    print(
        "ACTION -> BACKWARD | SPEED =",
        BACKWARD_SPEED
    )


# ============================================================
# TURN LEFT
# ============================================================

def turn_left():

    # Left motor backward
    LEFT_IN1.value(0)
    LEFT_IN2.value(1)

    # Right motor forward
    RIGHT_IN1.value(1)
    RIGHT_IN2.value(0)

    # TURN SPEED
    set_speed(TURN_SPEED)

    print(
        "ACTION -> LEFT | SPEED =",
        TURN_SPEED
    )


# ============================================================
# TURN RIGHT
# ============================================================

def turn_right():

    # Left motor forward
    LEFT_IN1.value(1)
    LEFT_IN2.value(0)

    # Right motor backward
    RIGHT_IN1.value(0)
    RIGHT_IN2.value(1)

    # TURN SPEED
    set_speed(TURN_SPEED)

    print(
        "ACTION -> RIGHT | SPEED =",
        TURN_SPEED
    )


# ============================================================
# SAFE STARTUP
# ============================================================

stop_car()

print("CAR READY")
print("Waiting for commands...")
print()
print("F = Forward")
print("B = Backward")
print("L = Left")
print("R = Right")
print("S = Stop")
print()
print("STRAIGHT SPEED :", STRAIGHT_SPEED)
print("TURN SPEED     :", TURN_SPEED)
print("BACKWARD SPEED :", BACKWARD_SPEED)
print()


# ============================================================
# MAIN CONTROL LOOP
# ============================================================

try:

    while True:

        # Check if ESP32 sent something
        if uart.any():

            data = uart.read(1)

            if data:

                try:
                    command = data.decode('utf-8').upper()

                except:
                    command = ''

                if command:

                    print(
                        "UART COMMAND ->",
                        repr(command)
                    )


                    # ----------------------------------------
                    # FORWARD
                    # ----------------------------------------

                    if command == 'F':

                        move_forward()


                    # ----------------------------------------
                    # BACKWARD
                    # ----------------------------------------

                    elif command == 'B':

                        move_backward()


                    # ----------------------------------------
                    # LEFT
                    # ----------------------------------------

                    elif command == 'L':

                        turn_left()


                    # ----------------------------------------
                    # RIGHT
                    # ----------------------------------------

                    elif command == 'R':

                        turn_right()


                    # ----------------------------------------
                    # STOP
                    # ----------------------------------------

                    elif command == 'S':

                        stop_car()


                    # ----------------------------------------
                    # UNKNOWN COMMAND
                    # ----------------------------------------

                    else:

                        print(
                            "WARNING -> Unknown command:",
                            repr(command)
                        )


        time.sleep_ms(10)


# ============================================================
# EMERGENCY STOP
# ============================================================

except KeyboardInterrupt:

    stop_car()

    print()
    print("========================================")
    print("CAR CONTROLLER STOPPED")
    print("MOTORS DISABLED")
    print("========================================")