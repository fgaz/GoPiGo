def set(pin, value):
    try:
        f = open("/dev/pi-blaster", 'w')
        f.write(str(pin) + "=" + str(value))
        f.close()	
    except:
        print("Error writing to: " + property + " value: " + value)
 