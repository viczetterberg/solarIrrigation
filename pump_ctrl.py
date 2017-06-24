#trigger pump automatically from env_log.py or user input from lab_env_db.html
# Author: Victor Zetterberg
#License: Public Domain courtesy of Breaks Energy LLC
import time

#Import MCP3008 library for Analog to Digital Converter
import Adafruit_MCP3008
#Import GPIO Library
import RPi.GPIO as GPIO

#Software SPI configuration:

CLK       = 18
MISO      = 23
MOSI      = 24
CS        = 25
pump_pin  = 27
on_time   = 10				#500GPH at 10 sec is .139 gallons 
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setup(pump_pin, GPIO.OUT)		#set pin to be output

GPIO.output(pump_pin, GPIO.HIGH)	#Turn on pump
time.sleep(on_time)			#Wait "on_time" seconds
GPIO.output(pump_pin, GPIO.LOW)		#Turn off pump

GPIO.cleanup()
