
def is_leap(year):
    leap = False
    if year%400 ==0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    return leap

# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# year = int(input())
# print(is_leap(year))



year = int(input())
print(is_leap(year))
