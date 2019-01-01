high_income = False
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")   

if not student:
    print("Eligible")
else:
    print("Not Eligible") 

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")   

if high_income and good_credit and not student:
    print("Eligible")

if high_income or good_credit or not student:
    print("Eligible")

age = 22
if age >= 18 and age < 65:
    print("OK")
if 18 <= age < 65:  
    print("OK")     