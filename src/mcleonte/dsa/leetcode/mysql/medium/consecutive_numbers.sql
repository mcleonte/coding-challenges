-- https://leetcode.com/problems/consecutive-numbers/
-- https://leetcode.com/problems/consecutive-numbers/discuss/2951540/MySQL-or-simple-2-joins
SELECT DISTINCT logs.num AS consecutivenums
FROM logs

INNER JOIN logs AS prv
  ON logs.num = prv.num
    AND logs.id = prv.id + 1

INNER JOIN logs AS nxt
  ON logs.num = nxt.num
    AND logs.id = nxt.id - 1
