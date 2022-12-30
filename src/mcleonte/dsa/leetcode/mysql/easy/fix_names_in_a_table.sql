-- https://leetcode.com/problems/fix-names-in-a-table/
-- https://leetcode.com/problems/fix-names-in-a-table/discuss/2828590/MySQL-or-greater96
SELECT
  user_id,
  CONCAT(
    UPPER(LEFT(name, 1)),
    LOWER(RIGHT(name, LENGTH(name) - 1))
  ) AS name
FROM users
ORDER BY user_id
