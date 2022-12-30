-- https://leetcode.com/problems/patients-with-a-condition/
-- https://leetcode.com/problems/patients-with-a-condition/discuss/2831333/MySQL-or-90-without-LIKE-clause
SELECT *
FROM Patients
WHERE conditions REGEXP '\\bDIAB1'
