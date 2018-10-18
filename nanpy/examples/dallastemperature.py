#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: just a test for DallasTemperature
# Dependencies: None

from nanpy import DallasTemperature

sensors = DallasTemperature(5)
n_sensors = sensors.getDeviceCount()

print("There are %d devices connected on pin %d" % (n_sensors, sensors.pin))
addresses = []

for i in range(n_sensors):
    addresses.append(sensors.getAddress(i))

sensors.setResolution(12)

while True:
    sensors.requestTemperatures()
    for i in range(n_sensors):
        temp = sensors.getTempC(i)
        print("Device %d (%s) temperature, in Celsius degrees is %0.2f" % (i, addresses[i], temp))
        print("Let's convert it in Fahrenheit degrees: %0.2f" % DallasTemperature.toFahrenheit(temp))
    print("\n")
