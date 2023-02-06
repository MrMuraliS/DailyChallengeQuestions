# 433. Minimum Genetic Mutation

"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

    Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
Output: 2

Example 3:

Input: startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
Output: 3
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        from collections import deque

        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            print(f"{queue=}")
            node, steps = queue.popleft()
            print(f"{node=}, {steps=}")
            if node == end:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    print(f"{c=}, {i=}")
                    neighbor = node[:i] + c + node[i + 1 :]
                    print(f"{neighbor=}")
                    print(f"{seen=}")
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1


if __name__ == "__main__":
    # startGene = "AACCGGTT"
    # endGene = "AACCGGTA"
    # bank = ["AACCGGTA"]
    # print(Solution().minMutation(startGene, endGene, bank))
    #
    # startGene = "AACCGGTT"
    # endGene = "AAACGGTA"
    # bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    # print(Solution().minMutation(startGene, endGene, bank))

    startGene = "AAAAACCC"
    endGene = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(Solution().minMutation(startGene, endGene, bank))
