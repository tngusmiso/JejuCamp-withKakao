#-*- coding: utf-8 -*-

class Car():
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x,'의 스피드로 움직이고 있습니다.')
    def stop(self):
        print('멈춤')

class HyCar(Car):
    battery = 100
    batteryKM = 300

hyk3 = HyCar()
print(hyk3.maxSpeed)