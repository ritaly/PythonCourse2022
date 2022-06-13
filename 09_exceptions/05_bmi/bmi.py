def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "standard"
    elif bmi < 30:
        return "overweight"
    else:
        return "obesity"
