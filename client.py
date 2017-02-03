# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()

blink = Image("99999:"
              "99999:"
              "99999:"
              "99999:"
              "99999")

             
radio.send("power on")

while True:
    incoming = radio.receive()
    if incoming is not None:
        incoming = float(incoming)
    
        sleep(1000 - running_time() % 1000)
        acceleration = accelerometer.get_z()
        radio.send(str(acceleration))
        acceleration = float(acceleration)
            
        if acceleration < (2 * incoming) or acceleration > (.5 * incoming):
            display.show(blink)
            sleep(150)
            display.clear()
            sleep(150)
            
        radio.send("next average")
    
    
    
