import serial
import time
import random
ser = serial.Serial('COM3', 9600, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_TWO, timeout=1)
addr = 1
while True:
    tmp_data = b'\xe8\x00\x00\x00\x00'
    tmp_data += bytes([addr])
    tmp_data += b'\x04\x00\x00'
    tmp_data += bytes([random.randint(0, 100)])
    tmp_data += b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ser.write(tmp_data)
    print(tmp_data)
    addr += 1
    if addr >= 9:
        addr = 1
