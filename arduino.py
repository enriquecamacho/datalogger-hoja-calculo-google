import serial
lectura = serial.Serial('/dev/ttyACM0',9600)

while True:
    print(lectura.readline())
    line=str(lectura.readline())
    line_split=line.split('@')[1].split(',')
    print(len(line_split))
