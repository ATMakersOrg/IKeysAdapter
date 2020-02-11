/*
 * Demonstrate the use of the USB Host Library for SAMD IntelliKeys (IK) USB
 * host driver. Prints IK events as CLIENT on serial port.
 */
 
#include <Adafruit_DotStar.h>

// There is only one pixel on the board
#define NUMPIXELS 1 

//Use these pin definitions for the ItsyBitsy M4
#define DATAPIN    7
#define CLOCKPIN   8

Adafruit_DotStar strip(NUMPIXELS, DATAPIN, CLOCKPIN, DOTSTAR_RGB);

#include <IntelliKeys.h>
#include <ArduinoJson.h>

//We are going to send in Little Endian, but we'll define this to make it easy to make it portable
#define HTONS(x) (x)
#define HTONL(x) (x)
#define NTOHS(x) (x)
#define NTOHL(x) (x)
/* Swap the defines above for the ones below if you want to send in "Network" (standard) byte order
#define HTONS(x) __builtin_bswap16(x)
#define HTONL(x) __builtin_bswap32(x)
#define NTOHS(x) __builtin_bswap16(x)
#define NTOHL(x) __builtin_bswap32(x)
*/

// On Arduino Zero debug on and send CLIENT to debug port
#if defined(ARDUINO_SAMD_ZERO)
#define DBSerial  if(1)Serial
#define CLIENT      Serial
#else
// All other boards including Trinket M0, debug off and send CLIENT to Serial1
#define DBSerial  if(0)Serial
#define CLIENT      Serial1
#endif

USBHost myusb;
IntelliKeys ikey1(&myusb);

char mySN[IK_EEPROM_SN_SIZE+1]; //+1 NUL

#define MAX_PRESSED 48
uint16_t pressedCells[MAX_PRESSED];

uint8_t overlayId=0;
uint8_t shiftState=0;
uint8_t altState=0;
uint8_t ctrlState=0;

void insertCell(short idx)
{
  for(int i = 0; i < MAX_PRESSED;i++)
  {
    if (pressedCells[i] == idx)
    {
      return; //already pressed
    }
    else if (pressedCells[i] == 0)
    {
      //end of list, insert at end
      pressedCells[i] = idx;
      return;
    }
    else if (idx < pressedCells[i])// we have a value in this spot - should we insert before it?
    {
      //speed this up with memcpy() or memmove() (probably doesn't matter at size 24)
      for (int j = (MAX_PRESSED - 1); j > i; j++)
      {
        pressedCells[j] = pressedCells[j-1];
      }
      pressedCells[i] = idx;
      return;
    }
    //else we need to keep moving forward - continue
  }
}
void removeCell(short idx)
{
  for (int i = 0; i < MAX_PRESSED; i++)
  {
    if (pressedCells[i] == idx) //found it
    {
      //optimize with memmove()
      for (int j = i; j < MAX_PRESSED; j++)
      {
        if (j == (MAX_PRESSED - 1))
        {
          pressedCells[j] = 0;
        }
        else
        {
          pressedCells[j] = pressedCells[j+1];
        }
        if (pressedCells[j] == 0)
        {
          return;
        }
      }
    }
  }
}

void IK_press(int x, int y)
{
  uint16_t idx = (x * 24) + y;
  insertCell(idx);
}

void IK_release(int x, int y)
{
  uint16_t idx = (x * 24) + y;
  removeCell(idx);
}

void IK_switch(int switch_number, int switch_state)
{
}

// Returns modified n. 
int modifyBit(int n, int p, int b) 
{ 
    int mask = 1 << p; 
    return (n & ~mask) | ((b << p) & mask); 
} 
  
void IK_sensor(int sensor_number, int sensor_value)
{
  overlayId = modifyBit(overlayId, sensor_number, sensor_value);
}

void IK_version(int major, int minor)
{
}

void IK_connect(void)
{
}

void IK_disconnect(void)
{
}

void IK_onoff(int onoff)
{
}

void IK_get_SN(uint8_t SN[IK_EEPROM_SN_SIZE])
{
}

void IK_correct_membrane(int x, int y)
{
}

void IK_correct_switch(int switch_num, int switch_state)
{
}

void IK_correct_done()
{
}

#define CMD_POLL 1

void readCommand()
{
  char command; //one byte commands
  static int ticksSinceCmd = 0;
  static uint16_t pressedBuff[MAX_PRESSED];
  int bytesAvail;
  
  if ((bytesAvail = CLIENT.available()) > 0) {
    ticksSinceCmd = 0;
    size_t bytesIn;
    CLIENT.setTimeout(10);
    command = CLIENT.read();//read one byte which is our command
    switch(command)
    {
      case 1:
      {
        shiftState = CLIENT.read();//the shift State
        altState = CLIENT.read();//read Alt State
        ctrlState = CLIENT.read();//read Ctrl State

        //Before we send the count, send the overlay id
        CLIENT.write(overlayId);
        
        uint8_t count = 0;
        memset(pressedBuff, 0, sizeof(pressedBuff));
        for (int i = 0 ; i < MAX_PRESSED; i++)
        {
           uint16_t idx = pressedCells[i];
           if (idx == 0)
           {    
            break;
           }
           pressedBuff[i] = HTONS(idx);
           count++;
        }
        CLIENT.write(count);
        CLIENT.write((const char*)pressedBuff, sizeof(uint16_t)*count); 
        break;
      }
    case 2: //set light on/off
      {
        uint8_t light=CLIENT.read();
        uint8_t status=CLIENT.read();
        ikey1.setLED(light, status);
        break;
      }
    }
  }
/*  else
    {
      ticksSinceCmd++;
      //no data available, if we've done this 100 times, go ahead and take time to reset the LEDs
      if (ticksSinceCmd > 1000)
      {
        ticksSinceCmd = 0;
        ikey1.setLED(1, shiftState);      
        ikey1.setLED(2, altState);      
        ikey1.setLED(5, ctrlState);      

        ikey1.setLED(3, 0);      
        ikey1.setLED(4, 0);      
        ikey1.setLED(6, 0);      
        ikey1.setLED(7, 0);      
        ikey1.setLED(8, 0);      
        ikey1.setLED(9, 0);      
      }      
    }
    */
}

void setup() {
  short s = HTONS(50);
  strip.begin(); // Initialize pins for output
  uint32_t magenta = strip.Color(255, 0, 255);
  uint32_t white = strip.Color(255, 255, 255);
  strip.setBrightness(80);
  strip.setPixelColor(0, white);
  strip.show();  // Turn all LEDs off ASAP
  
  DBSerial.begin(115200);
  DBSerial.println("IntelliKeys USB Test");
  // If there are concerns about CLIENT transmission being too slow, boost
  // the UART speed. 4*115200 or 8*115200 works on the SAMD21. Make sure to
  // match the UART speed on the other side.
  CLIENT.begin(115200);
  myusb.Init();

  ikey1.onConnect(IK_connect);
  ikey1.onDisconnect(IK_disconnect);
  ikey1.onMembranePress(IK_press);
  ikey1.onMembraneRelease(IK_release);
  ikey1.onSwitch(IK_switch);
  ikey1.onSensor(IK_sensor);
  ikey1.onVersion(IK_version);
  ikey1.onOnOffSwitch(IK_onoff);
  ikey1.onSerialNum(IK_get_SN);
  ikey1.onSerialNum(IK_get_SN);
  ikey1.onCorrectMembrane(IK_correct_membrane);
  ikey1.onCorrectSwitch(IK_correct_switch);
  ikey1.onCorrectDone(IK_correct_done);

  memset(mySN, 0, sizeof(mySN));
}

void loop() {
  myusb.Task();
  ikey1.Task();
  readCommand();
}
