# 640. Solve the Equation

"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

Example 1:
    Input: equation = "x+5-3+x=6+x-2"
    Output: "x=2"

Example 2:
    Input: equation = "x=x"
    Output: "Infinite solutions"

Example 3:
    Input: equation = "2x=x"
    Output: "x=0"

Example 4:
    Input: equation = "2x+3x-6x=x+2"
    Output: "x=-1"

Example 5:
    Input: equation = "x=x+2"
    Output: "No solution"

Constraints:
    3 <= equation.length <= 1000
    equation has exactly one '='.
    equation consists of integers with an absolute value in the range [0, 100] without any leading zeros.
    equation contains only '+' and '-' operation signs.

"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        coef = [0, 0]  # coefficient of x and constant
        left = 1
        for item in re.findall("=|[\+-]?[0-9x]+", equation):
            if item == "=":
                left = -1
            elif "x" in item:
                item = item.replace("x", "")
                coef[0] += (
                    left * int(item + "1")
                    if item in ["", "+", "-"]
                    else left * int(item)
                )
            else:
                coef[1] += left * int(item)
        if coef[0] == 0:
            return "Infinite solutions" if coef[1] == 0 else "No solution"
        else:
            return "x={0}".format(-coef[1] // coef[0])
