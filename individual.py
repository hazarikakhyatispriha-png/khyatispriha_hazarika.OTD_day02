from machine import Pin,
import time
import neopixel

ir = Pin(14,Pin.IN,Pin.PULL_UP)
np = neopixel.NeoPixel(Pin(15),16)
buzzer = Pin(12,Pin.OUT)

#Lighting us 1st LED Red is (255,0,0), Blue is (0,255,0), Green is (0,0,255)
while True:
    ir_value = ir.value()
    print(ir.value)
    time.sleep(0.2)
    if ir_value == 0:
        for i in range(0,16,1):
            np[i] =(255,0,255)
            buzzer.value(1)
            np.write()
            
        time.sleep(0.5)
    else :
        for i in range(0,16,1):
            np[i] = (0,0,0)
            buzzer.value(0)
            np.write()
        
    
    
    
    

