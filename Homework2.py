city = input("Enter the name of a city: ")
temp = int(input("Enter the temperature in "+ city +": "))

if temp > 20:
    print(f"It is currently warm in {city} with a temperature of 20ºC")
elif temp > 10:
    print(f"It is currently chilly in {city} with a temperature of 15ºC")
elif temp < 10:
    print(f"It is currently cold in {city} with a temperature of 5ºC")
else :
    #if city == None or str(temp) == None:
    print("Please try again and enter a city and temperature")

 
    
