-- Creating a view
CREATE VIEW vw_cars
AS SELECT TOP(50) * 
FROM [Cars].[dbo].Car_sales;