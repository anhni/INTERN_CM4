import time
import serial.tools.list_ports

def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        print(strPort) # print(strPort)
        if "/dev/ttyAMA2" in strPort:
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

def setDevice1(state):
    serial_read_data(ser)
    #print(ser)
    if state == True:
        ser.write(relay1_ON)
        # client.publish(AIO_FEED_ID[2],1)
    else:
        ser.write(relay1_OFF)
        # client.publish(AIO_FEED_ID[2],0)

portName = getPort()
print("portName:",portName)
if portName != "None":
    ser = serial.Serial(port=portName, baudrate=9600)

relay1_ON = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

# relay6_ON = [1, 6, 0, 0, 0, 255, 201, 138]
# relay6_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

distance2_ON = [12, 3, 0, 5, 0, 1, 149, 22]
# distance2_OFF = [12, 6, 0, 8, 0, 9, 201, 19]

while True:
    ser.write(distance2_ON)                                                                                                         
    print(serial_read_data(ser)) 
    # setDevice1(relay1_ON)                                                                                                
    time.sleep(2)                                                                                                                
    # ser.write(relay1_OFF)                                                                                                        
    # print(serial_read_data(ser))   
    # setDevice1(relay1_OFF)                                                                                              
    # time.sleep(2)