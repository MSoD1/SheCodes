#Ask what the current temperature is and if it’s rainy
#If the temperature is more than 20 and it’s not raining, output
#Enjoy a sunny day
#If the temperature is more than 20 and it’s raining, output: 
#Don’t forget your umbrella
#If the temperature is less than 20 and it’s not raining, output 
#Don’t forget your jacket
#If the temperature is less than 20 and it’s raining output 
#Don’t forget your umbrella and your jacket

temp = int(input("What is the current temperature? "))

rain = str(input("Is it raining? "))

if temp > 20 and rain == 'No':
    print("Enjoy the sunny day")
elif  temp < 20 and rain == 'Yes':
    print("Don’t forget your jacket")
