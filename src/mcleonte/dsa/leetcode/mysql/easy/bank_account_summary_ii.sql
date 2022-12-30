-- https://leetcode.com/problems/bank-account-summary-ii/
SELECT
  users.name,
  SUM(transactions.amount) AS balance
FROM users
INNER JOIN transactions
  USING (account)
GROUP BY users.account
HAVING balance > 10000
