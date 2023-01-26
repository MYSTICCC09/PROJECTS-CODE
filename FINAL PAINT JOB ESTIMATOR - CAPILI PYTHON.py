# SECOND PROGRAMMING EXERCISE

print ("Sir, please enter the area of the wall (Square Feet)")
wallArea = (float(input("")))
print ("Sir, please enter the price of the paint per gallon (USD)")
paintPrice = (float(input("")))
print()

paintGallon = wallArea/115

# 115sqft : 1 Gallon of Paint


totalLaborTime = paintGallon*8

# 1 Gallon of Paint : 8 Hours of Labor
paintCost = paintGallon*paintPrice
laborCost = totalLaborTime*20

# 8 Hours of Labor : 20 Dollars
totalCost = laborCost + paintCost

laborTimeHoursInt = (int(totalLaborTime))
# Converting to Int to obtain the whole number or hours only

laborTimeMinutesFloat = (float(totalLaborTime - laborTimeHoursInt))
# Subtracting the whole number from the total to obtain minutes

laborTimeMinutesInt = (int(60*laborTimeMinutesFloat))
# Converting minutes from decimal form in hours into minutes

paintCostString = "{:.2f}".format(paintCost)
paintGallonString = "{:.2f}".format(paintGallon)
laborCostString = "{:.2f}".format(laborCost)
totalCostString = "{:.2f}".format(totalCost)

if(paintGallon == 1):
    print("The Gallon of paint required: " + paintGallonString + " gallon of paint")
else:
    print("The Gallons of paint required: " + paintGallonString + " gallons of paint")

if(laborTimeMinutesInt == 0):
    print("It will take" , laborTimeHoursInt , "Hours")
else:
    print("The time you will have to wait will take" , laborTimeHoursInt , "Hours and" , laborTimeMinutesInt , "Minutes")
print("The paint will cost $" + paintCostString)
print("The labor will cost $" + laborCostString + " at a rate of $20 per hour")
print("Overall, your total cost to: $ will be:"+ totalCostString)

#SUBMITTED BY: ANDREI CAPILI (BSCPE 1-1 - PUP BC)