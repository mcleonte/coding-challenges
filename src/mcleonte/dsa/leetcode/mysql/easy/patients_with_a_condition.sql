-- https://leetcode.com/problems/patients-with-a-condition/
-- https://leetcode.com/problems/patients-with-a-condition/discuss/2831333/MySQL-or-90-without-LIKE-clause
SELECT
  patient_id,
  patient_name,
  conditions
FROM patients
WHERE conditions REGEXP '\\bDIAB1'
