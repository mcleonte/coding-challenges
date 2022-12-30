-- https://leetcode.com/problems/combine-two-tables/
-- https://leetcode.com/problems/combine-two-tables/discuss/2831219/MySQL-or-clean-solution-without-table-aliases
SELECT
    firstName,
    lastName,
    city,
    state
FROM Person
LEFT JOIN Address
USING(personId)
