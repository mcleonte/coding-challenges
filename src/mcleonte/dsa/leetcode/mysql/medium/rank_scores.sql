-- https://leetcode.com/problems/rank-scores/
-- https://leetcode.com/problems/rank-scores/discuss/2951484/MySQL-or-greater99-with-shortest-solution
SELECT
  score,
  DENSE_RANK() OVER(ORDER BY score DESC) AS `rank`
FROM scores
