-- Inner join between player seasons and player information on playerID
SELECT b.[playerID], b.[yearID], b.[teamID], b.[H], b.[2B], b.[RBI], p.*
FROM Baseball.dbo.Batting b
INNER JOIN People p on b.playerID = p.playerID;

-- Selecting players that changed teams more than once in a year
SELECT b.[playerID], b.[yearID], b.[teamID], b.[stint], b.[H], b.[2B], b.[RBI]
FROM Baseball.dbo.Batting b
WHERE stint = 3;

-- Left outer join example (many-to-one)
SELECT b.[playerID], b.[stint], b.[yearID], b.[teamID], b.[H], b.[2B], b.[RBI], t.*
FROM Baseball.dbo.Batting AS b
LEFT OUTER JOIN Teams t ON t.teamID = b.teamID and t.yearID = b.yearID;

-- Right outer join example (many-to-one)
SELECT b.[playerID],b.[stint], b.[yearID], b.[teamID], b.[H], b.[2B], b.[RBI], t.*
FROM Baseball.dbo.Batting as b
RIGHT OUTER JOIN Teams as t on b.teamID = t.teamID and b.yearID = t.yearID

-- Multiple Inner Joins example
USE Baseball
GO

SELECT *
FROM Batting b
INNER JOIN People p on b.playerID = p.playerID
INNER JOIN Pitching pit on b.playerID = pit.playerID AND b.teamID = pit.teamID AND b.yearID = pit.yearID
INNER JOIN Teams t on b.teamID = t.teamID AND b.yearID = t.yearID

-- Quad Join Example
SELECT *
FROM Batting b
INNER JOIN People p on b.playerID = p.playerID
INNER JOIN Pitching pit on b.playerID = pit.playerID and b.teamID = pit.teamID and b.yearID = pit.yearID
INNER JOIN Teams t on b.teamID = t.teamID and b.yearID = t.yearID
INNER JOIN TeamsFranchises  tf on t.franchID = tf.franchID