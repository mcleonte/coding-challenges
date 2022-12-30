-- https://leetcode.com/problems/exchange-seats/submissions/
SELECT
    id + IF(id & 1, (id != (SELECT COUNT(id) FROM Seat)), -1) AS id,
    student
FROM Seat
ORDER BY id
