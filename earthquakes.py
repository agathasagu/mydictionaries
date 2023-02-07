"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""


import json

infile = open("eq_data.json", "r")

earthquakes = json.load(infile)

print(f'The number of earthquakes: {len(earthquakes["features"])}')
print()
# print(earthquakes["features"][0]["properties"]["mag"])


list = earthquakes["features"]
eq_dict = {}

for earth in list:

    if earth["properties"]["mag"] > 6:
        eq_dict[earth["id"]] = [
            earth["properties"]["place"],
            earth["properties"]["mag"],
            earth["geometry"]["coordinates"][0],
            earth["geometry"]["coordinates"][1],
        ]

# print(eq_dict)
for each in eq_dict:
    print(f"Location: {eq_dict[each][0]}")
    print(f"Magnitude: {eq_dict[each][1]}")
    print(f"Longitude: {eq_dict[each][2]}")
    print(f"Latitude: {eq_dict[each][3]}")
    print()

"""
Alternative for dictionary in dictionary

eq_dict = {}
for earth in list:

    if earth["properties"]["mag"] > 6:
        eq_dict[earth["id"]] = {}
        eq_dict[earth["id"]]["location"] = earth["properties"]["place"]
        eq_dict[earth["id"]]["magnitude"] = earth["properties"]["mag"]
        eq_dict[earth["id"]]["longitude"] = earth["geometry"]["coordinates"][0]
        eq_dict[earth["id"]]["latitude"] = earth["geometry"]["coordinates"][1]


# print(eq_dict)

for each in eq_dict:
    print(f"Location: {eq_dict[each]['location']}")
    print(f"Magnitude: {eq_dict[each]['magnitude']}")
    print(f"Longitude: {eq_dict[each]['longitude']}")
    print(f"Latitude: {eq_dict[each]['latitude']}")
    print()



"""
