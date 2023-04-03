def is_leap(year):
    leap = False

    if year % 400 == 0:
        print("400")
        leap = True
    elif year % 100 == 0:
        print("100")
        leap = False
    elif leap % 4 == 0:
        print("4")
        print(leap % 4)
        leap = True
    else:
        print("else")
        leap = False

    return leap


year = int(input("Enter the year: "))
print(is_leap(year))
