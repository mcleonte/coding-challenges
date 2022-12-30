-- https://leetcode.com/problems/rising-temperature/
-- https://leetcode.com/problems/rising-temperature/discuss/2831305/MySQL-or-97-373ms-with-ADDDATE-and-no-WHERE-clause
SELECT t.id
FROM Weather t
JOIN Weather y
ON t.recordDate = ADDDATE(y.recordDate,1)
AND t.temperature > y.temperature
