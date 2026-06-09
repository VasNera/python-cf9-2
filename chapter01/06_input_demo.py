name = input("Please enter your name: ")

year_of_birth = int(input("Please enter your birth"))
height = float(input("Please enter your height"))
is_student = input("Are you a student? (yes/no)").lower == "yes"

if is_student:
    print("You are a student")
else:
    print("You are a teacher")
