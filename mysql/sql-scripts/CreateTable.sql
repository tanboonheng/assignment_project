create table user_info(
username VARCHAR(50) NOT NULL UNIQUE,
firstname VARCHAR(25) NOT NULL,
lastname VARCHAR(25) NOT NULL,
userid int PRIMARY KEY AUTO_INCREMENT);