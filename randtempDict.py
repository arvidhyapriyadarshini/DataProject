import random
import datetime
import time


results_log = []


def projDataTemp():
    temp = round(random.uniform(20, 100), 1)
    temp1 = str(temp)
    humidity = random.randint(20, 90)
    humidity1 = str(humidity)
    utc_time = datetime.datetime.utcnow()
    time1 = utc_time.strftime('%Y-%m-%d|%H:%M:%S')
    new_result = {"Temp": temp, "Humidity": humidity, "Time": time1}
    print(new_result)
    results_log.append(new_result)

    f = open("C:\\DataPythonProject\\randomTempDict3.txt", "a")
    f.write(str("\n"))
    f.write(str(new_result))
    time.sleep(5)


endTime = datetime.datetime.now() + datetime.timedelta(seconds=20)
while True:
    if datetime.datetime.now() >= endTime:
        break
    projDataTemp()
