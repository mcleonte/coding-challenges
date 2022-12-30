-- https://leetcode.com/problems/top-travellers/
-- https://leetcode.com/problems/top-travellers/discuss/2825300/MySQL-or-use-COALESCE-instead-of-IFNULL
SELECT
    u.name,
    COALESCE(SUM(r.distance),0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC
