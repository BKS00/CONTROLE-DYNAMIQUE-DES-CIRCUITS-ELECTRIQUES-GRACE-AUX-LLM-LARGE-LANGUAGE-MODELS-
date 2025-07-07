#include <Servo.h>

Servo myservo;
String command = "";

void setup() {
  Serial.begin(9600);
  Serial.println("Arduino is ready");

  pinMode(5, OUTPUT);  // LED 1
  pinMode(3, OUTPUT); // LED 2
  pinMode(11, OUTPUT); // LED 3
  myservo.attach(6);   // Servo moteur connecté à la broche 6
}

void executeCommand(int device, int action, int* params, int paramCount) {
  switch (device) {
    case 1:
      if (action == 0 && paramCount > 0) analogWrite(5, params[0]); // LED 1
      break;
    case 2:
      if (action == 0 && paramCount > 0) analogWrite(3, params[0]); // LED 2
      break;
    case 3:
      if (action == 0 && paramCount > 0) analogWrite(11, params[0]); // LED 3
      break;
    case 4:
      if (action == 1 && paramCount > 0) myservo.write(params[0]); // Servo moteur
      break;
    default:
      Serial.println("Invalid device or action");
      break;
  }
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      Serial.print("Received command: ");
      Serial.println(command);

      int parts[5] = {0}; 
      int partIndex = 0;
      int commaIndex = 0;
      while ((commaIndex = command.indexOf(',')) > 0 && partIndex < 5) {
        parts[partIndex++] = command.substring(0, commaIndex).toInt();
        command = command.substring(commaIndex + 1);
      }
      parts[partIndex] = command.toInt();

      if (partIndex >= 1) {
        executeCommand(parts[0], parts[1], parts + 2, partIndex - 1);
      } else {
        Serial.println("Command format error");
      }

      command = ""; 
    } else {
      command += c;
    }
  }
}
