num = int(input("Type the number you want to check if it's prime or not\n"))
if num == 1:
    print(f"{num} is a prime number.")
if num == 0:
    print(f"{num} is not a prime number.")
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number.")
        break
else:
    print(f"{num} is a prime number.")
