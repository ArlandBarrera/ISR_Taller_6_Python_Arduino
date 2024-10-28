const int LED = 13;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){
    char serialData = Serial.read();
    if (serialData == '1'){
      digitalWrite(LED, HIGH);
    } else {
      digitalWrite(LED, LOW);
    }
  }
}
