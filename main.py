#!/usr/bin/python3

import time
import board
import adafruit_dht
import logging
import os
import RPi.GPIO as GPIO


# AC Control Commands
encender = 'irsend SEND_ONCE mitsubishi SWITCH_ON'
apagar = 'irsend SEND_ONCE mitsubishi SWITCH_OFF'
subir_temp = 'irsend SEND_ONCE mitsubishi UP_TEMP'
bajar_temp = 'irsend SEND_ONCE mitsubishi DOWN_TEMP'
mostrar_comandos = 'irsend LIST mitsubishi ""' 

# Create LOG file
logging.basicConfig(filename='/home/idassa/ac_ir_control.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

#Let us Create an object
logger=logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)

# We need to set up PIN26 in OUTPUT and HIGH (1) mode to get 3V to supply Temperature Sensore (DHT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.HIGH)

# Initial the dht device, with data pin connected to PIN 40 GPIO 21:
dhtDevice = adafruit_dht.DHT22(board.D21)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        logger.info(f"Temperatura: {temperature} C -  Humedad: {humidity}% ")

        if GPIO.gpio_function(26) == 1:
           GPIO.setup(26, GPIO.OUT)
           GPIO.output(26, GPIO.HIGH)
           logger.warning("Pin 26 se ha cambiado a OUT y a 1 --> 3V")

        if temperature <= 25.0:
           logger.info('Temperatura BAJA: se apaga el aire acondicionado')
           os.system(apagar)
           time.sleep(6000.0)

        elif temperature >= 28.0:
           logger.info('Temperatura ALTA: se enciende el aire acondicionado')
           os.system(encender)
           time.sleep(6000.0)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        logger.error(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(600.0)
