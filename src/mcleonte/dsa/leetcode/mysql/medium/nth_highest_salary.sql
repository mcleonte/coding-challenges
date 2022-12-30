-- https://leetcode.com/problems/nth-highest-salary/
-- https://leetcode.com/problems/nth-highest-salary/discuss/2951511/MySQL-or-short-solution-with-LIMIT-+-OFFSET
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET N
  );
END
