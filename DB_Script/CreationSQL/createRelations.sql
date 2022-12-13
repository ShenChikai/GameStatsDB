-- Execute: \. /home/ubuntu/DB_CREATE/CreationSQL/createRelations.sql
-- Create all Relations in the database
CREATE TABLE GameNominatedByAward (
	GID int,
	AID int,
	YearNominated int,
	DidWin int,

	FOREIGN KEY (GID) REFERENCES Game(GID),
	FOREIGN KEY (AID) REFERENCES Award(AID)
);

CREATE TABLE GameHasGenre (
	GID int,
	Genre varchar(50) NOT NULL,

	FOREIGN KEY (GID) REFERENCES Game(GID)
);

CREATE TABLE CompanyOwnsPlatform (
	CID int,
	PID int,
	StartDate datetime,

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (PID) REFERENCES Platform(PID)
);

CREATE TABLE CompanyOwnsGame (
	CID int,
	GID int,

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (GID) REFERENCES Game(GID)
);

CREATE TABLE PlatformHostsGame (
	PID int,
	GID int,

	FOREIGN KEY (PID) REFERENCES Platform(PID),
	FOREIGN KEY (GID) REFERENCES Game(GID)
);

CREATE TABLE GameIsAvailableOn (
	GID int,
	OS VARCHAR(50),

	FOREIGN KEY (GID) REFERENCES Game(GID)
);

CREATE TABLE CompanyHasStock (
	CID int,
	Ticker varchar(10),

	FOREIGN KEY (CID) REFERENCES Company(CID),
	FOREIGN KEY (Ticker) REFERENCES Stock(Ticker)
);


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

