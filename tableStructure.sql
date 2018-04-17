CREATE TABLE allusers
(
  userid VARCHAR(15)
    PRIMARY KEY,
  fname  VARCHAR(20),
  lname  VARCHAR(20),
  uname  VARCHAR(20)
);

CREATE TABLE blockusers
(
  userid VARCHAR(15) REFERENCES allusers(userid),
    PRIMARY KEY(userid)
);