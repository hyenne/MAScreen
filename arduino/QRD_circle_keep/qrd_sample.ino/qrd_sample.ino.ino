int pin0 = A0;
int pin1 = A1;
int pin2 = A2;
int pin3 = A3;
int pin4 = A4;
int pin5 = A5;
int pin6 = A6;
int pin7 = A7;
int pin8 = A8;


int val0 = 0;  // variable to store the value coming from the sensor
int val1 = 0;
int val2 = 0;
int val3 = 0;
int val4 = 0;
int val5 = 0;
int val6 = 0;
int val7 = 0;
int val8 = 0;

int cnt = 0;

void setup() {

  // initialize serial:

  Serial.begin(19200);

  // declare the ledPin as an OUTPUT:

}

 

void loop() {

  // read the value from the sensor:

  val0 = analogRead(pin0);
  val1 = analogRead(pin1);
  val2 = analogRead(pin2);
  val3 = analogRead(pin3);
  val4 = analogRead(pin4);
  val5 = analogRead(pin5);
  val6 = analogRead(pin6);
  val7 = analogRead(pin7);
  val8 = analogRead(pin8);


  
  

//  //send over serial
//
  Serial.write( 0xff); //control byte
  Serial.write( (val0 >> 8) & 0xff); //first byte
  Serial.write( val0 & 0xff);  //second byte

  Serial.write( 0xfe);
  Serial.write( (val1 >> 8) & 0xff);
  Serial.write( val1 & 0xff);
  
  Serial.write( 0xfd);
  Serial.write( (val2 >> 8) & 0xff);
  Serial.write( val2 & 0xff);
  
  Serial.write( 0xfc);
  Serial.write( (val3 >> 8) & 0xff);
  Serial.write( val3 & 0xff);

  Serial.write( 0xfb);
  Serial.write( (val4 >> 8) & 0xff);
  Serial.write( val4 & 0xff);

  Serial.write( 0xfa); //control byte
  Serial.write( (val5 >> 8) & 0xff); //first byte
  Serial.write( val5 & 0xff);  //second byte

  Serial.write( 0xef); //control byte
  Serial.write( (val6 >> 8) & 0xff); //first byte
  Serial.write( val6 & 0xff);  //second byte

  Serial.write( 0xee); //control byte
  Serial.write( (val7 >> 8) & 0xff); //first byte
  Serial.write( val7 & 0xff);  //second byte

  Serial.write( 0xed); //control byte
  Serial.write( (val8 >> 8) & 0xff); //first byte
  Serial.write( val8 & 0xff);  //second byte
  cnt++;
  if (cnt == 1000) {
    Serial.println('------------'+millis());
    cnt=0;
  }
////  delay(100);                 

}

 
