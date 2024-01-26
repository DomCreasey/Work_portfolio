# Functions will be needed to calculate the bmi of the user,
# The equation for Male and Female is different
# so will have to be applied differently depending on the user.





# For men – BMR =
# 66.5 + (13.75 * weight in kg) + (5.003 * height in cm) - (6.75 * age) .
def m_bmr(kg, cm, age):
    bmr = 66.5 + (13.75 * float(kg))\
          + (5.003 * float(cm)) - (6.75 * float(age))
    return bmr

# print(m_bmr(63.3, 170, 29))


# For women – BMR =
# 655.1 + (9.563 * weight in kg) + (1.850 * height in cm) - (4.676 * age).
def f_bmr(kg, cm, age):
    bmr = 665.1 + (9.563 * float(kg))\
          + (1.850 * float(cm)) - (4.676 * float(age))
    return bmr
