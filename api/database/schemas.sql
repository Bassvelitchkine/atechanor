-- DROP TABLE IF EXISTS initiators;

CREATE TABLE initiators (
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    email TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE requests (
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    processed BOOLEAN NOT NULL DEFAULT 0,
    initiatorId TEXT NOT NULL,
    FOREIGN KEY (initiatorId)
        REFERENCES initiators (email)
            ON DELETE CASCADE
            ON UPDATE NO ACTION
);

CREATE TABLE profiles (
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    profileUrl TEXT NOT NULL PRIMARY KEY,
    email TEXT 
);

CREATE TABLE requests_profiles (
   requestId INTEGER,
   profileId TEXT,
   PRIMARY KEY (requestId, profileId),
   FOREIGN KEY (requestId) 
      REFERENCES requests (id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (profileId) 
      REFERENCES profiles (profileUrl) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);