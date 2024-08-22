-- Creates a stored procedure that adds a new correction for a student

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

-- create procedure
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
DECLARE project_id INT;

-- check if the project already exists
SELECT id INTO project_id FROM projects WHERE name = project_name;

-- If project does not exist, insert it and get the new project_id
IF project_id IS NULL THEN
INSERT INTO projects (name) VALUES(project_name);
SET project_id = LAST_INSERT_ID();
END IF;

-- Insert the correction into the corrections table
INSERT INTO corrections(user_id, project_id, score)
VALUES(
    user_id,
    project_id,
    score
    );
END$$

DELIMITER ;
