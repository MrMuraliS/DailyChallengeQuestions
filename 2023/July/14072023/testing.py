totalCost = 189  # Total subscription cost
usedDays = [30, 30, 30, 30, 30, 20]  # Number of days each person has used

# Calculate the total number of days used by all people
totalUsedDays = sum(usedDays)
print(189 / totalUsedDays)
data = [days * (189 / totalUsedDays) for days in usedDays]
print(data)
print(sum(data))
# Calculate individual subscription cost for each person
individualCosts = [totalCost * (days / totalUsedDays) for days in usedDays]

# Calculate your subscription revenue
subscriptionRevenue = sum(individualCosts)

print("Individual Subscription Costs:")
total = 0
for i, cost in enumerate(individualCosts):
    print(f"Person {i+1}: {cost}")
    total += cost
print("Total:", total)

print("Total Subscription Revenue:", subscriptionRevenue)
