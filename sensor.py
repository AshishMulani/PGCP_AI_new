class TemperatureError(Exception):
    pass

class TemperatureSensor:
    def __init__(self):
        self._temp=0

    def check_temp(self,temp):
        self._temp=temp
        if self._temp>50:
            raise TemperatureError('Temperature too high')
        else:
            print(f'current temperature {self._temp}')



sensor=TemperatureSensor()

try:
    sensor.check_temp(55)
except TemperatureError as e:
    print(f'WARNING: {e}')