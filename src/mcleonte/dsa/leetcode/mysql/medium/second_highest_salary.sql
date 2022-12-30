-- https://leetcode.com/problems/second-highest-salary/
-- https://leetcode.com/problems/second-highest-salary/discuss/2951454/MySQL-or-elegant-replacing-of-empty-output-with-NULL
WITH cte AS (
  SELECT
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
  FROM employee
)

SELECT salary AS secondhighestsalary
FROM cte
WHERE rnk = 2

UNION ALL
SELECT NULL
LIMIT 1
