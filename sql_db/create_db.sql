CREATE DATABASE work_searches;
CREATE USER work_user  WITH PASSWORD 'admin';
ALTER ROLE work_user  SET client_encoding TO 'utf-8';
ALTER ROLE work_user  SET default_transaction_isolation TO 'read committed';
ALTER ROLE work_user  SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE work_searches TO work_user;