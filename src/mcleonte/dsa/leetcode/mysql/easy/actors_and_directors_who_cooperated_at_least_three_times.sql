-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
SELECT
  actor_id,
  director_id
FROM
  actordirector
GROUP BY 1, 2
HAVING COUNT(timestamp) >= 3
