sum = 0
sr =0

while(True):
    user_input= input("Enter the item price or q to quit\n")
    if (user_input !='q'):
        sum = sum + int(user_input)
        sr = sr +1
        print(f"{sr}. {user_input}")
        print(f"Order total so far: {sum}")
    if user_input=='q':
            break
print(f"Your Bill total is {sum}.Thanks for shoping.")