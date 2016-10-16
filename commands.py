MINPIN = 0
MAXPIN = 15
command = 0

def encodeCommand():
    action = input('Please select action(0/R - 1/W):')
    action = int(action)
    
    if (action < 0  or action > 1):
        return -1

    pin = input('Please select pin:')
    pin = int(pin)
    if( pin < MINPIN or pin > MAXPIN):
        return -1
    command = pin + (action<<4)
    
    return command

 

    
