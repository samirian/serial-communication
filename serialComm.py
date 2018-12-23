import serial

#import serial.tools.list_ports as port_list
#ports = list(port_list.comports())
#for p in ports:
#    print (p)
	
ser = serial.Serial(port='COM1')  # open serial port
print(ser.name)         # check which port was really used
print(ser.read())
ser.close() 