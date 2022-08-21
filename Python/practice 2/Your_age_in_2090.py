# Your age in 2090
try:
    user_input = int(input('Enter your  age / Year of birth: '))
    if user_input<=130:
        hundred = 100-user_input
        output = 2022+hundred
        print(f"You will turn 100 years old in {output}")
    elif user_input>2022:
        print("Your are not born Yet!!")
    elif user_input>1950:
        output = user_input +100
        print(f"You will turn 100 years old in {output}")
    elif user_input>1850:
        output = user_input +100
        print(f"You seem to be the oldest person alive!\nYou will turn 100 years old in {output}")
    else:
        print('Please Enter valid age!')
except:
    print("please enter only your birth year not a full birth date")
user_input2 = int(input("Enter the year you want to know your age in :"))
print(f"Your age in {user_input2} will be {user_input2 -(output - 100)}")
