SELECT 'Users' AS table_name, id, user_id, NULL AS store_name, general_stamps AS data1, NULL AS data2, NULL AS data3 
FROM users
UNION ALL
SELECT 'Stores' AS table_name, id, NULL AS user_id, store_name, NULL AS data1, NULL AS data2, NULL AS data3 
FROM stores
UNION ALL
SELECT 'Purchases' AS table_name, id, NULL AS user_id, NULL AS store_name, store_stamps AS data1, purchase_count AS data2, last_purchase AS data3 
FROM purchases;



