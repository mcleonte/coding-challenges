-- https://leetcode.com/problems/find-customer-referee/submissions/
-- https://leetcode.com/problems/find-customer-referee/discuss/2834404/MySQL-or-99.53-426ms

-- v1
SELECT name
FROM Customer
WHERE referee_id IS NULL
OR referee_id <> 2;

-- v2
SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) <> 2;
