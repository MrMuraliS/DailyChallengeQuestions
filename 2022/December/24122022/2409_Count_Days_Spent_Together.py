# 2409. Count Days Spent Together

"""
Alice and Bob are traveling to Rome for separate business meetings.

You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.

Return the total number of days that Alice and Bob are in Rome together.

You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
"""

"""
Example 1:

Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
Example 2:

Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
Output: 0
Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.
"""


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arriveAlicedays = list(map(int, arriveAlice.split("-")))
        leaveAlicedays = list(map(int, leaveAlice.split("-")))
        arriveBobdays = list(map(int, arriveBob.split("-")))
        leaveBobdays = list(map(int, leaveBob.split("-")))

        # print(arriveAlicedays)
        arriveAliceday = sum(days[: arriveAlicedays[0] - 1]) + arriveAlicedays[1]
        leaveAliceday = sum(days[: leaveAlicedays[0] - 1]) + leaveAlicedays[1]
        arriveBobday = sum(days[: arriveBobdays[0] - 1]) + arriveBobdays[1]
        leaveBobday = sum(days[: leaveBobdays[0] - 1]) + leaveBobdays[1]

        print(arriveAliceday, leaveAliceday, arriveBobday, leaveBobday)

        result = min(leaveAliceday, leaveBobday) - max(arriveAliceday, arriveBobday) + 1

        return result if result > 0 else 0
