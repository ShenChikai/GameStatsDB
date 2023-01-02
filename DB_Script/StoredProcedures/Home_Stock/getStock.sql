-- Execute: \. /home/ubuntu/GameStatsDB/DB_Script/StoredProcedures/Home_Stock/getStock.sql
DELIMITER $$

-- Stored Procedure called in Home page

-- Get Stock data by <companyName>, <startDate>, <endDate>
CREATE PROCEDURE GetStock (companyName varchar(30), startDate date, endDate date)
BEGIN
	SELECT ttp.*
    FROM Company c
        JOIN CompanyHasStock ghs ON c.CID = ghs.CID
        JOIN Stock s ON ghs.Ticker = s.Ticker
        JOIN TimeTickerPrice ttp ON s.Ticker = ttp.Ticker
    WHERE c.CName = companyName AND ttp.Date >= startDate AND ttp.Date <= endDate;
END $$


-- Get Company Name that has a stock
CREATE PROCEDURE GetCompanyWithStock ()
BEGIN
	SELECT CName
    FROM Company c
        RIGHT JOIN CompanyHasStock ghs ON c.CID = ghs.CID
    ORDER BY c.MarketCap DESC;
END $$
-- Test:
-- SELECT ttp.*
--     FROM Company c
--         JOIN CompanyHasStock ghs ON c.CID = ghs.CID
--         JOIN Stock s ON ghs.Ticker = s.Ticker
--         JOIN TimeTickerPrice ttp ON s.Ticker = ttp.Ticker
--     WHERE c.CName = 'Microsoft' AND ttp.Date >= '2021-07-14' AND ttp.Date <= '2022-10-17';