from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class Display(ArduinoObject):
    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

    @arduinoobjectmethod
    def setSeconds(self, seconds):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getSeconds(self):
        pass

    @arduinoobjectmethod
    def setMinutes(self, minutes):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getMinutes(self):
        pass

    @arduinoobjectmethod
    def setHours(self, hours):
        pass

    @returns(int)
    @arduinoobjectmethod
    def getHours(self):
        pass

    @arduinoobjectmethod
    def setup(self):
        pass

    @arduinoobjectmethod
    def loop(self):
        pass
