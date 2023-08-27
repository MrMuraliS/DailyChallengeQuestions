# 207. Course Schedule

"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                To take course 1 you should have finished course 0, and to take course 0 you should
                also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 105
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

"""


# Solution 1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        # Create a visited array
        visited = [0] * numCourses

        # DFS
        def dfs(i):
            # If we have a cycle, return False
            if visited[i] == -1:
                return False
            # If we have already visited this node, return True
            if visited[i] == 1:
                return True

            # Mark the node as visited
            visited[i] = -1

            # For each pre in the graph, check if we can finish the course
            for pre in graph[i]:
                if not dfs(pre):
                    return False

            # Mark the node as visited
            visited[i] = 1
            return True

        # For each course, check if we can finish it
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# Solution 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        # Create a visited array
        visited = [0] * numCourses

        # DFS
        def dfs(i):
            # If we have a cycle, return False
            if visited[i] == -1:
                return False
            # If we have already visited this node, return True
            if visited[i] == 1:
                return True

            # Mark the node as visited
            visited[i] = -1

            # For each pre in the graph, check if we can finish the course
            for pre in graph[i]:
                if not dfs(pre):
                    return False

            # Mark the node as visited
            visited[i] = 1
            return True

        # For each course, check if we can finish it
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# Solution 3
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a graph
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        # Create a visited array
        visited = [0] * numCourses

        # DFS
        def dfs(i):
            # If we have a cycle, return False
            if visited[i] == -1:
                return False
            # If we have already visited this node, return True
            if visited[i] == 1:
                return True

            # Mark the node as visited
            visited[i] = -1

            # For each pre in the graph, check if we can finish the course
            for pre in graph[i]:
                if not dfs(pre):
                    return False

            # Mark the node as visited
            visited[i] = 1
            return True

        # For each course, check if we can finish it
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
