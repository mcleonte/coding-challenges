-- https://leetcode.com/problems/capital-gainloss/
-- https://leetcode.com/problems/capital-gainloss/discuss/2825394/MySQL-or-greater97-with-simplest-solution-possible-or-use-IF-not-CASE
SELECT
  stock_name,
  SUM(IF(operation = 'Sell', price, -price)) AS capital_gain_loss
FROM stocks
GROUP BY stock_name
