SECURE = (('a','@'),('i','1'),('s','$'),('I','|'),('o','0'))
def SecurePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password
if __name__ == '__main__':
    password = input('Enter your password:\n')
    password = SecurePassword(password)
    print(f"Your secure password is {password}")