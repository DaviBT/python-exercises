# the planets distance from the Sun

earth = 149597870   # 149,597,870 km
jupiter = 778547200 # 778,547,200 km

# Objective : discover the distance between Earth and Jupiter

distanceEarthAndJupiterKm = jupiter - earth


print("The distance in kilometers between Earth and Jupiter is " + f"{distanceEarthAndJupiterKm:,}" + "km") # result : The kilometers distance between Earth and Jupiter is 628,949,330km

distanceEarthAndJupiterMi = distanceEarthAndJupiterKm / 1.609344

print("The distance in miles between Earth and Jupiter is " + f"{distanceEarthAndJupiterMi:,}" + " miles") # result : The miles distance between Earth and Jupiter is 390,810,995.0389724 miles