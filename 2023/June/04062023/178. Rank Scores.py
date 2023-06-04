# 178. Rank Scores

"""
Write an SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| Id          | int     |
| Score       | decimal |
+-------------+---------+
Id is the primary key for this table.
Each row contains the score of a candidate in some exam.

Using the above example table, the query should return the following:

+-------+------+
| score | rank |
+-------+------+
| 3.50  | 1    |
| 3.65  | 2    |
| 4.00  | 3    |
| 5.00  | 4    |
+-------+------+

"""

# Write your MySQL query statement below

# select Score, dense_rank() over(order by Score desc) as Rank from Scores;
