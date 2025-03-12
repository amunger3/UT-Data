--Simple Query with an ORDER BY
SELECT * 
FROM .Car_sales
ORDER BY Fuel_efficiency;

--All Manufactuers that have a 'b'
SELECT *
FROM [Cars].[dbo].[Car_sales]
WHERE MANUFACTURER LIKE '%b%';

--Top 10 Records
SELECT TOP 10 * 
FROM Cars.dbo.Car_sales;

--Engine size >= 1.8 Top 10
SELECT TOP 10 *
FROM Cars.dbo.Car_sales
WHERE Engine_size >= 1.8
ORDER BY Engine_size ASC;