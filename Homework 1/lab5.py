#William Nguyen
#1824617
services = dict([('Oil change', 35), ('Tire rotation', 19), ('Car wash', 7), ('Car wax', 12)])
print("Davy's auto shop services")
print('Oil change --', '${}'.format(services['Oil change']))
print('Tire rotation --', '${}'.format(services['Tire rotation']))
print('Car wash --', '${}'.format(services['Car wash']))
print('Car wax --', '${}'.format(services['Car wax']))
print()
first = input('Select first service:')
print()
second = input('Select second service:')
print()
print()
print("Davy's auto shop invoice")
print()
if(first == '-'):
    print('Service 1: No service')
    first = int(0)
else:
    print('Service 1:', first+',', '${}'.format(services[first]))
    first = int(services[first])
if(second == '-'):
    print('Service 2: No service')
    second = int(0)
else:
    print('Service 2:', second+',', '${}'.format(services[second]))
    second = int(services[second])

print()
print('Total:', '${}'.format(first + second))