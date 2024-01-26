# This project will take in a users details and calculate there BMI.
# A meal plan will be tailored to them depending on  goals and fitness level.
print("Welcome to Dom's meal planner!")
from imperial_metric_converter import metric_split, inches_to_cms, \
    feet_inches_to_inches, cm_to_inches, inch_to_feet_inch




def height_entry_measurement():
    """This will allow the user to input the data in the
     measurement they are most comfortable with.
     """
    choice = input(
        "How would you like to enter your"
        " Height? CM(1), Feet,Inches(2) or Inches(3)")
    if choice == '1':
        cm = int(input('Enter your height in Cms\n'))
        inch = cm_to_inches(cm)
        feet_inch = inch_to_feet_inch(inch)
    elif choice == '2':
        feet_inch = metric_split('Feet', 'Inches')
        inch = feet_inches_to_inches(feet_inch[0], feet_inch[1])
        cm = inches_to_cms()
    elif choice == '3':
        inch = int(input('Enter your height in Inches\n'))
        cm = inches_to_cms(inch)
        feet_inch = inch_to_feet_inch(inch)
    else:
        print('That is not a valid entry')
        return height_entry_measurement()
    return cm, inch, feet_inch


cm, inch, feet_inch = height_entry_measurement()
