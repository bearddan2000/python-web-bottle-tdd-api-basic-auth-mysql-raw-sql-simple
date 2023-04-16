DROP TABLE IF EXISTS `animal`.dog;

CREATE TABLE `animal`.dog (
	id INT PRIMARY KEY auto_increment,
	breed varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_chained`.dog;

CREATE TABLE `test_chained`.dog (
	id INT PRIMARY KEY auto_increment,
	breed varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_raw`.dog;

CREATE TABLE `test_raw`.dog (
	id INT PRIMARY KEY auto_increment,
	breed varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `test_api`.dog;

CREATE TABLE `test_api`.dog (
	id INT PRIMARY KEY auto_increment,
	breed varchar(25) NOT NULL,
	color varchar(10) NOT NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
