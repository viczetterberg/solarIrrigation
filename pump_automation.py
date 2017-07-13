
#PROGRAM TRIGGERED BY CRON
# Author: Victor Zetterberg
#License: Public Domain courtesy of Breaks Energy LLC

import time

from ctrl_sense import Ctrl_sense

# create an isntance of my Ctrl_sense
ctrl = Ctrl_sense()

i = 0
pump_threshold = 35  #% moisture content in which pump will be triggered
irrigation_interval = 40 #seconds pump will be on for

while i < 4:
    sens0 = ctrl.read_soil()
    if sens0 == 0:
        i = 4
    elif sens0 < 25:
        i = i + 1
        print('Test {0}' .format(i))
        print('Current Soil Moisture %: {0}'.format(sens0))
        time.sleep(5)
        sens1 = ctrl.read_soil()
        i = i + 1
        print('Test {0}' .format(i))
        print('Current Soil Moisture %: {0}'.format(sens1))
        time.sleep(5)
        sens2 = ctrl.read_soil()
        i = i + 1
        print('Test {0}' .format(i))
        print('Current Soil Moisture %: {0}'.format(sens2))
        time.sleep(5)
        sens = (sens0 + sens1 + sens2)/3
        print('Average Soil Moisture %: {0}'.format(sens))

        if sens < pump_threshold:
            ctrl.set_pump(True)
            time.sleep(irrigation_interval)
            ctrl.set_pump(False)
            i = i + 1
