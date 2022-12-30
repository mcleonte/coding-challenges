-- https://leetcode.com/problems/department-highest-salary/
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
