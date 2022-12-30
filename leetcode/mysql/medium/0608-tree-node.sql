-- https://leetcode.com/problems/tree-node/
-- https://leetcode.com/problems/tree-node/discuss/2825360/MySQL-or-greater97-with-simplest-solution-possible
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id from Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
ORDER BY id
