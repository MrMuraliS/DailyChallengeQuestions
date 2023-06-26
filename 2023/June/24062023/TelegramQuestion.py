import random


def guss():
    print("get a number in your mind")
    while True:
        gc = random.randint(1, 10)
        x = input(f"is you number{gc} yes or no?")
        if x != "no":
            break


print("i got youuu")
guss()
