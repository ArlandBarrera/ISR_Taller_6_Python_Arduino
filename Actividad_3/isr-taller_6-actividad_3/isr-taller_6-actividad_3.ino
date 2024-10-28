const int trigger = 11;
const int echo = 10;
float tiempo, distancia;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(3);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(8);
  digitalWrite(trigger, LOW);
  tiempo = pulseIn(echo, HIGH);
  distancia = tiempo / 59;
  Serial.println(distancia);
  delay(150);
}
