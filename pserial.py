import serial
import mysql.connector

ser = serial.Serial('/dev/ttyUSB0', 9600, bytesize=serial.EIGHTBITS,
					parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_TWO, timeout=1)
conn = mysql.connector.connect(
	user='ptdsn_admin', password='bismillah', host='127.0.0.1', database='ptdsn')
mode_write = False
data_arr = []


def send_to_db(name, value):
	cursor = conn.cursor()
	sql1 = "UPDATE status SET nilai='"+str(value)+"' WHERE nama='"+str(name)+"'"
	sql2 = "INSERT INTO log (nama, nilai) VALUES ('" + \
							str(name)+"','"+str(value)+"')"
	# print(sql)
	cursor.execute(sql1)
	cursor.execute(sql2)

	conn.commit()
	cursor.close()


while True:
	read = ser.read()
	if read == b'\xe8':
		mode_write = True
		continue
	if mode_write == True:
		data_arr.append(read)
	if len(data_arr) >= 17:
		if data_arr[4] == b'\x01' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 1: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x02' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 2: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x03' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 3: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x04' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 4: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x05' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 5: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x06' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 6: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x07' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 7: " + str(int.from_bytes(data_arr[8], "big")))
		elif data_arr[4] == b'\x08' and data_arr[5] == b'\x04':
			send_to_db(str(int.from_bytes(data_arr[4], "big")), str(
				int.from_bytes(data_arr[8], "big")))
			print("addr 8: " + str(int.from_bytes(data_arr[8], "big")))
		data_arr = []
		mode_write = False



