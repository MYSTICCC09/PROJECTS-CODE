# SECOND PROGRAMMING EXERCISE

print("Good Day Sir Jobert!")
print("Kindly choose between metric and english units ; Type 1 for metric or 2 for english units")
unit = (int(input("")))
print("")

if unit == 1:
    print("Sir, Please enter your weight in kilograms (kg)")
    weight = (float(input("")))
    print("")

    print("Sir, Please enter your height in centimeters (cm)")
    height = (float(input("")))
    print("")

    bmi = weight/((height/100)**2)

elif unit == 2:
    print("Sir, please enter your weight in pounds (lb)")
    weight = (float(input("")))
    print("")

    print("Sir, please enter your height in inches (in)")
    height = (float(input("")))
    print("")

    bmi = (weight/(height**2))*703


if(bmi <= 18.5):
    bmiRating = "Underweight"
elif(bmi >= 18.6 and bmi <= 24.9):
    bmiRating = "Normal"
elif(bmi >= 25.0 and bmi <= 29.9):
    bmiRating = "Overweight"
elif(bmi >= 30):
    bmiRating = "Obese"

bmiString = "{:.2f}".format(bmi)

print("Your BMI is:", bmiString)
print("Your BMI Rating is:", bmiRating)

#SUBMITTED BY: ANDREI CAPILI (BSCPE 1-1 - PUP BC)