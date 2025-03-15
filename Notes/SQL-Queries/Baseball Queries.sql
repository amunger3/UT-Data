-- Inner join between player seasons and player information on playerID
SELECT b.[playerID], b.[yearID], b.[teamID], b.[H], b.[2B], b.[RBI], p.*
FROM Baseball.dbo.Batting b
INNER JOIN People p on b.playerID = p.playerID;

-- Selecting players that changed teams more than once in a year
SELECT b.[playerID], b.[yearID], b.[teamID], b.[stint], b.[H], b.[2B], b.[RBI]
FROM Baseball.dbo.Batting b
WHERE stint = 3;