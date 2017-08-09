#!/usr/bin/python
import json

class Tariff:

    tariffs = json.loads(open('prices.json').read()) 

    def __init__(self):
        pass

    @classmethod
    def cost(cls, power_usage, gas_usage):
        cost_per_tariff = []
        for tariff in cls.tariffs:
            total = 0
            if 'power' in tariff['rates']:
                total += power_usage * tariff['rates']['power'] 
            if 'gas' in tariff['rates']:
                total += gas_usage * tariff['rates']['gas']
            #Add standing charge for the year
            months_in_year = 12
            total += months_in_year * tariff['standing_charge']
            #Add VAT   
            vat = 0.05
            total += vat * total
            cost_per_tariff.append((tariff['tariff'], round(total, 2)))
        return sorted(cost_per_tariff, key=lambda t: t[1])

    @classmethod
    def usage(cls, tariff, fuel_type, target_monthly_spend):
        #return (((month_spend - standing_charge)*12) - added_vat) / kwh_charge 
        #kwh_charge = cls.tariffs[tariff]['rates'][fuel_type]




# cmd = input()
# while cmd != 'quit':
#     print('Ovo Energy')
#Tariff.cost()
#Tariff.cost(100,2)
t = Tariff()
print(t.cost(100,50))
