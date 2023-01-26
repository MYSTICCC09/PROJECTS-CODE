print()
cookies = int(input("Hi ! Please Enter How Many Cookies You Desire to Bake: "))

#Assigned Values:
sugar = 0.03125
butter = 0.02083
flour = 0.05730

sugarTotal = float(sugar*cookies)
butterTotal = float(butter*cookies)
flourTotal = float(flour*cookies)

format_sugarTotal = "{:.2f}".format(sugarTotal)
format_butterTotal = "{:.2f}".format(butterTotal)
format_flourTotal = "{:.2f}".format(flourTotal)

print()
print("Tadah! The Ingredients needed for you to bake", cookies, "pieces of cookies are")
print("Sugar:", format_sugarTotal,"Cups")
print("Butter:", format_butterTotal,"Cups")
print("Flour:", format_flourTotal,"Cups")
print()

#Submitted By: Andrei N. Capili (BSCPE 1-1)

print()
maleAmount = int(input("How Many Male Students Are In The Class?: "))
femaleAmount = int(input("How Many Female Students Are In The Class?: "))

total = maleAmount + femaleAmount

malePercent = (float(maleAmount/total)*100)
femalePercent = (float(femaleAmount/total)*100)

format_malePercent = "{:.2f}".format(malePercent)
format_femalePercent = "{:.2f}".format(femalePercent)

print()
print("Total Number of Students:", total)
print("Male Students:", maleAmount, "/", total)
print("Female Students:", femaleAmount,"/", total)
print("Percentage of Male Students:", format_malePercent, "%")
print("Percentage of Female Students:", format_femalePercent, "%")
print()

#Submitted By: Andrei N. Capili (BSCPE 1-1) - STUDENT ACCURATE