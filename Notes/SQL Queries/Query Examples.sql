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

--Vehicle type, average price in thousands, group by vehicle type (with a CAST)
SELECT Vehicle_type, AVG(CAST(Price_in_thousands AS MONEY)) AS Avg_Price
FROM dbo.Car_sales
GROUP BY Vehicle_type;

--Vehicle type, average price in thousands group by vehicle type with a CAST and with a WHERE clause
SELECT Vehicle_type, AVG(CAST(Price_in_thousands AS MONEY)) AS Avg_Price
FROM dbo.Car_sales
WHERE Engine_size >= 3
GROUP BY Vehicle_type;

--Subquery basics
SELECT TOP 5 Manufacturer, Model, Horsepower
FROM dbo.Car_sales
WHERE Horsepower >= (SELECT AVG(CAST(Horsepower AS INT)) FROM dbo.Car_sales)
ORDER BY Horsepower DESC;

-- Compare Fuel_efficiency to performance ratio (in query calculation)
SELECT Manufacturer, Model, 
       Fuel_efficiency, 
       Horsepower,
       (cast(Horsepower as int) / cast(Fuel_efficiency as int)) AS Power_Ratio
FROM dbo.Car_sales
where Fuel_efficiency > 0
ORDER BY Power_Ratio DESC