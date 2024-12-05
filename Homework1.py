username = input("What's your name? ")
city = input("What city are you currently in? ")
temp = int(input("What is the temperature in "+ city +"? "))

txt = f"Hi {username}, you are in {city} and it is currently {temp}\N{DEGREE SIGN}C or {temp*3}\N{DEGREE SIGN}F  \n I predict tonight the temperature will be {temp-10}\N{DEGREE SIGN}C or {(temp*3)-20}\N{DEGREE SIGN}F  \n Have a good day!"
print(txt)


