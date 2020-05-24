import processing.serial.*;


Serial port;  // Create object from Serial class

int lip = 0;

int numVals = 9;
int[] vals = new int[9];
int[] init = {0,0,0,0,0,0,0,0,0};
int[] flags = { 0xff, 0xfe, 0xfd, 0xfc, 0xfb, 0xfa, 0xef, 0xee, 0xed };
int[][] positions = { {400, 80}, {400, 190}, {400, 300},  {400, 410}, {400, 520}, {100, 190}, {250, 190}, {550, 190}, {700, 190} };
int[][] colors = { {255, 0, 0}, {255, 122, 0}, {255, 200, 0}, {145, 200, 62}, {13, 123, 62}, {57, 83, 164}, {72, 146, 206}, {244, 150, 191}, {195, 51, 147} };
float size=100;
boolean reporting = false;
int reportingNum;
Table table;
int count=0;

int getY(int val) {
  return (int)(val / 1023.0f * size);
}

void drawValues() {
  background(0);
  textSize(32);
  for (int i = 0; i < numVals; i++) {
    fill(colors[i][0], colors[i][1], colors[i][2]);
    circle(positions[i][0], positions[i][1], getY(vals[i])-init[i]);
  }
  fill(255);
  for (int i = 0; i < numVals; i++) {
    text(getY(vals[i])-init[i], positions[i][0], positions[i][1]);
  }
  if (reporting) {
    TableRow newRow = table.addRow();
    for (int i = 0; i < numVals; i++) {
      newRow.setInt(str(i), getY(vals[i])-init[i]);
    }
    println(table.getRowCount());
    if (table.getRowCount() == 500) {
      saveTable(table, "data/" + str(reportingNum) + "count2"+str(count)+".csv");
      println("done");
      count++;
      reporting=false;
    }
  }
}

void setup() {
  size(800, 600);
  port = new Serial(this, "COM5", 9600);
  smooth();
}

void startReporting(int num) {
  table = new Table();
  for (int i = 0; i < numVals; i++) {
    table.addColumn(str(i));
  }
  reporting = true;
  reportingNum = num;
}

void keyPressed() {
  if (key==' ') {
    for (int i = 0; i < numVals; i++) {
        init[i] = getY(vals[i]);
    }
    return;
  }
  else if (!reporting) {
    if (key == '1') {
      startReporting(1);
    }
    if (key == '2') {
      startReporting(2);
    }
    if (key == '3') {
      startReporting(3);
    }
    if (key == '4') {
      startReporting(4);
    }
    if (key == '5') {
      startReporting(5);
    }
    if (key == '6') {
      startReporting(6);
    }
    if (key == '7') {
      startReporting(7);
    }
    if (key == '8') {
      startReporting(8);
    }
    if (key == '9') {
      startReporting(9);
    }
    if (key == '0') {
      startReporting(0);
    }
    if (key == 'l') {
      startReporting(10);
    }
    if (key == 'r') {
      startReporting(11);
    }
  }
}

void draw(){
  while (port.available() >= 3) {
    int val= port.read();
    for (int i = 0; i < numVals; i++) {
      if (val == flags[i]) {
        vals[i] = (port.read() << 8) | (port.read());
      }
    }
  }
  drawValues();
}
