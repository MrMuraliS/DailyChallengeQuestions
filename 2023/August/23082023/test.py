numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for idx, n in enumerate(numbers):
    print(f"{idx=} and number is {n=} then {numbers=}")
    n = numbers.pop()
    print(f"AFTER POP: {n=} and {numbers=}")
    if n % 2:
        numbers.insert(0, n)
    print(f"AFTER INSERT: {numbers=}\n")
