import serial
import time
import requests
import json
import psycopg2

#firebase_url = 'https://arduino-project-3ee2b-default-rtdb.firebaseio.com/'
ser = serial.Serial('COM6', 9600, timeout=0)
conn = psycopg2.connect(database="GorselProg3", user="postgres",
                        password='bzc96', host='127.0.0.1', port='5432')

cur = conn.cursor()
fixed_interval = 1
while 1:
    try:
        data = ser.readline()
        # print(temperature_c)
        datastr = str(data)
        x = datastr.replace("b'", " ")
        repdatastr = x[: -5]

        tempstart = repdatastr.startswith(" Temp")
        humstart = repdatastr.startswith(" Hum")
        lightstart = repdatastr.startswith(" Light")
        soundstart = repdatastr.startswith(" Sound")
        # print(tempstart, humstart, lightstart, soundstart)
        # print(x)
        # current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%Y/%m/%d')

        # current location name
        Data_Location = 'Ankara'
        # print(repdatastr, ',', time_hhmmss, ',',
        #       date_mmddyyyy, ',', Data_Location)

        if(tempstart):
            repdatastr = repdatastr[15:]
            print(repdatastr)
            cur.execute(
                '''INSERT INTO temperature (temperature, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))
            linenumber += 1
            print("record inserted")
        elif(humstart):
            repdatastr = repdatastr[12:]
            print(repdatastr)
            cur.execute(
                '''INSERT INTO humidity (humidity, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))
            linenumber += 1
            print("record inserted")
        elif(lightstart):
            repdatastr = repdatastr[9:]
            print(repdatastr)
            cur.execute(
                '''INSERT INTO light (light, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))
            linenumber += 1
            print("record inserted")
        elif(soundstart):
            repdatastr = repdatastr[9:]
            print(repdatastr)
            cur.execute(
                '''INSERT INTO sound (sound, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))
            linenumber += 1
            print("record inserted")
        else:
            linenumber = 2

        conn.commit()
        # insert record
        # data = {'date': date_mmddyyyy,
        #         'time': time_hhmmss, 'value': repdatastr}
        # result = requests.post(
        #     firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))

        # print('Record inserted. Result Code = ',
        #       str(result.status_code), ',', result.text)
        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
    time.sleep(fixed_interval)
