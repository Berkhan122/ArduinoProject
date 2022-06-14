import serial
import time
import psycopg2


ser = serial.Serial('COM6', 9600, timeout=0)
conn = psycopg2.connect(database="", user="postgres",
                        password='', host='127.0.0.1', port='5432')

cur = conn.cursor()
fixed_interval = 1
while 1:
    try:
        data = ser.readline()

        datastr = str(data)
        x = datastr.replace("b'", " ")
        repdatastr = x[: -5]

        tempstart = repdatastr.startswith(" Temp")
        humstart = repdatastr.startswith(" Hum")
        lightstart = repdatastr.startswith(" Light")
        soundstart = repdatastr.startswith(" Sound")
        ratiostart = repdatastr.startswith(" Rs/")

       
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%Y/%m/%d')

        
        Data_Location = 'Ankara'

        if(tempstart):
            repdatastr = repdatastr[15:]
            cur.execute(
                '''INSERT INTO temperature (temperature, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))

            print("record inserted to temperature", repdatastr)
        elif(humstart):
            repdatastr = repdatastr[12:]
            cur.execute(
                '''INSERT INTO humidity (humidity, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))

            print("record inserted to humidity", repdatastr)
        elif(lightstart):
            repdatastr = repdatastr[9:]
            cur.execute(
                '''INSERT INTO light (light, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))

            print("record inserted to light", repdatastr)
        elif(soundstart):
            repdatastr = repdatastr[9:]
            cur.execute(
                '''INSERT INTO sound (sound, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))

            print("record inserted to sound", repdatastr)
        elif(ratiostart):
            repdatastr = repdatastr[9:]
            cur.execute(
                '''INSERT INTO mq9 (ratio, datadate, datalocation, datatime) Values (%s, %s,%s, %s)''', (float(repdatastr), date_mmddyyyy, Data_Location, time_hhmmss))
            print("record inserted to mq9", repdatastr)
        else:
            print("Record empty")

        conn.commit()

        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
    time.sleep(fixed_interval)
