CREATE TABLE IF NOT EXISTS users
(
    id             SERIAL PRIMARY KEY,
    username       varchar(50),
    google_user_id varchar(100),
    eid            varchar(20) UNIQUE,
    first_name     varchar(50),
    last_name      varchar(50),
    phone          varchar(50),
    is_banned      bool
);

CREATE TABLE IF NOT EXISTS employees
(
    id         SERIAL PRIMARY KEY,
    username   varchar(50),
    first_name varchar(50),
    last_name  varchar(50),
    phone      varchar(50)
);

CREATE TABLE IF NOT EXISTS locations
(
    id        SERIAL PRIMARY KEY,
    name      varchar(50),
    latitude  FLOAT,
    longitude FLOAT
);

CREATE TABLE IF NOT EXISTS requests
(
    id              SERIAL PRIMARY KEY,
    user_id         INT,
    start_location  INT,
    end_location    INT,
    start_latitude  FLOAT,
    start_longitude FLOAT,
    notes           TEXT,
    status_code     int,
    assigned_group  int,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (start_location) REFERENCES locations (id),
    FOREIGN KEY (end_location) REFERENCES locations (id)
);

CREATE TABLE IF NOT EXISTS seeus_config
(
    name  varchar(100) UNIQUE,
    value text
);
