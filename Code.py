""" This program calculates the wind chill outside """

# Getting and defining the variables
print("Please enter the temperature(Fahrenheit):")
T = input()
print("Please enter the wind speed(mph)")
W = input()

T = float(T)
W = float(W)



# Computing the wind chill
wind_chill = (35.74+0.6215*T)+(-35.75+0.4275*T)*(W**.16)

# Displaying the wind chill
print("The wind chill is "); print(wind_chill)