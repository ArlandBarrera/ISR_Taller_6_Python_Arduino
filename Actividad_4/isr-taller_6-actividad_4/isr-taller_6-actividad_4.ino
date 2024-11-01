#include <DHT.h>
#define DHTTYPE DHT11

const int pinDHT11 = 2;
float humedad;
float temperatura;

DHT dht(pinDHT11, DHTTYPE);

void setup() {
  dht.begin();
  Serial.begin(9600);
}

void loop() {
  delay(5000); // delay 5s, recomendacion del fabricante
  humedad = dht.readHumidity();
  temperatura = dht.readTemperature(); // grados celsius
  Serial.print(humedad);
  Serial.print(",");
  Serial.println(temperatura);
}
