-- Execute: \. /home/ubuntu/GameStatsDB/DB_Script/CreationSQL/createEntities.sql
-- Create all Entities in the Database
-- **If were to drop all entities, must drop all relations first

-- Create table for entity Game
CREATE TABLE Game (
	GID int Primary Key,
	GName varchar(50) NOT NULL,
	Sales float(10,2),
	ReleaseDate datetime NOT NULL,
	IsF2P varchar(5)
);

-- Create table for entity Award
CREATE TABLE Award (
	AID int Primary Key,
	AName varchar(30) NOT NULL,
	VotedByWho varchar(4) 
);

-- Create table for entity Company
CREATE TABLE Company (
	CID int Primary Key,
	CName varchar(30) NOT NULL,
	MarketCap float(15,3),
	Earnings int,
	EmployeeCount int,
	Revenue float(15, 3),
	Country varchar(20)
);

-- Create table for entity Platform
CREATE TABLE Platform (
	PID int Primary key,
	PName varchar(10),
	FoundDate datetime
);

-- Create table for entity Stock
CREATE TABLE Stock (
	Ticker varchar(10) Primary Key,
	Country varchar(30),
	Exchange varchar(30) NOT NULL,
	FiftyTwoWeekHigh float(10, 2),
	FiftyTwoWeekLow float(10, 2),
	Market varchar(10)
);
