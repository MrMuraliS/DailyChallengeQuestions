import json
from json import JSONDecodeError

s = "{aff_id:1571,culture:EN-US,package:4}"
temp = s.strip("{}").split(",")

print(temp)

temp = dict(map(lambda x: x.split(":"), temp))
print(temp)

for x, y in temp.items():
    try:
        temp[x] = eval(y)
    except:
        pass

print(temp)

# try:
#     json.loads(s)
# except JSONDecodeError as e:
#     print("Invalid JSON")
#     print(e)
# except Exception as e:
#     print(e)
