-- https://leetcode.com/problems/delete-duplicate-emails/
-- https://leetcode.com/problems/delete-duplicate-emails/discuss/2840308/MySQL-or-easiest-solution-without-SELECT-clause
DELETE p1
FROM Person p1
JOIN Person p2
WHERE p1.email = p2.email
AND p1.id > p2.id
