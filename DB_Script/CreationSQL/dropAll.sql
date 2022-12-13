-- Execute: \. /home/ubuntu/DB_CREATE/CreationSQL/dropAll.sql
-- Drop all Relations and Entities in the Database
-- This is included for testing purpose
-- Must drop relations first due to foreign key dependencies
DROP TABLE GameNominatedByAward;
DROP TABLE GameHasGenre;
DROP TABLE CompanyOwnsPlatform;
DROP TABLE CompanyOwnsGame;
DROP TABLE PlatformHostsGame;
DROP TABLE GameIsAvailableOn;
DROP TABLE CompanyHasStock;
DROP TABLE TimeTickerPrice;

DROP TABLE Game;
DROP TABLE Award;
DROP TABLE Company;
DROP TABLE Platform;
DROP TABLE Stock;