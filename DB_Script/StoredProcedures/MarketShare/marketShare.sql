-- Execute: \. /home/ubuntu/GameStatsDB/DB_Script/StoredProcedures/MarketShare/marketShare.sql

-- Stored Procedure called in MarketShare page

DELIMITER $$
-- Genre Share
CREATE PROCEDURE GenreShare ()
BEGIN
	SELECT Genre, Share/Total AS PercentShare, Share, Total
    FROM (
        SELECT Genre, count(GID) AS Share
        FROM GameHasGenre
        GROUP BY Genre
    ) AS Shares,
    (
        SELECT count(GID) AS Total
        FROM GameHasGenre
    ) AS TotalShares
    ORDER BY Share DESC;
END $$

-- Platform Share
CREATE PROCEDURE PlatformShare ()
BEGIN
	SELECT PName, Share/Total AS PercentShare, Share, Total
    FROM (
        SELECT PName, count(GID) AS Share
        FROM Platform p
        JOIN PlatformHostsGame phg ON p.PID = phg.PID
        GROUP BY phg.PID
    ) AS Shares,
    (
        SELECT count(GID) AS Total
        FROM PlatformHostsGame
    ) AS TotalShares
    ORDER BY Share DESC;
END $$

-- OS Share
CREATE PROCEDURE OSShare ()
BEGIN
	SELECT OS, Share/Total AS PercentShare, Share, Total
    FROM (
        SELECT OS, count(GID) AS Share
        FROM GameIsAvailableOn
        GROUP BY OS
    ) AS Shares,
    (
        SELECT count(GID) AS Total
        FROM GameIsAvailableOn
    ) AS TotalShares
    ORDER BY Share DESC;
END $$

-- CompanyMC Share
CREATE PROCEDURE CompanyMCShare ()
BEGIN
	SELECT CName, MarketCap/Total AS PercentShare, MarketCap, Total
    FROM Company,
    (
        SELECT sum(MarketCap) AS Total
        FROM Company
    ) AS TotalMC
    ORDER BY MarketCap DESC;
END $$