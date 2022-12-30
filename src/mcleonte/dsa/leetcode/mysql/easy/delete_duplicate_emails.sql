-- https://leetcode.com/problems/delete-duplicate-emails/
-- https://leetcode.com/problems/delete-duplicate-emails/discuss/2840308/MySQL-or-easiest-solution-without-SELECT-clause
DELETE person
FROM person
INNER JOIN person AS person2
WHERE person.email = person2.email
  AND person.id > person2.id
