--Simple Query with an ORDER BY
SELECT * 
FROM .Car_sales
ORDER BY Fuel_efficiency;

--All Manufactuers that have a 'b'
SELECT *
FROM [Cars].[dbo].[Car_sales]
WHERE MANUFACTURER LIKE '%b%';