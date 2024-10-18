-- Database: tableau-embeded

-- DROP DATABASE IF EXISTS "tableau-embeded";

CREATE DATABASE tableauembeded
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- SCHEMA: metadata
\c tableauembeded
-- DROP SCHEMA IF EXISTS metadata ;

CREATE SCHEMA IF NOT EXISTS metadata
    AUTHORIZATION postgres;

-- Table: metadata.users

-- DROP TABLE IF EXISTS metadata.users;

CREATE TABLE IF NOT EXISTS metadata.users
(
    id uuid NOT NULL,
    firstname text COLLATE pg_catalog."default" NOT NULL,
    lastname text COLLATE pg_catalog."default",
    username text COLLATE pg_catalog."default" NOT NULL,
    passworduser text COLLATE pg_catalog."default" NOT NULL,
    email text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT uniq_email UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS metadata.users
    OWNER to postgres;