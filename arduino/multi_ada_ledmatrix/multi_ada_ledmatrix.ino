#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_IS31FL3731.h>

// If you're using the full breakout...
Adafruit_IS31FL3731 ledmatrix[4];

void init_matrix() {
  for(int i=0; i<4; i++) {
    ledmatrix[i] = Adafruit_IS31FL3731(); 
    //ledmatrix[i].Matrix(i2c, address=0x75);
  }
}

// If you're using the FeatherWing version
//Adafruit_IS31FL3731_Wing ledmatrix = Adafruit_IS31FL3731_Wing();
//display = adafruit_is31fl3731.Matrix(i2c, address=0x75)

// The lookup table to make the brightness changes be more visible
uint8_t sweep[] = {1, 2, 3, 4, 6, 8, 10, 15, 20, 30, 40, 60, 60, 40, 30, 20, 15, 10, 8, 6, 4, 3, 2, 1};
uint8_t address[] = {0x74, 0x75, 0x76, 0x77};

void setup() {
  Serial.begin(9600);
  Serial.println("Multi test");

  init_matrix();
  for(int i=0; i<4; i++) {
    if (! ledmatrix[i].begin(address[i])) {
      Serial.println("IS31 not found");
      while (1);
    }
  }
//  Serial.println("IS31 found!");
}

void loop() {
  // animate over all the pixels, and set the brightness from the sweep table
  for (uint8_t incr = 0; incr < 24; incr++)
    for (uint8_t x = 0; x < 16; x++)
      for (uint8_t y = 0; y < 9; y++)
        for(int i=0; i<4; i++)
          ledmatrix[i].drawPixel(x, y, sweep[(x+y+incr)%24]);
  delay(20);
}
