# 2024. Maximize the Confusion of an Exam

"""
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l, d = 0, {"T": 0, "F": 0}  #   Ex: answerKey = TTFTTFTT
        #                   01234567

        for r in range(len(answerKey)):  #   l    r      d        r-l+1
            d[answerKey[r]] += 1  #  –––  –––  –––––––––   ––––––
            #   0    0   {T:1,F:0}     1
            if max(d.values()) < r - l - k + 1:  #   0    1   {T:2,F:0}     2
                d[answerKey[l]] -= 1  #   0    2   {T:2,F:1}     3
                l += 1  #   2    3   {T:3,F:1}     4
                #   2    4   {T:4,F:1}     5
        return r - l + 1
