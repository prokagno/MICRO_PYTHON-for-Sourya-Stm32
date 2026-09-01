# SOURYA Board -- MicroPython Applications

## Overview

This repository contains MicroPython-based applications developed for
our STM32-based SOURYA Board.

The purpose of these examples is to demonstrate how the STM32 side of
the SOURYA Board can be programmed using MicroPython for GPIO control,
PWM-based control, UART communication, and integration with the ESP32.

------------------------------------------------------------------------

## What is MicroPython?

**MicroPython** is a lightweight implementation of the Python
programming language designed to run directly on microcontrollers.

It provides a simple Python-based programming environment while still
allowing access to hardware peripherals such as:

-   GPIO pins
-   PWM
-   UART
-   Timers
-   ADC and other microcontroller peripherals

Instead of writing low-level embedded code for every hardware operation,
MicroPython provides a simpler and more readable way to control the
microcontroller.

------------------------------------------------------------------------

## Why are we using MicroPython?

MicroPython is being used on the **STM32 side of our SOURYA Board** to
make hardware development and testing faster and easier.

It allows us to:

-   Configure STM32 GPIO pins using simple Python statements.
-   Control outputs directly from the MicroPython program.
-   Generate PWM signals for hardware control.
-   Communicate with the ESP32 through UART.
-   Quickly test and modify hardware-control logic without developing a
    complete low-level firmware application.

The STM32 therefore acts as the **hardware-control processor**, while
MicroPython provides the programming interface used to implement that
control logic.

------------------------------------------------------------------------

## MicroPython on Our SOURYA Board

Our SOURYA Board contains an STM32 microcontroller and an ESP32 for
wireless and higher-level applications.

For the MicroPython applications documented here, the **STM32 runs the
MicroPython firmware**.

The basic workflow is:

``` text
MicroPython Code
       ↓
STM32 MicroPython Firmware
       ↓
STM32 Hardware Peripherals
       ↓
SOURYA Board Hardware
```

When communication with the ESP32 is required, the architecture becomes:

``` text
Application / Wireless Interface
              ↓
             ESP32
              ↓
             UART
              ↓
             STM32
              ↓
      MicroPython Program
              ↓
      SOURYA Board Hardware
```

This provides a clear separation between the wireless/application layer
and the real-time hardware-control layer.

------------------------------------------------------------------------

## How We Use MicroPython

A MicroPython application generally follows these steps:

1.  **Import the required MicroPython modules.**
2.  **Configure the required STM32 peripherals.**
3.  **Assign the required GPIO pins.**
4.  **Implement the hardware-control functions.**
5.  **Run the main application loop.**
6.  **Monitor the system through the MicroPython serial console when
    required.**

For example, GPIO control can be initialized using:

``` python
from machine import Pin

led = Pin("A6", Pin.OUT)

led.on()
led.off()
```

Similarly, PWM can be configured for hardware control:

``` python
from machine import Pin, PWM

motor = PWM(Pin("A6"))
motor.freq(1000)
motor.duty_u16(60000)
```

UART can be used to communicate with the ESP32:

``` python
from machine import UART

uart = UART(1, 115200)
```

The exact pins and peripherals depend on the particular SOURYA Board
application.

------------------------------------------------------------------------

## MicroPython Applications in This Project

The MicroPython programs in this project demonstrate several core
functions of our SOURYA Board.

### 1. GPIO Control

MicroPython is used to configure STM32 GPIO pins as inputs or outputs
and control their digital states.

This provides the basic software interface for controlling digital
hardware connected to the board.

### 2. PWM Control

The STM32 uses MicroPython PWM functionality for hardware-control
applications that require variable duty-cycle output.

In the car-control application, PWM is used to control the motor-driver
enable signals.

### 3. UART Communication

MicroPython is used to configure the STM32 UART peripheral and
communicate with the ESP32.

The STM32 can receive commands from the ESP32 and execute the
corresponding hardware-control operation.

### 4. ESP32 + STM32 Applications

In the remote-car applications, the ESP32 handles the higher-level
interface:

-   Bluetooth-based control, or
-   Wi-Fi/Blynk-based control.

The ESP32 converts the user's command into a simple control command and
sends it to the STM32 through UART.

The STM32 then performs the actual motor-control operation using
MicroPython.

------------------------------------------------------------------------

## Programming Model

The overall programming model used in these applications is:

``` text
MicroPython Interface
      │
      ▼
USB-TTL/FDTI adapter
      │
      │ UART
      ▼
    STM32
      │
      ▼
 MicroPython
      │
      ├── GPIO
      ├── PWM
      └── Other STM32 Peripherals
```

This architecture allows the ESP32 and STM32 to have clearly defined
responsibilities.

### ESP32

The ESP32 is responsible for application-level and wireless
functionality when required.

``` text
User Application
      │
      ▼
    ESP32
      │
      │ UART
      ▼
    STM32
      │
      ▼
 MicroPython
      │
      ├── GPIO
      ├── PWM
      └── Other STM32 Peripherals
```

### STM32

The STM32 is responsible for direct hardware control.

### MicroPython

MicroPython provides the software layer through which the STM32 hardware
is configured and controlled.

------------------------------------------------------------------------

## Running a MicroPython Program

The general process is:

1.  Install or use a MicroPython-compatible development environment.
2.  Connect the SOURYA Board to the computer.
3.  Ensure the STM32 is running the appropriate MicroPython firmware.
4.  Open the MicroPython serial/REPL interface.
5.  Transfer or execute the `.py` program on the STM32.
6.  Observe the serial output for initialization and operation messages.
7.  Verify the corresponding hardware operation.

The application files in this repository can be used as individual
MicroPython programs according to their respective documentation.

------------------------------------------------------------------------

## Important Note

The MicroPython programs are intended to be used with the **pin
assignments and hardware architecture of our SOURYA Board**.

Therefore, GPIO names and peripheral configurations should not be copied
directly to another STM32 board without checking that board's pin
mapping and MicroPython firmware configuration.

For applications involving the ESP32, the ESP32 and STM32 must also be
connected according to the UART configuration specified in the
corresponding documentation.

------------------------------------------------------------------------

## Project Documentation

Detailed documentation is provided separately for each application.

The documentation covers the relevant:

-   Objective
-   Hardware interface
-   Pin assignment
-   Peripheral configuration
-   Functional operation
-   MicroPython code
-   Communication architecture where applicable
-   Safety and reliability considerations

For the remote-car applications, the documentation also covers the ESP32
application layer and the communication path between the ESP32 and
STM32.

------------------------------------------------------------------------

## Summary

MicroPython gives our SOURYA Board a practical and flexible way to
program the STM32 hardware using Python.

In this project, it is primarily used to:

-   Control STM32 GPIOs.
-   Generate PWM signals.
-   Handle UART communication.
-   Implement hardware-control logic.
-   Interface the STM32 with the ESP32 application layer.

The resulting architecture keeps the system modular:

**ESP32 handles the application/wireless side, while STM32 + MicroPython
handles the direct hardware-control side.**


---

## Author

**Dhanumjay Suragani** — [GitHub Profile](https://github.com/Dhanumjay-Suragani)