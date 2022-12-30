-- https://leetcode.com/problems/department-highest-salary/
-- https://leetcode.com/problems/department-highest-salary/discuss/2951421/MySQL-or-greater96-efficient-solution-with-CTE-and-RANK
WITH cte AS (
  SELECT
    name,
    salary,
    departmentid,
    RANK() OVER(PARTITION BY departmentid ORDER BY salary DESC) AS rnk
  FROM employee
)

SELECT
  department.name AS department,
  cte.name AS employee,
  cte.salary
FROM cte
INNER JOIN department
  ON cte.departmentid = department.id
    AND cte.rnk = 1
