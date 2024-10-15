def check_grade(Grade):
    if Grade >= 80 and Grade <= 100:
        return"You did a great job!"

    elif Grade >= 70 and Grade <= 79:
        return"Keep it up!"
    
    elif Grade >= 60 and Grade <= 69:
        return"You passed but there room for improvement."

    else:
        return"Better luck next time."
    
usergrade = int(input("Enter Grade: "))
print(check_grade(usergrade))