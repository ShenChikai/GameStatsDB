-- Execute: \. /home/ubuntu/GameStatsDB/DB_Script/CreationSQL/createRelations.sql
-- Create all Relations in the database

-- Create table for relation GameNominatedByAward
CREATE TABLE GameNominatedByAward (
	GID int,
	AID int,
	YearNominated int,
	DidWin int,

	FOREIGN KEY (GID) REFERENCES Game(GID),
	FOREIGN KEY (AID) REFERENCES Award(AID)
);

-- Create table for relation GameHasGenre
CREATE TABLE GameHasGenre (
	GID int,
	Genre varchar(50) NOT NULL,

	FOREIGN KEY (GID) REFERENCES Game(GID)
);

-- Create table for relation CompanyOwnsPlatform
CREATE TABLE CompanyOwnsPlatform (
	CID int,
	PID int,
	StartDate datetime,

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (PID) REFERENCES Platform(PID)
);

-- Create table for relation CompanyOwnsGame
CREATE TABLE CompanyOwnsGame (
	CID int,
	GID int,

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (GID) REFERENCES Game(GID)
);

-- Create table for relation PlatformHostsGame
CREATE TABLE PlatformHostsGame (
	PID int,
	GID int,

	FOREIGN KEY (PID) REFERENCES Platform(PID),
	FOREIGN KEY (GID) REFERENCES Game(GID)
);

-- Create table for relation GameIsAvailableOn
CREATE TABLE GameIsAvailableOn (
	GID int,
	OS VARCHAR(50),

	FOREIGN KEY (GID) REFERENCES Game(GID)
);

-- Create table for relation CompanyHasStock
CREATE TABLE CompanyHasStock (
	CID int,
	Ticker varchar(10),

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (Ticker) REFERENCES Stock(Ticker)
);

-- Create table for relation TimeTickerPrice
CREATE TABLE TimeTickerPrice (
	Date datetime,
	Ticker varchar(10),
	Open float(10,2),
	High float(10,2),
	Low float(10,2),
	Close float(10,2),
	Adj_Close float(10,2),
	Volume float(12,2),

	FOREIGN KEY (Ticker) REFERENCES Stock(Ticker)
);

