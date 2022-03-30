import serial
import time
import random
ser = serial.Serial('COM3', 9600, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_TWO, timeout=1)
vald = [b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']
data = b'\xe8\x00\x00\x00\x00\x01\x04\x00\x00\x63\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# data_arr = ['\xe8', '\x00', '\x00', '\x00', '\x00', '\x01', '\x04', '\x00', '\x00', '\x64', '\x00', '\x00', '\x00',
#             '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00', '\x00']
data_arr = [232, 0, 0, 0, 0, 1, 4, 0, 0, 100, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
addr = 1
while True:
    # for x in range(8):
    # vald[x] = bytes([random.randint(0, 200)])
    # data_arr[5] = bytes([x+1])
    # data_arr[9] = bytes([random.randint(0, 100)])
    # ser.write(data)
    # print(data_arr)
    # for y in range(len(data_arr)):
    # print(data_arr[y])
    # print(bytes([data_arr[y]]))
    # ser.write(bytes([data_arr[y]]))
    tmp_data = b'\xe8\x00\x00\x00\x00'
    # print(b'\xe8\x00\x00\x00\x00')
    tmp_data += bytes([addr])
    tmp_data += b'\x04\x00\x00'
    tmp_data += bytes([random.randint(0, 100)])
    tmp_data += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ser.write(tmp_data)
    print(tmp_data)
    # time.sleep(1)
    addr += 1
    if addr >= 9:
        addr = 1
    # for x in range(len(data_arr)):
    #     vald[x] = random.randint(0, 200)
