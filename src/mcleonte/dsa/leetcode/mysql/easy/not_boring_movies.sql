-- https://leetcode.com/problems/not-boring-movies/
-- https://leetcode.com/problems/not-boring-movies/discuss/2837414/MySQL-or-greater94-fastest-solution-with-Bitwise-AND
SELECT
  id,
  movie,
  description,
  rating
FROM cinema
WHERE id & 1 = 1
  AND description != 'boring'
ORDER BY rating DESC
