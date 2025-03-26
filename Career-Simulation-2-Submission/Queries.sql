-- Selecting All
SELECT * FROM VegetableSales.dbo.annex1;
SELECT * FROM VegetableSales.dbo.annex2;
SELECT * FROM VegetableSales.dbo.annex3;
SELECT * FROM VegetableSales.dbo.annex4;

-- Altering a column
ALTER TABLE VegetableSales.dbo.annex3
ALTER COLUMN Item_Code bigint;

-- Top Quantity Sold by Date (Total Sales Over Time) (*deliverable*)
SELECT Date, SUM(Quantity_Sold_kilo) AS Qty_Sold From VegetableSales.dbo.annex2
GROUP BY Date
ORDER BY Qty_Sold DESC;

-- Sales by product category (*deliverable*)
SELECT SUM(Wholesale_Price_RMB_kg) AS Total_Sales, Category_Code
FROM VegetableSales.dbo.annex3
INNER JOIN VegetableSales.dbo.annex1 ON VegetableSales.dbo.annex3.Item_Code = VegetableSales.dbo.annex1.Item_Code
GROUP BY Category_Code
ORDER BY Total_Sales DESC;

-- Total Sales Table (*deliverable*)
SELECT 
	Item_Code, 
	SUM(Quantity_Sold_kilo) AS Total_Qty_Sold, 
	AVG(Unit_Selling_Price_RMB_kg) AS Unit_Price,
	(SUM(Quantity_Sold_kilo) * AVG(Unit_Selling_Price_RMB_kg)) AS Total_Sales_$
FROM VegetableSales.dbo.annex2
GROUP BY Item_Code
ORDER BY Total_Sales_$ DESC;

-- Total Sales Value Per Customer Transaction (*deliverable*)
SELECT 
	Date, 
	Time, 
	Item_Code, 
	Quantity_Sold_kilo, 
	Unit_Selling_Price_RMB_kg, 
	Sale_or_Return, 
	Discount_Yes_No, 
	(Quantity_Sold_kilo * Unit_Selling_Price_RMB_kg) AS Sales_Value
FROM VegetableSales.dbo.annex2
ORDER BY Sales_Value DESC;

-- Joining Item and Category Names to Item Codes for readability
SELECT Date,  VegetableSales.dbo.annex3.Item_Code, Wholesale_Price_RMB_kg, Category_Code, Category_Name, Item_Name
FROM VegetableSales.dbo.annex3
INNER JOIN VegetableSales.dbo.annex1 ON VegetableSales.dbo.annex3.Item_Code = VegetableSales.dbo.annex1.Item_Code;

-- Grouping By Item Code
SELECT Item_Code,
        SUM(Quantity_Sold_kilo) AS Qty_Sold, 
        AVG(Unit_Selling_Price_RMB_kg) AS Unit_Price 
    FROM VegetableSales.dbo.annex2
GROUP BY Item_Code
ORDER BY Qty_Sold DESC;

-- Inner joining product information with sales information
SELECT a1.*, a2.[Quantity_Sold_kilo], a2.[Unit_Selling_Price_RMB_kg]
FROM VegetableSales.dbo.annex2 a2
INNER JOIN VegetableSales.dbo.annex1 a1 on a2.Item_Code = a1.Item_Code;

-- Most Expensive Vegetables
SELECT a1.*, a2.[Quantity_Sold_kilo], a2.[Unit_Selling_Price_RMB_kg]
FROM VegetableSales.dbo.annex2 a2
INNER JOIN VegetableSales.dbo.annex1 a1 on a2.Item_Code = a1.Item_Code
ORDER BY Unit_Selling_Price_RMB_kg DESC;