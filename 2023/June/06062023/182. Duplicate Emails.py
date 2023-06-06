# 182. Duplicate Emails

"""
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  |
| 2  |
| 3  |
| 4  |
| 5  |
+----+---------+

For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
|         |
+---------+

Note: All emails are in lowercase.
"""

"""
/* Write your T-SQL query statement below */

SELECT 
email as Email 
FROM PERSON 
GROUP BY email HAVING count(email) > 1;  
"""
