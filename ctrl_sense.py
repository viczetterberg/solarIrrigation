'''
FILE NAME
ctrl_sense.py
Version 0
Created by Victor Zetterberg of Breaks Energy LLC
March 2, 2017
'''
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import Adafruit_MCP3008

#ADC init
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
#sensors and controls init
HUMIDITY = 17
PUMP     = 27
SOIL     = 0

class Ctrl_sense(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(HUMIDITY, GPIO.IN)     #set humidity sensor as input.
        GPIO.setup(PUMP, GPIO.OUT)    #set pump relay as an output.
        GPIO.setup(SOIL, GPIO.IN)     #set soil moisture as an input.

    def read_soil(self):
        mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
        moisture = mcp.read_adc(SOIL) 	#read SOIL channel of ADC
        moisture = 100*moisture/950 #convert to percentage
        return moisture

    def read_air(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, HUMIDITY) #read dht22
        temperature = temperature*9/5+32    #convert to farenheit
        return humidity, temperature

    def set_pump(self, value):
        GPIO.output(PUMP, value)
