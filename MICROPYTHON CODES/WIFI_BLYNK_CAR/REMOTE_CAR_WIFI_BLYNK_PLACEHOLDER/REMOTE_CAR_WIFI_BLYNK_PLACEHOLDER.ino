#define BLYNK_TEMPLATE_ID "YOUR_BLYNK_TEMPLATE_ID"
#define BLYNK_TEMPLATE_NAME "YOUR_BLYNK_TEMPLATE_NAME"
#define BLYNK_AUTH_TOKEN "YOUR_BLYNK_AUTH_TOKEN"

#include <WiFi.h>
#include <BlynkSimpleEsp32.h>

char ssid[] = "YOUR_WIFI_SSID";
char pass[] = "YOUR_WIFI_PASSWORD";

#define RXD2 16
#define TXD2 17

HardwareSerial STM(2);

int joyX = 512;
int joyY = 512;

char lastCommand = 'S';

const int CENTER = 512;
const int DEADZONE = 150;

void sendCommand(char cmd)
{
    if(cmd != lastCommand)
    {
        STM.write(cmd);
        lastCommand = cmd;

        Serial.print("Sent : ");
        Serial.println(cmd);
    }
}

void processJoystick()
{
    Serial.print("X=");
    Serial.print(joyX);
    Serial.print("  Y=");
    Serial.println(joyY);

    char command = 'S';

    if(joyY > CENTER + DEADZONE)
    {
        command = 'F';
    }
    else if(joyY < CENTER - DEADZONE)
    {
        command = 'B';
    }
    else if(joyX < CENTER - DEADZONE)
    {
        command = 'L';
    }
    else if(joyX > CENTER + DEADZONE)
    {
        command = 'R';
    }
    else
    {
        command = 'S';
    }

    sendCommand(command);
}

BLYNK_WRITE(V0)
{
    joyX = param.asInt();
    processJoystick();
}

BLYNK_WRITE(V1)
{
    joyY = param.asInt();
    processJoystick();
}

void setup()
{
    Serial.begin(115200);

    STM.begin(115200, SERIAL_8N1, RXD2, TXD2);

    Serial.println();
    Serial.println("==============================");
    Serial.println("SOURYA REMOTE CAR");
    Serial.println("==============================");

    Serial.print("Connecting WiFi");

    WiFi.begin(ssid, pass);

    while(WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi Connected");
    Serial.print("IP : ");
    Serial.println(WiFi.localIP());

    Blynk.config(BLYNK_AUTH_TOKEN);

    Serial.print("Connecting Blynk");

    while(!Blynk.connect())
    {
        Serial.print(".");
        delay(500);
    }

    Serial.println();
    Serial.println("Blynk Connected");
    Serial.println("Ready");
}

void loop()
{
    Blynk.run();

    static unsigned long timer = 0;

    if(millis() - timer > 5000)
    {
        timer = millis();

        Serial.println("----------------------");

        if(WiFi.status() == WL_CONNECTED)
        {
            Serial.println("WiFi : Connected");
            Serial.print("RSSI : ");
            Serial.println(WiFi.RSSI());
        }
        else
        {
            Serial.println("WiFi : Disconnected");
        }

        if(Blynk.connected())
        {
            Serial.println("Blynk : Connected");
        }
        else
        {
            Serial.println("Blynk : Disconnected");
        }
    }
}