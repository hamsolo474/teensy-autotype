#include <Bounce.h>
#include <Keyboard.h>

//const int ledPin = 13; 

void setup() {
  Serial.begin(9600); 

  //pinMode(ledPin, OUTPUT);
  //digitalWrite(ledPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); 

    if (command.startsWith("PRINT ")) {
      //digitalWrite(ledPin, HIGH); // Turn on the LED
      String content = command.substring(6);
      Keyboard.println(content);
    }
    if (command.startsWith("SLOW ")) {
      //digitalWrite(ledPin, HIGH); // Turn on the LED
      String content = command.substring(5);
      for (int i = 0; i < content.length(); i++) {
        Keyboard.print(content[i]);
        delay(120);
      }
      Keyboard.print("\n");
    }
  }
