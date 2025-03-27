SELECT 
D.MonthName, 
COUNT(*) AS TotalTrips, 
SUM(T.TotalAmount) AS TotalRevenue 
FROM dbo.Trip AS T
JOIN dbo.[Date] AS D
    ON T.[DateID]=D.[DateID]
GROUP BY D.MonthName; 
 

#SQL Code for Query 2: 
SELECT 
D.DayName, 
AVG(T.TripDurationSeconds) AS AvgDuration, 
AVG(T.TripDistanceMiles) AS AvgDistance 
FROM dbo.Trip AS T
JOIN dbo.[Date] AS D
    ON T.[DateID]=D.[DateID]
GROUP BY D.DayName;
 

#SQL Code for Query 3: 
SELECT TOP 10 
G.City, 
COUNT(*) AS TotalTrips 
FROM dbo.Trip AS T
JOIN dbo.Geography AS G
    ON T.PickupGeographyID=G.GeographyID
GROUP BY G.City
ORDER BY TotalTrips DESC;
 

SELECT TOP 10 
    G.City, 
    COUNT(*) AS TotalTrips 
FROM dbo.Trip AS T
JOIN dbo.Geography AS G
    ON T.DropoffGeographyID=G.GeographyID
GROUP BY G.City
ORDER BY TotalTrips DESC;