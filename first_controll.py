import serial.tools.list_ports
import time




def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        print(strPort) # print(strPort)
        if "FT232R USB UART" in strPort:
            splitPort = strPort.split(" ")
            print("PortName:",strPort)
            commPort = splitPort[0]
    return commPort

relay1_ON = [1,6,0,0,0,255,201,138]
relay1_OFF = [1,6,0,0,0,0,137,202]

portName = getPort()
print("portName:",portName)
if portName != "None":
    ser = serial.Serial(port=portName, baudrate=9600)

print(ser)
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
while True:
    ser.write(relay1_ON)
    print(serial_read_data(ser))
    time.sleep(2)
    ser.write(relay1_OFF)
    print(serial_read_data(ser))
    time.sleep(2)