-- https://leetcode.com/problems/exchange-seats/submissions/
-- https://leetcode.com/problems/exchange-seats/discuss/2860927/MySQL-or-greater98-Shortest-solution-with-pure-math-no-IF-CASE-UNION-WHERE
SELECT
  student,
  id - 1 + (id & 1) * (2 - (id = (SELECT COUNT(id) FROM seat))) AS id
FROM seat
ORDER BY id
