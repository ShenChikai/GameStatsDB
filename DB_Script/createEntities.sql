-- Execute: \. /home/ubuntu/DB_CREATE/createRelations.sql
-- **If were to drop all entities, must drop all relations first
DROP TABLE Game;
DROP TABLE Award;
DROP TABLE Company;
DROP TABLE Platform;
DROP TABLE Stock;

CREATE TABLE Game (
	GID int Primary Key,
	GName varchar(50) NOT NULL,
	Sales float(10,2),
	ReleaseDate datetime NOT NULL,
	IsF2P varchar(5)
);

CREATE TABLE Award (
	AID int Primary Key,
	AName varchar(30) NOT NULL,
	VotedByWho varchar(4) 
);

CREATE TABLE Company (
	CID int Primary Key,
	CName varchar(30) NOT NULL,
	MarketCap float(15,3),
	Earnings int,
	EmployeeCount int,
	Revenue float(15, 3),
	Country varchar(20)
);

CREATE TABLE Platform (
	PID int Primary key,
	PName varchar(10),
	FoundDate datetime
);

CREATE TABLE Stock (
	Ticker varchar(10) Primary Key,
	Country varchar(30),
	Exchange varchar(30) NOT NULL,
	HistoricalHigh float(10, 2),
	HistoricalLow float(10, 2),
	MarketCap int
);
