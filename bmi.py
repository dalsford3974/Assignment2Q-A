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

def testFunctions():
    tests = [
        (validWeight(-1), "Invalid weight", "test 1", "-1"), #fails OFF the boundary
        (validWeight(0), "Invalid weight", "test 2", "0"), #fails ON the boundary
        (validWeight(100), "Invalid weight", "test 3", "100"), #passes Interior valuelue
        (validHeight(-1), "Invalid height", "test 4", "-1"), #fails OFF the boundary
        (validHeight(0), "Invalid height", "test 5", "0"), #fails ON the boundary
        (validHeight(5), "Invalid height", "test 6", "5"), #passes Interior value
        (validInches(-1), "Invalid inches", "test 7", "-1"), #fails OFF the boundary
        (validInches(0), "Invalid inches", "test 8", "0"), #passes ON the boundary
        (validInches(5), "Invalid inches", "test 9", "5"), #passes Interior value
        (validInches(12), "Invalid inches", "test 10", "12"), #fails ON the boundary
        (validInches(13), "Invalid inches", "test 11", "13") #fails OFF the boundary
    ]
# If passed print the test id and "passed"
    for condition, message, test_id, input_value in tests:
        try:
            assert condition, message
            print(f"Test {test_id} passed. (input: {input_value})")
        except AssertionError as e:
            print(f"Test {test_id} failed: {e} (input: {input_value})")

testFunctions()
#main()