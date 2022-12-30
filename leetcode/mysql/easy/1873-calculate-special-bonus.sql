-- https://leetcode.com/problems/calculate-special-bonus
-- https://leetcode.com/problems/calculate-special-bonus/discuss/2848543/MySQL-or-3-approaches

-- v1
SELECT
    employee_id,
    salary * (name NOT LIKE 'M%') * (employee_id & 1) as bonus
FROM Employees
ORDER BY employee_id;

-- v2
SELECT
    employee_id,
    IF(employee_id & 1 = 1 AND name NOT LIKE 'M%', salary, 0) as bonus
FROM Employees
ORDER BY employee_id;

-- v3
SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 = 1 AND LEFT(name,1) != 'M'
        THEN salary
        ELSE 0
    END AS bonus
FROM Employees
ORDER BY employee_id;

