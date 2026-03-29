def get_grade(marks):
    if marks >= 80:
        return "Grade A"
    elif marks >= 60:
        return "Grade B"
    elif marks >= 40:
        return "Grade C"
    else:
        return "Fail"

marks = int(input("Enter marks: "))
print(get_grade(marks))