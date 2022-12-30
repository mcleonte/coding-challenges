-- https://leetcode.com/problems/second-highest-salary/
-- https://leetcode.com/problems/second-highest-salary/discuss/2951454/MySQL-or-elegant-replacing-of-empty-output-with-NULL
WITH cte AS (
  SELECT DISTINCT salary AS secondhighestsalary
  FROM employee
  ORDER BY salary DESC
  LIMIT 1, 1
)

SELECT secondhighestsalary
FROM cte
UNION ALL
SELECT NULL
LIMIT 1
