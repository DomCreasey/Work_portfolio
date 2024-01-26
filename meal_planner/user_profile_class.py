# The best way to store each user will be as an object,
# once each object has been instantiated we will be able to create a plan
# to the desired time length with any dietary requirements necessary.

class Person:
    """Each person will have a different profile containing
    age, weight(in kg and pounds), height(in cm and inches),
    gender and activity level.
    """

    def __init__(self, age, kg, pounds, stone_pounds, cm, inch, feet_inch, activity_lvl):
        self._age = age
        self._kg = kg
        self.pounds = pounds
        self.stone_pounds = pounds
        self._cm = cm
        self.inch = inch
        self.feet_inch = feet_inch
        self._activity_lvl = activity_lvl




