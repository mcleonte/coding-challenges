-- https://leetcode.com/problems/group-sold-products-by-the-date/
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY 1
ORDER BY 1
