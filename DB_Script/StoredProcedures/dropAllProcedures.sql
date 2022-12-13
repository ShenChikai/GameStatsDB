-- To view available stored procedures:
--     SHOW PROCEDURE STATUS WHERE db = 'GameStats';

-- Drop All stored procedures
-- This is included for testing purpose
-- execute: \. /home/ubuntu/DB_CREATE/StoredProcedures/dropAllProcedures.sql

-- Market Shares
DROP PROCEDURE IF EXISTS GenreShare;
DROP PROCEDURE IF EXISTS PlatformShare;
DROP PROCEDURE IF EXISTS OSShare;
DROP PROCEDURE IF EXISTS CompanyMCShare;
-- Home Page Stock Related
DROP PROCEDURE IF EXISTS GetStock;
DROP PROCEDURE IF EXISTS GetCompanyWithStock;
-- Interactive Table
DROP PROCEDURE IF EXISTS GetAllTableOptions;
DROP PROCEDURE IF EXISTS InteractiveTableSearch;