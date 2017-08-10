#!/usr/bin/python
import json

class Tariff:

    tariffs = json.loads(open('prices.json').read())
    months_in_year = 12
    vat = 0.05

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
            total += cls.months_in_year * tariff['standing_charge']
            #Add VAT
            total += cls.vat * total
            cost_per_tariff.append((tariff['tariff'], round(total, 2)))
        return sorted(cost_per_tariff, key=lambda t: t[1])

    @classmethod
    def usage(cls, tariff, fuel_type, target_monthly_spend):
        try:            
            selected_tariff = [t for t in cls.tariffs if t['tariff'] == tariff][0]            
        except IndexError:
            print("{0} is not a recognised tariff.".format(tariff))
            return 0
        if fuel_type not in selected_tariff['rates']:
            print("{0} does not have a rate for {1} fuel type.".format(tariff, fuel_type))
            return 0
        #Calculate the monthly standing charge + VAT
        gross_standing_charge = selected_tariff['standing_charge'] + (selected_tariff['standing_charge'] * cls.vat)
        #Deduct that from the monthly spend
        net_monthly_spend = target_monthly_spend - gross_standing_charge
        #Calculate the kwh rate + VAT
        gross_kwh = selected_tariff['rates'][fuel_type] + (selected_tariff['rates'][fuel_type] * cls.vat)
        return round(net_monthly_spend / gross_kwh, 2)


#print(Tariff.usage('better-energy', 'power', 100))
cmd = input("Please enter command:\n").split()
while cmd[0] != 'quit':
    if cmd[0] == 'cost':
        result = Tariff.cost(float(cmd[1]), float(cmd[2]))
        print(result)
    elif cmd[0] == 'usage':
        result = Tariff.usage(cmd[1], cmd[2], float(cmd[3]))
        print(result)#TODO format me
    else:
        cmd = input("Command not recognised. Please try again: \n").split()
        continue
    cmd = input("Please enter command:\n").split()




