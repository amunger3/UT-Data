-- Selecting All
SELECT * FROM VegetableSales.dbo.annex1;
SELECT * FROM VegetableSales.dbo.annex2;
SELECT * FROM VegetableSales.dbo.annex3;
SELECT * FROM VegetableSales.dbo.annex4;

-- Altering a column
ALTER TABLE VegetableSales.dbo.annex3
ALTER COLUMN Item_Code bigint;

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