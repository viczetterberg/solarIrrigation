#!/usr/bin/env python

'''

FILE NAME
env_log.py

1. WHAT IT DOES
Takes a reading from a DHT sensor and records the values in an SQLite3 database using a Raspberry Pi.
 
2. REQUIRES
* Any Raspberry Pi
* A DHT sensor
* A 10kOhm resistor
* Jumper wires

3. ORIGINAL WORK
Raspberry Full stack 2015, Peter Dalmaris

4. HARDWARE
D17: Data pin for sensor

5. SOFTWARE
Command line terminal
Simple text editor
Libraries:
import sqlite3
import sys
import Adafruit_DHT

6. WARNING!
None

7. CREATED 

8. TYPICAL OUTPUT
No text output. Two new records are inserted in the database when the script is executed

 // 9. COMMENTS
--

 // 10. END

'''



import sqlite3
import sys
import Adafruit_DHT
import time
import Adafruit_MCP3008

# Software SPI Configuration
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def log_values(sensor_id1, sensor_id2, moist, temp, hum):
	conn=sqlite3.connect('/var/www/lab_app/lab_app.db')  #It is important to provide an
							     #absolute path to the database
							     #file, otherwise Cron won't be
							     #able to find it!
	curs=conn.cursor()
	curs.execute("""INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (sensor_id1,temp))
	curs.execute("""INSERT INTO moistures values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (sensor_id2,moist))
	curs.execute("""INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'),
         (?), (?))""", (sensor_id1,hum))

	conn.commit()
	conn.close()

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
temperature = temperature*9/5+32
moisture = mcp.read_adc(0)
moisture =100*moisture/950
# If you don't have a sensor but still wish to run this program, comment out all the 
# sensor related lines, and uncomment the following lines (these will produce random
# numbers for the temperature and humidity variables):
# import random
# humidity = random.randint(1,100)
# temperature = random.randint(10,30)
if humidity is not None and temperature is not None and moisture is not None:
	log_values("1", "2", moisture, temperature, humidity)	
else:
	log_values("1", "2", -999, -999, -999)
