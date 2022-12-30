-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
SELECT employee.name AS employee
FROM employee
INNER JOIN employee AS manager
  ON employee.managerid = manager.id
    AND employee.salary > manager.salary
