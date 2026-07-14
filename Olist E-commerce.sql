CREATE DATABASE analysis;
USE analysis;
SHOW TABLES;
SELECT COUNT(*)
FROM orders;
SELECT COUNT(*)
FROM order_items;

SELECT order_status,COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_status;

SELECT COUNT(o.order_id) AS total_order,c.customer_state
FROM customers c 
INNER JOIN orders o 
	ON c.customer_id=o.customer_id
GROUP BY c.customer_state
ORDER BY total_order DESC;

SELECT ROUND(SUM(price),2)
FROM order_items;

SELECT p.product_category_name,SUM(oi.price) AS total
FROM products p
INNER JOIN order_items oi
	ON p.product_id=oi.product_id
GROUP BY p.product_category_name
ORDER BY total DESC;


SELECT ROUND(AVG(order_total),2) AS AOV
FROM(
	SELECT SUM(price) AS order_total,
    order_id
    FROM order_items
    GROUP BY order_id
    )
    AS order_totals

SELECT YEAR(order_purchase_timestamp) AS order_year,
MONTH(order_purchase_timestamp) AS order_month,
COUNT(order_id) AS total_order
FROM orders
GROUP BY order_year,order_month
ORDER BY order_year,order_month;

SELECT YEAR(order_purchase_timestamp) AS order_year,
COUNT(order_id) AS total_order
FROM orders
GROUP BY order_year
ORDER BY order_year;

SELECT YEAR(o.order_purchase_timestamp) AS order_year,
SUM(oi.price) AS total_revenue
FROM orders o
INNER JOIN order_items oi ON o.order_id=oi.order_id
GROUP BY order_year
ORDER BY order_year;

SELECT AVG(DATEDIFF(order_delivered_customer_date,
                order_purchase_timestamp)) AS avg_delivery_date
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;

SELECT 
	CASE
		WHEN order_estimated_delivery_date>=order_delivered_customer_date THEN "ON TIME"
		WHEN order_estimated_delivery_date<order_delivered_customer_date THEN "LATE"
	END AS delivery_status,
		COUNT(*) AS total_orders
FROM orders
WHERE order_delivered_customer_date IS NOT NULL
GROUP BY delivery_status

