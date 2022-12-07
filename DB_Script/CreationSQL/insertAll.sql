-- Execute: \. /home/ubuntu/DB_CREATE/CreationSQL/insertAll.sql
-- ############################# Entities #############################
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