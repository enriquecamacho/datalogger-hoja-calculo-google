import gspread
from oauth2client.service_account import ServiceAccountCredentials

import serial
lectura = serial.Serial('/dev/ttyACM0',9600)



scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('datasamplev1-02618c8ef7ea.json',scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
hoja_calculo = file.open("hoja1demodata").sheet1 # open sheet

#data= hoja_calculo.get_all_records()
#print(data)

#hoja_calculo.append_row([1,1,1,1,1,1,1,1])

while True:
    print(lectura.readline())
    line=str(lectura.readline())
    line_split=line.split('@')[1].split(',')
    #print(len(line_split))
    if len(line_split) == 10 :
        hoja_calculo.append_row([line_split[1],line_split[2],line_split[3],line_split[4],line_split[5],line_split[6],line_split[7],line_split[8]])

