import digitalio
import board
import busio
import adafruit_rfm9x
from time import sleep
import paho.mqtt.publish as publish

RADIO_FREQ_MHZ = 868.0
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
LoRa = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ, baudrate=1000000)

while True:
    sensor_data_message = LoRa.receive()
    if sensor_data_message is not None:
        sensor_data_string = str(received_data, "utf-8")
        publish.single("sg5-2a", sensor_data_string, hostname="mqtt.eclipseprojects.io")
