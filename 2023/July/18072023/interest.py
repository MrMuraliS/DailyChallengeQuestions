amount = 200000
rate = 0.01  # 1% per month which means 12% per year. This is called compound interest. 12/100/12 = 0.01
# 12 percent per year divided by 100 to get the percentage in decimal form,
# then divided by 12 to get the percentage per month
years = 4


def interest(amount, rate, years):
    for _ in range(12 * years):
        amount += amount * rate
    return round(amount, 2)


print(interest(amount, rate, years))
