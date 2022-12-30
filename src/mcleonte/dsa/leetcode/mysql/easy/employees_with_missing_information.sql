-- https://leetcode.com/problems/employees-with-missing-information/
-- https://leetcode.com/problems/employees-with-missing-information/discuss/2853824/MySQL-or-3-clear-solutions-cte-subquery-filter-before-union

-- v1 - cte

WITH full_join AS (

  SELECT *
  FROM employees
  LEFT JOIN salaries
    USING (employeed_id)

  UNION ALL

  SELECT *
  FROM salaries
  LEFT JOIN employees
    USING (employeed_id)
)

SELECT employee_id
FROM full_join
WHERE name IS NULL
  OR salary IS NULL
ORDER BY employee_id;

-- v2 - subquery

SELECT employee_id
FROM (

  SELECT *
  FROM employees
  LEFT JOIN salaries
    USING (employeed_id)

  UNION ALL

  SELECT *
  FROM salaries
  LEFT JOIN employees
    USING (employeed_id)

) AS full_join

WHERE name IS NULL
  OR salary IS NULL
ORDER BY employee_id;

-- v3 - filter each join before union

SELECT employee_id
FROM employees
LEFT JOIN salaries
  USING (employee_id)
WHERE employees.name IS NULL
  OR salaries.salary IS NULL

UNION ALL

SELECT employee_id
FROM salaries
LEFT JOIN employees
  USING (employee_id)
WHERE employees.name IS NULL
  OR salaries.salary IS NULL

ORDER BY employee_id;
