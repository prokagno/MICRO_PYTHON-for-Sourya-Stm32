#define RXD2 16
#define TXD2 17

HardwareSerial mySerial(2);

void setup()
{
  Serial.begin(115200);

  mySerial.begin(115200, SERIAL_8N1, RXD2, TXD2);

  Serial.println("Type message:");
}

void loop()
{
  // Receive from STM32
  if (mySerial.available())
  {
    String data = mySerial.readString();

    Serial.println("From STM32: " + data);
  }

  // Send to STM32
  if (Serial.available())
  {
    String command = Serial.readStringUntil('\n');

    command.trim();

    mySerial.println(command);

    Serial.println("Sent to STM32: " + command);
  }
}