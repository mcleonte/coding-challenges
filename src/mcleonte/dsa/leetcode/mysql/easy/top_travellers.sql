-- https://leetcode.com/problems/top-travellers/
-- https://leetcode.com/problems/top-travellers/discuss/2825300/MySQL-or-use-COALESCE-instead-of-IFNULL
SELECT
  users.name,
  COALESCE(SUM(rides.distance), 0) AS travelled_distance
FROM users
LEFT JOIN rides
  ON users.id = rides.user_id
GROUP BY users.id
ORDER BY travelled_distance DESC, users.name ASC
