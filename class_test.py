# Bibliotheken laden
from machine import Pin, I2C
import struct
import utime as time

enable_Pin = machine.Pin(16, machine.Pin.OUT, value=0)

from I2C.i2c_caen import A7585

DEV_A = A7585(112,20,21)
DEV_A.startup(80,10,30,2,rampuptime=2)

enable_Pin.value(1)
DEV_A.SetEnable(True)

print("Setup Done")

time.sleep(1)

def check_I2C():
    Vout = DEV_A.GetVout()
    statusHV = DEV_A.GetHVOn()
    conectionHV = DEV_A.GetConnectionStatus()
    print("V:",Vout,"HV:",statusHV,"Connectivity:",conectionHV)

while True:
    print(DEV_A.GetRampVs())
    print(DEV_A.GetMaxV())
    time.sleep(1.5)
  
    



