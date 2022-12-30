-- https://leetcode.com/problems/combine-two-tables/
-- https://leetcode.com/problems/combine-two-tables/discuss/2831219/MySQL-or-clean-solution-without-table-aliases
SELECT
  person.firstname,
  person.lastname,
  address.city,
  address.state
FROM person
LEFT JOIN address
  USING (personid)
