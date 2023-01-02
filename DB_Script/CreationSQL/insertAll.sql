-- Execute: \. /home/ubuntu/GameStatsDB/DB_Script/CreationSQL/insertAll.sql
-- ############################# Entities #############################

-- Code for insert all the data from CSV format

-- Game
-- 1,007: Quantum of Solace,3.3,2008/10/31,FALSE
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/Game.csv'
INTO TABLE Game
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(GID, GName, @Sales, @ReleaseDate, IsF2P)
SET Sales = CAST(@Sales AS DECIMAL(10,2)),
ReleaseDate = DATE_FORMAT(@ReleaseDate, '%Y/%m/%d');

-- Award
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/Award.csv'
INTO TABLE Award
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Company 
-- 0, 11 bit studios, 260017093.0, 8147710, 192, 17777847.0, Poland
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/Company.csv'
INTO TABLE Company
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Platform
-- 1,3DS,2011-02-26
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/Platform.csv'
INTO TABLE Platform
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(PID, PName, @FoundDate)
SET FoundDate = DATE_FORMAT(@FoundDate, '%Y-%m-%d');

-- Stock
-- ATVI,United States,NMS,86.9,57.47,us_market
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/Stock.csv'
INTO TABLE Stock
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Ticker,Country,Exchange,@FiftyTwoWeekHigh,@FiftyTwoWeekLow,Market)
SET FiftyTwoWeekHigh = CAST(@FiftyTwoWeekHigh AS DECIMAL(10,2)),
FiftyTwoWeekLow = CAST(@FiftyTwoWeekLow AS DECIMAL(10,2));

-- ############################# Relations #############################
-- GameNominatedByAward 
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/GameNominatedByAward.csv'
INTO TABLE GameNominatedByAward
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- GameHasGenre  
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/GameHasGenre.csv'
INTO TABLE GameHasGenre
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- CompanyOwnsGame  
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/CompanyOwnsGame.csv'
INTO TABLE CompanyOwnsGame
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- CompanyOwnsPlatform 
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/CompanyOwnsPlatform.csv'
INTO TABLE CompanyOwnsPlatform
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- PlatformHostsGame  
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/PlatformHostsGame.csv'
INTO TABLE PlatformHostsGame
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- GameIsAvailableOn  
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/GameIsAvailableOn.csv'
INTO TABLE GameIsAvailableOn
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- CompanyHasStock  
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/CompanyHasStock.csv'
INTO TABLE CompanyHasStock
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- TimeTickerPrice  
-- 2020-12-07,4751.T,1710.0,1755.0,1705.0,1705.0,1677.94189453125,2498400
LOAD DATA LOCAL INFILE '/home/ubuntu/DB_CREATE/CSV_Data/TimeTickerPrice.csv'
INTO TABLE TimeTickerPrice
FIELDS TERMINATED BY ','
ENCLOSED BY ''
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Date,Ticker, @Open, @High, @Low, @Close, @Adj_Close, Volume)
SET Date = DATE_FORMAT(@Date, '%Y-%m-%d'),
Open = CAST(@Open AS DECIMAL(10,2)),
High = CAST(@High AS DECIMAL(10,2)),
Low = CAST(@Low AS DECIMAL(10,2)),
Close = CAST(@Close AS DECIMAL(10,2)),
Adj_Close = CAST(@Adj_Close AS DECIMAL(10,2))
;