-- https://leetcode.com/problems/sales-analysis-iii/
SELECT
  product_id,
  product.product_name
FROM product
INNER JOIN sales
  USING (product_id)
GROUP BY product_id
HAVING MIN(sales.sale_date) >= '2019-01-01'
  AND MAX(sales.sale_date) <= '2019-03-31'
