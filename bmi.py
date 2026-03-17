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
