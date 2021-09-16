""" This program calculates the wind chill outside and now it doesn't suck ass """

# Getting and defining the variables
T = input("Please enter the temperature (Fahrenheit): ")
W = input("Please enter the wind speed (mph): ")

T = float(T)
W = float(W)



# Computing the wind chill
wind_chill = (35.74+0.6215*T)+(-35.75+0.4275*T)*(W**.16)

# Displaying the wind chill
print("The wind chill is "); print(wind_chill)


print("Persona 5 Royal lol")