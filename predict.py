import pickle
import serial

port = "COM3"

ser = serial.Serial(port, 9600)

with open("model.pkl", "rb") as f:
	model = pickle.load(f)

while True:
	resp = ser.readline().decode('utf-8')
	resp = [ int(x) for x in resp.split(' ') ]
	if (len(resp) == 7):
		resp = [ int(x) for x in resp ]
		print(model.predict([resp])[0])