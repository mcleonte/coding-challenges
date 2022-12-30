-- https://leetcode.com/problems/rising-temperature/
-- https://leetcode.com/problems/rising-temperature/discuss/2831305/MySQL-or-97-373ms-with-ADDDATE-and-no-WHERE-clause
SELECT weather.id
FROM weather
INNER JOIN weather AS yesterday
  ON weather.recorddate = ADDDATE(yesterday.recorddate, 1)
    AND weather.temperature > yesterday.temperature
