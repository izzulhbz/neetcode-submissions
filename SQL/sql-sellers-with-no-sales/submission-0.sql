-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT s.seller_name 
    FROM seller
    INNER JOIN orders o
    ON s.seller_id = o.seller_id
    WHERE o.sale_date >= '2020-01-01' AND o.sale_date <= '2020-12-31'
)
ORDER BY s.seller_name ASC