-- To view available stored procedures:
--     SHOW PROCEDURE STATUS WHERE db = 'GameStats';

-- Drop All stored procedures
-- execute: \. /home/ubuntu/DB_CREATE/StoredProcedures/dropAllProcedures.sql
-- Market Shares
DROP PROCEDURE IF EXISTS GenreShare;
DROP PROCEDURE IF EXISTS PlatformShare;
DROP PROCEDURE IF EXISTS OSShare;
DROP PROCEDURE IF EXISTS CompanyMCShare;