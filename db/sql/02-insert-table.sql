DELIMITER $$

CREATE TRIGGER `animal`.tr_ins_after
    AFTER INSERT
    ON `animal`.dog FOR EACH ROW
BEGIN
    INSERT INTO `test_chained`.dog (id, breed, color) VALUES(new.id, new.breed, new.color);
    INSERT INTO `test_raw`.dog (id, breed, color) VALUES(new.id, new.breed, new.color);
    INSERT INTO `test_api`.dog (id, breed, color) VALUES(new.id, new.breed, new.color);
END$$    

TRUNCATE `animal`.dog;
TRUNCATE `test_chained`.dog;
TRUNCATE `test_raw`.dog;
TRUNCATE `test_api`.dog;

INSERT INTO `animal`.dog (id, breed, color)
VALUES
(default, 'Am Bulldog', 'White'),
(default, 'Blue Tick', 'Grey'),
(default, 'Labrador', 'Black'),
(default, 'Gr Shepard', 'Brown');

DROP TRIGGER `animal`.tr_ins_after;