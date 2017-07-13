import time

from ctrl_sense import Ctrl_sense

# create an isntance of my Ctrl_sense
test = Ctrl_sense()

# Get current state of humidity and print it out
humid, temp = test.read_air()
soi = test.read_soil()
#print sensor readings
print('Current Humidity: {0}'.format(humid))
print('Current Temperature: {0}'.format(temp))
print('Current Soil Moisture %: {0}'.format(soi))
#test pump relay
print("Toggling relay (Ctrl-C to end test)")
while True:
    test.set_pump(True)
    time.sleep(1)
    test.set_pump(False)
    time.sleep(1)
