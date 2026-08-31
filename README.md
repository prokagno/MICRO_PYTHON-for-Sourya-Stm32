# Sourya Board -- MicroPython Applications

## Overview

This repository contains MicroPython applications developed for the
**STM32 side of our Sourya Board**.

MicroPython allows us to program the STM32 using Python while
controlling hardware peripherals such as GPIO, PWM, and UART.

------------------------------------------------------------------------

## 1. What is MicroPython?

**MicroPython** is a lightweight implementation of Python designed to
run directly on microcontrollers.

It provides a simple Python-based programming environment for
controlling microcontroller hardware without requiring a complete
low-level firmware application for every development and testing task.

In our Sourya Board, **MicroPython runs directly on the STM32** and is
used to implement the hardware-control logic.

------------------------------------------------------------------------

## 2. Requirements

### Hardware

-   Our Sourya Board
-   ST-LINK programmer/debugger
-   USB cable
-   USB-to-UART adapter
-   UART connection cables

### Software

1.  **MicroPython firmware** --- the provided `firmware.hex`
2.  **STM32CubeProgrammer** --- for erasing and programming the STM32
3.  **Thonny** --- for writing, transferring, and testing MicroPython
    programs

### Official Downloads

-   **STM32CubeProgrammer:**
    https://www.st.com/en/development-tools/stm32cubeprog.html
-   **Thonny:** https://thonny.org/

STMicroelectronics currently lists **STM32CubeProgrammer v2.23.0** as
the latest release, and the official Thonny website currently lists
**Thonny 5.0.0**.

------------------------------------------------------------------------

## 3. Install MicroPython Firmware

The repository contains the required firmware:

``` text
firmware.hex
```

This firmware must be programmed into the STM32 before using Thonny.

### Step 1 --- Install STM32CubeProgrammer

Download and install STM32CubeProgrammer from:

https://www.st.com/en/development-tools/stm32cubeprog.html

### Step 2 --- Connect ST-LINK

1.  Connect the **ST-LINK** to the computer using USB.
2.  Connect the ST-LINK programming/debug interface to the Sourya Board.
3.  Power the Sourya Board as required.
4.  Open **STM32CubeProgrammer**.

### Step 3 --- Open Erase and Programming

1.  Select the **ST-LINK** interface.
2.  Connect to the STM32.
3.  Open the **Erase and Programming** section.

### Step 4 --- Full Chip Erase

1.  Select **Full chip erase**.
2.  Start the erase operation.
3.  Wait until the erase completes successfully.

> **Important:** A full chip erase removes the existing STM32
> firmware/application.

### Step 5 --- Program the MicroPython Firmware

1.  In the **File** section, select:

    ``` text
    firmware.hex
    ```

2.  Confirm that the correct STM32 is connected.

3.  Click **Start Programming**.

4.  Wait until programming completes successfully.

5.  Do not disconnect the ST-LINK or power off the board during
    programming.

The STM32 is now ready for MicroPython.

------------------------------------------------------------------------

## 4. Install and Configure Thonny

Thonny is used as the development environment for MicroPython.

Download it from:

https://thonny.org/

### Step 1 --- Install Thonny

1.  Download the appropriate installer.
2.  Install Thonny.
3.  Open Thonny.

### Step 2 --- Select the MicroPython Interpreter

In Thonny:

1.  Open **Tools**.
2.  Select **Options**.
3.  Open the **Interpreter** tab.
4.  Select the appropriate **MicroPython** interpreter from the
    dropdown.

------------------------------------------------------------------------

## 5. Connect the Sourya Board to Thonny

Connect the **USB-to-UART adapter** to the Sourya Board using the
designated **TX2/RX2 UART interface**.

``` text
USB-UART Adapter       Sourya Board
-----------------------------------
TX       ───────────→  RX2
RX       ←───────────  TX2
GND      ────────────  GND
VCC      ────────────  VCC
```

> **Important:** TX and RX must be crossed. The adapter TX connects to
> the board RX, and the adapter RX connects to the board TX.

------------------------------------------------------------------------

## 6. Select the COM Port

After connecting the USB-to-UART adapter:

1.  Open Thonny.
2.  Go to **Tools → Options → Interpreter**.
3.  Select the appropriate MicroPython interpreter.
4.  Select the **COM/Port** that appears for the USB-to-UART adapter.
5.  Connect to the board.

If multiple COM ports are available, disconnect and reconnect the
adapter to identify the correct port.

------------------------------------------------------------------------

## 7. Program the Sourya Board

Once Thonny is connected:

1.  Open the required `.py` application.
2.  Check the code and Sourya Board pin configuration.
3.  Run the program from Thonny to test it.
4.  Check the MicroPython console for output or errors.
5.  After testing, save the program to the STM32 board.

------------------------------------------------------------------------

## 8. Important: Save the Program as `main.py`

The application that should automatically run after reset or power-up
**must be saved in the STM32 MicroPython filesystem with the exact
filename:**

``` text
main.py
```

For example:

``` text
main.py
```

If the program is saved only as:

``` text
led.py
test.py
car.py
program.py
```

it can remain stored on the board, but it will not be the automatic
startup program.

> **Always save the final application as `main.py` when it is intended
> to run automatically.**

------------------------------------------------------------------------

## 9. Complete Setup Workflow

``` text
Obtain firmware.hex
        ↓
Install STM32CubeProgrammer
        ↓
Connect ST-LINK
        ↓
Erase and Programming
        ↓
Full Chip Erase
        ↓
Select firmware.hex
        ↓
Start Programming
        ↓
MicroPython installed
        ↓
Install Thonny
        ↓
Tools → Options → Interpreter
        ↓
Select MicroPython
        ↓
Connect USB-UART to TX2/RX2 + GND/VCC
        ↓
Select correct COM port
        ↓
Open / test MicroPython program
        ↓
Save final program as main.py
        ↓
Reset / power-cycle board
        ↓
Application starts
```

------------------------------------------------------------------------

## 10. How MicroPython Is Used in This Project

The MicroPython programs developed for the Sourya Board demonstrate:

-   GPIO control
-   PWM-based control
-   UART communication
-   STM32 hardware-control logic
-   ESP32-to-STM32 communication
-   Manual and wireless vehicle-control applications

For ESP32-based applications:

``` text
User Application
      ↓
    ESP32
      ↓
     UART
      ↓
    STM32
      ↓
 MicroPython
      ↓
Sourya Board Hardware
```

The ESP32 handles application/wireless functionality when required,
while the STM32 running MicroPython handles direct hardware control.

------------------------------------------------------------------------

## 11. Important Notes

-   Use the provided **`firmware.hex`** for the Sourya Board MicroPython
    setup.
-   Use **STM32CubeProgrammer** with ST-LINK to install the firmware.
-   Use **Thonny** for MicroPython development and program transfer.
-   Select the correct COM port for the USB-to-UART adapter.
-   Use the designated **TX2/RX2** UART connection.
-   Always verify TX/RX orientation before connecting the UART adapter.
-   Save the automatic startup application as **`main.py`**.
-   Do not disconnect power or ST-LINK during firmware programming.
-   The GPIO names and peripheral configurations in the applications are
    specific to our Sourya Board.

------------------------------------------------------------------------

## Summary

**Install firmware → Full chip erase → Program `firmware.hex` → Install
Thonny → Select MicroPython interpreter → Connect USB-UART → Select COM
port → Develop/test → Save final program as `main.py`.**

Once this setup is complete, the STM32 is ready to run the MicroPython
applications provided in this repository.
