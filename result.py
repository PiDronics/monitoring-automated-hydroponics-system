from time import sleep, time
import datetime

class Result:
    def __init__(self, value, sensorType):
        self.status = self.getStatus(value, sensorType)
        self.value = value
        self.date_time = self.getDateTime()
        self.unix_time = round(time()*1000)

    def getStatus(self, value, sensorType):
        status = -1
        if sensorType in "Temperature":
            if value > 30 and value < 35:
                status = 8
            elif value > 35 and value < 40:
                status = 5
            elif value > 40:
                status = 1
            else:
                status = 10
        elif sensorType in "pH":
            if value > 5.5 and value < 6.5:
                status = 10
            elif (value > 6.5 and value < 7) or (value < 5.5 and value > 5):
                status = 5
            else:
                status = 1
        return status
    
    def getDateTime(self):
        now = datetime.datetime.now()
        return(now.strftime("%Y-%m-%d %H:%M"))
