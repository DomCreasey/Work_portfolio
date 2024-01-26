# In order for the data to be as consistent as possible,
# I want it all to be stored as metric units.
# Some people will prefer to record there weight and height
# in imperial measurements, so we will still store both measurements
# but all calculations will be on the metric units.

def metric_split(val1, val2):
    """This will allow us to split any
      metric measurements easily from a string and convert
      them into a list containing two integers.
      """
    string = input(f'Please enter in this format {val1},{val2}').strip()
    try:
        lst = string.split(',')
        num_lst = [int(lst[0]), int(lst[1])]
        return num_lst
    except ValueError:
        print('Input incorrect')
        return metric_split(val1, val2)




print(metric_split("Feet", "Inch"))

def feet_inches_to_inches(feet, inches):
    """Takes the input in Feet, Inch
    and converts it to cm's,
    """
    ttl_inch = float((float(feet) * 12) + float(inches))
    return ttl_inch


def inches_to_cms(feet, inches):
    """Takes the input in Feet, Inch
    and converts it to cm's,
    """
    ttl_inch = feet_inches_to_cms(feet, inches)
    cm = ttl_inch * 2.54
    return round(cm, 2)


def cm_to_inches(cm):
    """Takes the input in Cm
     and converts it to Inch.
     """
    inch = float(cm) * 0.393701
    return inch


def inch_to_feet_inch(inch):
    """Splits inch into a List
     containing feet, then inches.
     """
    feet_inch = [(inch // 12), (inch % 12)]
    return feet_inch


def pounds_to_kgs(stone, pounds):
    """Converts the input of Pounds to Kgs"""
    ttl_pound = float((float(stone) * 14) + float(pounds))
    kg = ttl_pound * 0.45359237
    return round(kg, 2)


def kgs_to_pounds(kg):
    """Takes the input in Kgs
     and converts it to Pounds.
     """
    pounds = float(kg) * 2.20462
    return pounds


def pounds_to_stone_pounds(pounds):
    """Splits inch into a List
       containing Stone, then Pounds.
       """
    stone_pounds = [(pounds // 12), (pounds % 12)]
    return stone_pounds
