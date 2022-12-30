-- https://leetcode.com/problems/customers-who-never-order/
-- https://leetcode.com/problems/customers-who-never-order/discuss/2831261/MySQL-or-98.77-407ms
SELECT customers.name AS customers
FROM customers
LEFT JOIN orders
  ON customers.id = orders.customerid
WHERE orders.customerid IS NULL
