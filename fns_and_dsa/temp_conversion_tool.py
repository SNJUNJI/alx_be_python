FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

def convert_to_celsius(fahrenheit):
    celsius=fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit=celsius*CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit
temp=float(input("Enter the temperature to convert: "))
type=str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
if type=="C":
    result=convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
elif type=="F":
    result=convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
else:
    print("Sorry, no such operations: try again.")