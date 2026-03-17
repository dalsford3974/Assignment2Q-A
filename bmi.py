# Weight <= 0 Test Cases:
# -1, 0, 100, 0.2

def validWeight(weight):
    if weight <= 0:
        return False
    return True

# -1, 0, 100, "abc", 0.2, "a.4"


def isWeightNum(weight):
    try:
        float(weight)
        return True
    except ValueError:
        return False

# Height <= 0 Test Cases:
# -1, 0, 5, 0.2


def validHeight(height):
    if height <= 0:
        return False
    return True

# -1, 0, 5, "abc", 0.2, "a.4"


def isHeightNum(height):
    try:
        float(height)
        return True
    except ValueError:
        return False

# Inches < 0 or >= 12 Test Cases:
# -1, 0, 5, 11, 12


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


def main():

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
    print(
        f"Your height: {heightFt:.2f} ft {HeightIn:.2f} in / {heightM:.2f} m")
    print(f"Your BMI: {bmi:.2f}")
    print(f"Your BMI classification: {classifyBMI(bmi)}")

# loop through all assert statements and print the error message if an assertion fails

assertions = [
    (validWeight(-1), "Out of bounds"),
    (validWeight(0), "Out of bounds"),
    (validWeight(100), "Invalid weight"),
    (validWeight(0.2), "Invalid weight"),
    (isWeightNum(-1), "Invalid weight"),
    (isWeightNum(0), "Invalid weight"),
    (isWeightNum(100), "Invalid weight"),
    (isWeightNum("abc"), "Invalid weight"),
    (isWeightNum(0.2), "Invalid weight"),
    (isWeightNum("a.4"), "Invalid weight"),
    (validHeight(-1), "Out of bounds"),
    (validHeight(0), "Out of bounds"),
    (validHeight(5), "Invalid height"),
    (validHeight(0.2), "Invalid height"),
    (isHeightNum(-1), "Invalid height"),
    (isHeightNum(0), "Invalid height"),
    (isHeightNum(5), "Invalid height"),
    (isHeightNum("abc"), "Invalid height"),
    (isHeightNum(0.2), "Invalid height"),
    (isHeightNum("a.4"), "Invalid height"),
    (validInches(-1), "Out of bounds"),
    (validInches(0), "Out of bounds"),
    (validInches(5), "Invalid inches"),
    (validInches(11), "Invalid inches"),
    (validInches(12), "Out of bounds")
]

for condition, message in assertions:
    try:
        assert condition, message
    except AssertionError as e:
        print(e)
