celsius_temps = [0, 10, 20, 31, 45, 100]

fahrenheit_temps = [t*9/5 + 32 for t in celsius_temps if t>20]
print(fahrenheit_temps)