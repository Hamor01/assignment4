def cal_grade(maths, physics, geo, chem):

    # Check for negative values and values greater than 100

    if any(mark < 0 or mark > 100 for mark in [maths, physics, geo, chem]):
        return 'Those are unrecognized marks or average'

    # Calculate the average
    total = (maths + physics + geo + chem)

    avg = total / 4

    # Determine the grade based on the average
    if 0 <= avg <= 30:
        return 'D'
    elif 31 <= avg <= 50:
        return 'C'
    elif 51 <= avg <= 70:
        return 'B'
    elif 71 <= avg <= 100:
        return 'A'


# Prompting the user to enter the subject marks

maths = int(input("Enter Maths mark: "))

physics = int(input("Enter Physics mark: "))

geo = int(input("Enter Geography mark: "))

chem = int(input("Enter Chemistry mark: "))

# The final grade of the student

result = cal_grade(maths, physics, geo, chem)

print("Your mean grade is : ", result)
