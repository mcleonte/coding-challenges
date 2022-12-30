-- https://leetcode.com/problems/duplicate-emails/
-- https://leetcode.com/problems/duplicate-emails/discuss/2831249/MySQL-or-simplest-approach
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(id) > 1
