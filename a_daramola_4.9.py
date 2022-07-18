#Akinola Daramola Jr
#Programming Exercise 4.9
#06/29/2022


"""
Ocean Levels
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year,
create an application that displays the number of millimeters that the ocean will have risen each year for the next 25 years.
"""

#Declaring value for sea level vaiable
sea_level_per_year = 1.6

#Declaring value of years with range function
years = range(1,26,1)

#For loop to iterate through years variable
for year in years: #For loop syntax
    total_amount = year * sea_level_per_year #Calculating sea level rate times each year
    print(f"Sea level year {year}: {total_amount:.2f}mm") #Displaying sea level for each year


