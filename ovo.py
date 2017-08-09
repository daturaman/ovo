#!/usr/bin/python
import json

class Tariff:

    tariffs = json.loads(open('prices.json').read())

    def __init__(self):
        pass

    @classmethod
    def cost(cls, power_usage, gas_usage):
        for tariff in cls.tariffs:
            annual_power = 0
            if 'power' in tariff['rates']:
                annual_power = power_usage * tariff['rates']['power']
            print("{0} {1}".format(tariff['tariff'], round(annual_power, 2)))






# cmd = input()
# while cmd != 'quit':
#     print('Ovo Energy')
#Tariff.cost()
#Tariff.cost(100,2)
t = Tariff()
t.cost(100,2)
