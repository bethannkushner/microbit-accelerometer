# Add your Python code here. E.g.
from microbit import *
import radio

radio.on()

data_list = [] #defines list where accelerometer data is stored
avg = None

while True:
        
    if button_a.was_pressed():
        display.scroll(str(len(data_list)))
        
    if button_b.was_pressed():
        if avg is not None:
            display.scroll(str(avg))
        elif avg == None:
            display.scroll("-1023")
        
    incoming = radio.receive()
    if incoming == "power on":
        if avg == None:
            radio.send("-1023")
        elif avg is not None:
            avg = int(avg)
            radio.send(str(avg))
            
    elif incoming == "next average":
        if avg == None:
            radio.send("-1023")
        elif avg is not None:
            radio.send(str(avg))
            
    elif incoming is not None:
        incoming = int(data
        data_list.append(data)
        
    if len(data_list) % 5 == 0 and len(data_list) >= 5:
        avg = sum(data_list)/len(data_list)
        avg = int(avg)
        
    if len(data_list) >= 100:
        avg = sum(data_list)/len(data_list)
        avg = int(avg)
        data_list.clear()
        data_list.append(avg)
        
    
        
        
        
        
        
    
