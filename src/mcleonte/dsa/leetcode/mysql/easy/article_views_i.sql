-- https://leetcode.com/problems/article-views-i/
-- https://leetcode.com/problems/article-views-i/discuss/2825204/MySQL-or-greater95-with-simplest-approach
SELECT DISTINCT author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY id
