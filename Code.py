print("Please enter the temperature:")
T = input()
W = 20

wind_chill = (35.74+0.6215*T)+(-35.75+0.4275*T)*(W**.16)

print(wind_chill)