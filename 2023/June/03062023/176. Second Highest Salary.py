# 176. Second Highest Salary

"""
Write a SQL query to get the second highest salary from the Employee table.
If there is no second highest salary, then the query should return null.

Example 1:
    Input:
        +----+--------+
        | Id | Salary |
        +----+--------+
        | 1  | 100    |
        | 2  | 200    |
        | 3  | 300    |
        +----+--------+
    Output:
        +---------------------+
        | SecondHighestSalary |
        +---------------------+
        | 200                 |
        +---------------------+

Example 2:
    Input:
        +----+--------+
        | Id | Salary |
        +----+--------+
        | 1  | 100    |
        +----+--------+
    Output:
        +---------------------+
        | SecondHighestSalary |
        +---------------------+
        | Null                |
        +---------------------+

Constraints:
    There will always be at least two employees in the table.

"""

# Write your MySQL query statement below

SELECT MAX(salary) as SecondHighestSalary FROM Employee WHERE salary < ( SELECT MAX(salary) as SecondHighestSalary FROM Employee ORDER BY salary DESC);