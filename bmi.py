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


def BMICalc():
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
    print(f"Your BMI classification: {classifyBMI(bmi)}\n")

# loop through all assert statements and print the error message if an assertion fails


def testFunctions():
    tests = [
        # fails OFF the boundary
        (1, validWeight(-1) == False, "Weight must be a positive number", "-1"),

        # fails ON the boundary
        (2, validWeight(0) == False, "Weight must be a positive number", "0"),

        # passes Interior value
        (3, validWeight(100) == True, "Weight is valid", "100"),

        # fails OFF the boundary
        (4, validHeight(-1) == False, "Height must be a positive number", "-1"),

        # fails ON the boundary
        (5, validHeight(0) == False, "Height must be a positive number", "0"),

        # passes Interior value
        (6, validHeight(5) == True, "Height is valid", "5"),

        # fails OFF the boundary
        (7, validInches(-1) == False, "Inches must be a value between 0 and 11", "-1"),

        # passes ON the boundary
        (8, validInches(0) == True, "Inches is valid", "0"),

        # passes Interior value
        (9, validInches(5) == True, "Inches is valid", "5"),

        # fails ON the boundary
        (10, validInches(12) == False, "Inches must be a value between 0 and 11", "12"),

        # fails OFF the boundary
        (11, validInches(13) == False, "Inches must be a value between 0 and 11", "13"),

        # passes Underweight
        (12, classifyBMI(18.4) == "Underweight",
         "BMI classification is Underweight", "18.4"),

        # passes Normal weight ON the boundary
        (13, classifyBMI(18.5) == "Normal weight",
         "BMI classification is Normal weight", "18.5"),

        # passes Normal weight OFF the boundary
        (14, classifyBMI(24.9) == "Normal weight",
         "BMI classification is Normal weight", "24.9"),

        # passes Overweight ON the boundary
        (15, classifyBMI(25) == "Overweight",
         "BMI classification is Overweight", "25"),

        # passes Overweight OFF the boundary
        (16, classifyBMI(29.9) == "Overweight",
         "BMI classification is Overweight", "29.9"),

        # passes Obese ON the boundary
        (17, classifyBMI(30) == "Obese", "BMI classification is Obese", "30"),

        # passes Obese OFF the boundary
        (18, classifyBMI(30.1) == "Obese", "BMI classification is Obese", "30.1"),
    ]
# If passed print the test id and "passed"
    print("\nRunning tests...")
    for testNum, condition, message, inputValue in tests:
        try:
            assert condition, message
            print(f"Test {testNum} passed. (input: {inputValue})")
        except AssertionError as e:
            print(f"Test {testNum} failed: {e} (input: {inputValue})")
    print("All tests completed.\n")


while True:
    print("What would you like to do?\n1. BMI Calculator\n2. Test Cases\n3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        BMICalc()
    elif choice == "2":
        testFunctions()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
