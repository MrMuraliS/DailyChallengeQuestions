data = [
    ("satish.bonde", "admin"),
    ("aditya. kumar01", "admin"),
    ("ravi", "moder"),
    ("amit", "moder"),
]


def getDict(val):
    results = dict()
    for value, key in val:
        if key not in results:
            results[key] = [value]
        else:
            results[key].append(value)
    return results


print(getDict(data))
