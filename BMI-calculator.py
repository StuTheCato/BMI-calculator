import os
import time
from time import sleep

# BMI - Table
seeTable = input("Do you want to see the BMI Table? (y/n): ")

if (seeTable == "y"):
    print("BMI Table:")
    print(".----------------.---------------------.")
    print("|  Underweight:  |   less than 18,5    |")
    print(":----------------+---------------------:")
    print("| Normal weight: | 18,5 - 24,9         |")
    print(":----------------+---------------------:")
    print("| Overweight:    | 25 - 29,9           |")
    print(":----------------+---------------------:")
    print("| Obesity:       | over than 30 - 34,9 |")
    print("'----------------'---------------------'")
    print("") # <-- for space
    print(".........................................")
    print("")
elif (seeTable == "n"):
    os.system('cls')


# User inputs
weight = input("Your body weight (kg): ")
print(f"==> {weight}")
height = input("Your body height (m): ")
print(f"==> {height}")
sleep(2)
print("")


# Calculate BMI
calcHeight = float(height) * float(height)
calcBMI = int(weight) / calcHeight
yourBMI = round(calcBMI, 1)

if (yourBMI < 18.5):
    print(f"{yourBMI} - You are underweight.")
elif (0 < yourBMI < 24.9):
    print(f"{yourBMI} - You are normal weight.")
elif (25 < yourBMI < 29.9):
    print(f"{yourBMI} - You are overweight.")
elif (30 < yourBMI < 999999):
    print(f"{yourBMI} - You are obese.")
    
#     /\_____/\
#    /  o   o  \
#   ( ==  ^  == )
#    )         (
#   (           )
#  ( (  )   (  ) )
# (__(__)___(__)__)
