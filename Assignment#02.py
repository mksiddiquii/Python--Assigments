name = input("What is your Name? ")
math = int(input("Enter Your Math Number? "))
english = int(input("Enter Your English Number? "))
science = int(input("Enter Your Science Number? "))
chemistry = int(input("Enter Your Chemistry Number? "))
biology = int(input("Enter Your Biology Number? "))
total_no_get = math + english + science + chemistry + biology
total_number = 500
percentage = (total_no_get / total_number) * 100
print(f"Name:{name}\nMath:{math}\nEnglish:{english}\nScience:{science}\nChemistry:{chemistry}\nBiology:{biology}")
print(f"Total Number: 500/{total_no_get}\nPercentage:{percentage}%")
if percentage >= 90:
    print("Excellent A+ grade")
elif percentage >= 80 and percentage < 90:
    print("Excellent A grade")
elif percentage >= 70 and percentage < 80:
    print("Good B grade")
elif percentage >= 60 and percentage < 70:
    print("Average C grade")
elif percentage >= 50 and percentage < 60:
    print("Below Average D grade")
else:
    print("Fail F grade")
