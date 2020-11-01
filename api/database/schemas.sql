-- DROP TABLE IF EXISTS initiators;

CREATE TABLE initiators (
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email TEXT NOT NULL
);

-- CREATE TABLE profiles (
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     profileUrl TEXT NOT NULL,
--     email TEXT 
-- );

-- CREATE TABLE requests (
--     requestId INTEGER NOT NULL,
--     initiatorId TEXT NOT NULL
-- );