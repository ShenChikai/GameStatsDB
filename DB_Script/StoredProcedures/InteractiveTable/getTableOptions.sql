-- Execute: \. /home/ubuntu/DB_CREATE/StoredProcedures/InteractiveTable/getTableOptions.sql
DELIMITER $$

-- Get All Options for Table
CREATE PROCEDURE GetAllTableOptions ()
BEGIN
    -- Get Game list
	SELECT GName
    FROM Game g
    ORDER BY Sales DESC;
    -- Get Genre list
    SELECT UNIQUE Genre
    FROM GameHasGenre;
    -- Get Platform list
    SELECT PName
    FROM Platform;
    -- Get Award list
    SELECT AName
    FROM Award;
END $$

-- Get OS list (GameName, Genre, Platform, OS, DESC/ASC)
CREATE PROCEDURE InteractiveTableSearch (GName varchar(50), GType varchar(50), 
                                        PName varchar(10), AName varchar(30), IsDesc varchar(8))
BEGIN
	IF IsDesc = 'True' THEN
        IF AName = '' THEN
            SELECT UNIQUE (g.GName AS 'Game', g.Sales, g.ReleaseDate AS 'Release Date', g.IsF2P AS 'F2P', 
                    c.CName AS 'Company', c.MarketCap, c.Country,
                    a.AName AS 'Award', gnba.YearNominated AS 'Year Nominated', gnba.DidWin AS 'Won')
            FROM Game g
                LEFT JOIN GameHasGenre ghg ON ghg.GID = g.GID
                LEFT JOIN PlatformHostsGame phg ON phg.GID = g.GID
                LEFT JOIN Platform p ON p.PID = phg.PID
                LEFT JOIN CompanyOwnsGame cog ON cog.GID = g.GID
                LEFT JOIN Company c ON c.CID = cog.CID
                LEFT JOIN GameNominatedByAward gnba ON gnba.GID = g.GID
                LEFT JOIN Award a on a.AID = gnba.AID
            WHERE g.GName LIKE CONCAT('%', GName, '%') AND ghg.Genre LIKE CONCAT('%', GType, '%')
                AND p.PName LIKE CONCAT('%', PName, '%')
            ORDER BY g.Sales DESC;
        ELSE
            SELECT UNIQUE (g.GName AS 'Game', g.Sales, g.ReleaseDate AS 'Release Date', g.IsF2P AS 'F2P', 
                    c.CName AS 'Company', c.MarketCap, c.Country,
                    a.AName AS 'Award', gnba.YearNominated AS 'Year Nominated', gnba.DidWin AS 'Won')
            FROM Game g
                LEFT JOIN GameHasGenre ghg ON ghg.GID = g.GID
                LEFT JOIN PlatformHostsGame phg ON phg.GID = g.GID
                LEFT JOIN Platform p ON p.PID = phg.PID
                LEFT JOIN CompanyOwnsGame cog ON cog.GID = g.GID
                LEFT JOIN Company c ON c.CID = cog.CID
                LEFT JOIN GameNominatedByAward gnba ON gnba.GID = g.GID
                LEFT JOIN Award a on a.AID = gnba.AID
            WHERE g.GName LIKE CONCAT('%', GName, '%') AND ghg.Genre LIKE CONCAT('%', GType, '%')
                AND p.PName LIKE CONCAT('%', PName, '%') AND a.AName LIKE CONCAT('%', AName, '%')
            ORDER BY g.Sales DESC;
        END IF;
        
    ELSE
        IF AName = '' THEN
            SELECT UNIQUE (g.GName AS 'Game', g.Sales, g.ReleaseDate AS 'Release Date', g.IsF2P AS 'F2P', 
                    c.CName AS 'Company', c.MarketCap, c.Country,
                    a.AName AS 'Award', gnba.YearNominated AS 'Year Nominated', gnba.DidWin AS 'Won')
            FROM Game g
                LEFT JOIN GameHasGenre ghg ON ghg.GID = g.GID
                LEFT JOIN PlatformHostsGame phg ON phg.GID = g.GID
                LEFT JOIN Platform p ON p.PID = phg.PID
                LEFT JOIN CompanyOwnsGame cog ON cog.GID = g.GID
                LEFT JOIN Company c ON c.CID = cog.CID
                LEFT JOIN GameNominatedByAward gnba ON gnba.GID = g.GID
                LEFT JOIN Award a on a.AID = gnba.AID
            WHERE g.GName LIKE CONCAT('%', GName, '%') AND ghg.Genre LIKE CONCAT('%', GType, '%')
                AND p.PName LIKE CONCAT('%', PName, '%')
            ORDER BY g.Sales ASC;
        ELSE
            SELECT UNIQUE (g.GName AS 'Game', g.Sales, g.ReleaseDate AS 'Release Date', g.IsF2P AS 'F2P', 
                    c.CName AS 'Company', c.MarketCap, c.Country,
                    a.AName AS 'Award', gnba.YearNominated AS 'Year Nominated', gnba.DidWin AS 'Won')
            FROM Game g
                LEFT JOIN GameHasGenre ghg ON ghg.GID = g.GID
                LEFT JOIN PlatformHostsGame phg ON phg.GID = g.GID
                LEFT JOIN Platform p ON p.PID = phg.PID
                LEFT JOIN CompanyOwnsGame cog ON cog.GID = g.GID
                LEFT JOIN Company c ON c.CID = cog.CID
                LEFT JOIN GameNominatedByAward gnba ON gnba.GID = g.GID
                LEFT JOIN Award a on a.AID = gnba.AID
            WHERE g.GName LIKE CONCAT('%', GName, '%') AND ghg.Genre LIKE CONCAT('%', GType, '%')
                AND p.PName LIKE CONCAT('%', PName, '%') AND a.AName LIKE CONCAT('%', AName, '%')
            ORDER BY g.Sales ASC;
        END IF;
    END IF;
END $$


-- CALL InteractiveTableSearch('','','','','True');

 SELECT g.GName AS 'Game', g.Sales, g.ReleaseDate AS 'Release Date', g.IsF2P AS 'F2P', 
                    c.CName AS 'Company', c.MarketCap, c.Country,
                    a.AName AS 'Award', gnba.YearNominated AS 'Year Nominated', gnba.DidWin AS 'Won'
            FROM Game g
                LEFT JOIN GameHasGenre ghg ON ghg.GID = g.GID
                LEFT JOIN PlatformHostsGame phg ON phg.GID = g.GID
                LEFT JOIN Platform p ON p.PID = phg.PID
                LEFT JOIN CompanyOwnsGame cog ON cog.GID = g.GID
                LEFT JOIN Company c ON c.CID = cog.CID
                LEFT JOIN GameNominatedByAward gnba ON gnba.GID = g.GID
                LEFT JOIN Award a on a.AID = gnba.AID
            ORDER BY g.Sales DESC;