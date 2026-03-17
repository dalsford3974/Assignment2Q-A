def validWeight(weight):
    if weight <= 0:
        return False
    return True


def isWeightNum(weight):
    try:
        float(weight)
        return True
    except ValueError:
        return False


def validHeight(height):
    if height <= 0:
        return False
    return True


def isHeightNum(height):
    try:
        float(height)
        return True
    except ValueError:
        return False

def validInches(inches):
    if inches < 0 or inches >= 12:
        return False
    return True


def lbsToKg(weight):
    return weight * 0.45


def inchesToMeters(height):
    return height * 0.025


def calculateBMI(weight, height):
    return weight / (height ** 2)


def classifyBMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# need to fix the -Ft plus +In printing height must be greater than 0 error.
# It is just invalid

while True:
    weightLbs = input("Enter your weight in lbs: ")
    if not isWeightNum(weightLbs):
        print("Invalid input. Please enter a number.\n")
        continue
    weightLbs = float(weightLbs)
    if not validWeight(weightLbs):
        print("Weight must be greater than 0.\n")
        continue
    heightFt = input("Enter your height in feet: ")
    HeightIn = input("Enter your height in inches: ")
    if not isHeightNum(heightFt) or not isHeightNum(HeightIn):
        print("Invalid input. Please enter a number.\n")
        continue
    heightFt = float(heightFt)
    HeightIn = float(HeightIn)
    if not validInches(HeightIn):
        print("Inches must be a value between 0 and 11.\n")
        continue
    if not validHeight(heightFt) or not validHeight(HeightIn):
        print("Height must be greater than 0.\n")
        continue
    weightKg = lbsToKg(weightLbs)
    heightM = inchesToMeters(HeightIn) + (inchesToMeters(heightFt) * 12)
    bmi = calculateBMI(weightKg, heightM)
    break

# print weight in both pounds and kilograms
print(f"Your weight: {weightLbs:.2f} lbs / {weightKg:.2f} kg")
# print height in both feet/inches and meters
print(f"Your height: {heightFt:.2f} ft {HeightIn:.2f} in / {heightM:.2f} m")
print(f"Your BMI: {bmi:.2f}")
print(f"Your BMI classification: {classifyBMI(bmi)}")

