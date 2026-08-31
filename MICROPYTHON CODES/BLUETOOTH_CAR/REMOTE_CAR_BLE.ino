#include <BluetoothSerial.h>
#include "esp_system.h"

BluetoothSerial SerialBT;

HardwareSerial STM(2);

#define RXD2 16
#define TXD2 17


void setup()
{
    Serial.begin(115200);

    delay(1000);

    Serial.println();
    Serial.println("===== ESP32 BOOT =====");
    Serial.print("Reset reason: ");
    Serial.println(esp_reset_reason());

    SerialBT.begin("SOURYA_MICRO_CAR");

    STM.begin(115200, SERIAL_8N1, RXD2, TXD2);

    Serial.println("Bluetooth Ready");
    Serial.println("SOURYA_MICRO_CAR");
}

void loop()
{
    if(SerialBT.available())
    {
        char cmd = SerialBT.read();

        STM.write(cmd);

        Serial.print("Sent : ");
        Serial.println(cmd);
    }
}