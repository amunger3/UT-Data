--Correlation coefficient
SELECT
    (COUNT(*) * SUM(cast(Curb_weight as float) * cast(Sales_in_thousands as money)) - SUM(cast(Curb_weight as float)) * SUM(cast(Sales_in_thousands as money))) / 
    (
        SQRT(COUNT(*) * SUM(cast(Curb_weight as float) * cast(Curb_weight as float)) - SUM(cast(Curb_weight as float)) * SUM(cast(Curb_weight as float))) * 
        SQRT(COUNT(*) * SUM(cast(Sales_in_thousands as money) * cast(Sales_in_thousands as money)) - SUM(cast(Sales_in_thousands as money)) * SUM(cast(Sales_in_thousands as money)))
    ) AS correlation_coefficient
FROM Car_sales
WHERE Curb_weight IS NOT NULL AND Sales_in_thousands IS NOT NULL;