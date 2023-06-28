import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    comPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        print(strPort) # print(strPort)
        if "FT232R USB UART" in strPort:
            splitPort = strPort.split(" ")
            print("PortName:",strPort)
            commPort = splitPort[0]
    return commPort

def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
            return value
        else:
            return -1
    return 0

portName = getPort()
print("portName:",portName)
if portName != "None":
    ser = serial.Serial(port=portName, baudrate=9600)

relay1_ON = [0, 6, 0, 0, 0, 255, 200, 91]
relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]

while True:
 ser.write(relay1_ON)                                                                                                         
 print(serial_read_data(ser))                                                                                                 
 time.sleep(5)                                                                                                                
 ser.write(relay1_OFF)                                                                                                        
 print(serial_read_data(ser))                                                                                                 
 time.sleep(5)