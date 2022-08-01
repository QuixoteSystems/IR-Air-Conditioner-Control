# IR Air Conditioner Automatic Control
Simple Script to Control automatically your AC from a Raspberry Pi  with IR Transmitter Hat Expansion.

Python script to control your Air Conditioner, specially made to keep fresh your CPD. You can keep the room a steady fresh temperature about 25ºC. This script thanks to the IR hat switch off and switch on the Air Conditioner when detect that the temperature is high or cold enough.

Stuff you need:

- Raspberry Pi (I did with a 4 B)
- IR Remote Shield v1.0 Hat
- Temperature & Humidity Sensor DHT22
- microSD card, power supply, case...

More info about how make the project:

English: https://www.quixote.systems/en/control-your-air-conditioner-with-raspberry/

Spanish: https://www.quixote.systems/controla-tu-aire-acondicionado-con-una-raspi/


You have to adapt in the script your PATH where you want to save this script and also you have to plug DHT22 sensor to PIN 40 (GPIO 21) or wherever you want but the you have to change:

~~~
# Initial the dht device, with data pin connected to PIN 40 GPIO 21:
dhtDevice = adafruit_dht.DHT22(board.D21)
~~~
