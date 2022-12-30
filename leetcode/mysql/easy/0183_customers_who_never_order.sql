-- https://leetcode.com/problems/customers-who-never-order/
-- https://leetcode.com/problems/customers-who-never-order/discuss/2831261/MySQL-or-98.77-407ms
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL
